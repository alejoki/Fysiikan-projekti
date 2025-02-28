import streamlit as st
import pandas as pd
import numpy as np
from scipy.signal import butter, lfilter, find_peaks
import plotly.express as px

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def calculate_steps(data, height, distance):
    peaks, _ = find_peaks(data, height=height, distance=distance)
    return len(peaks)

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)

    a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distance = R * c
    return distance

accel_data = pd.read_csv("Accelerometer.csv")
location_data = pd.read_csv("Location.csv")
accel_data = accel_data[accel_data["Time (s)"] >= 3]
location_data = location_data[location_data["Time (s)"] >= 3]
accel_y = accel_data["Acceleration y (m/s^2)"]
accel_y = accel_y - accel_y.mean()

fs = len(accel_data) / (accel_data["Time (s)"].max() - accel_data["Time (s)"].min())

cutoff = 2
order = 5
filtered_accel_y = butter_lowpass_filter(accel_y, cutoff, fs, order)
height = 0.1
distance_seconds = 0.2
distance = int(distance_seconds * fs)

steps_filtered = calculate_steps(filtered_accel_y, height=height, distance=distance)

N = len(accel_y)
yf = np.fft.fft(accel_y)
xf = np.fft.fftfreq(N, 1 / fs)
psd = (np.abs(yf) ** 2) / (N * fs)
L = np.where((xf > 0.5) & (xf < 4))
psd_walk = psd[L]
freq_walk = xf[L]
dominant_frequency = freq_walk[np.argmax(psd_walk)]

steps_fourier = int(dominant_frequency * (accel_data["Time (s)"].max() - accel_data["Time (s)"].min()))

average_speed = location_data["Velocity (m/s)"].mean()
total_distance = 0
for i in range(1, len(location_data)):
    total_distance += calculate_distance(
        location_data["Latitude (°)"].iloc[i - 1],
        location_data["Longitude (°)"].iloc[i - 1],
        location_data["Latitude (°)"].iloc[i],
        location_data["Longitude (°)"].iloc[i],
    )

step_length = total_distance / steps_filtered

st.title("Kävelylenkki")
st.header("Yhteenveto")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Askelmäärä (suodatettu)", steps_filtered)
col2.metric("Askelmäärä (Fourier)", steps_fourier)
col3.metric("Keskinopeus (m/s)", f"{average_speed:.2f}")
col4.metric("Matka (m)", f"{total_distance:.2f}")
col5.metric("Askelpituus (m)", f"{step_length:.2f}")
st.subheader("Reitti Kartalla")
fig = px.scatter_map(location_data, lat="Latitude (°)", lon="Longitude (°)", color="Velocity (m/s)",
                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=10, zoom=15)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.plotly_chart(fig)
st.header("Kuvaajat")
st.subheader("Suodatettu Kiihtyvyys (y-komponentti)")
filtered_df = pd.DataFrame({'Time (s)': accel_data["Time (s)"], 'Acceleration y (m/s^2)': filtered_accel_y})
st.line_chart(filtered_df, x='Time (s)', y='Acceleration y (m/s^2)')
st.subheader("Tehospektri")
chart_data = pd.DataFrame(np.transpose(np.array([freq_walk, psd_walk])), columns=["freq", "psd"])
st.line_chart(chart_data, x='freq', y='psd', y_label='Teho', x_label='Taajuus [Hz]')
