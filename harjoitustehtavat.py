import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from fractions import Fraction

# Tehtävä 1
print("Tehtävä 1: Opiskelijoiden pituusjakauma")

heights = {"1.51-1.53": 2, "1.54-1.56": 2, "1.57-1.59": 5, "1.60-1.62": 38, "1.63-1.65": 62, "1.66-1.68": 110, "1.69-1.71": 126, "1.72-1.74": 130, "1.75-1.77": 126, "1.78-1.80": 72, "1.81-1.83": 42, "1.84-1.86": 23, "1.87-1.89": 7, "1.90-1.92": 1}

total_students = sum(heights.values())
print(f"Opiskelijoiden lukumäärä: {total_students}")

midpoints, frequencies = [], []
for height_range, count in heights.items():
    lower, upper = map(float, height_range.split('-'))
    midpoints.append((lower + upper) / 2)
    frequencies.append(count)

height_rv = stats.rv_discrete(name='height', values=(range(len(midpoints)), np.array(frequencies)/total_students))

weighted_mean = np.average(midpoints, weights=frequencies)
weighted_var = np.average((np.array(midpoints) - weighted_mean)**2, weights=frequencies)
weighted_std = np.sqrt(weighted_var)

print(f"Keskipituus: {weighted_mean:.4f} m")
print(f"Keskihajonta: {weighted_std:.4f} m")

prob_over_180cm = sum(freq for range_str, freq in heights.items() if float(range_str.split('-')[0]) >= 1.80) / total_students
frac_over_180cm = Fraction(sum(freq for range_str, freq in heights.items() if float(range_str.split('-')[0]) >= 1.80), total_students).limit_denominator()
print(f"a) Todennäköisyys että opiskelija on yli 180 cm pitkä: {frac_over_180cm}")

prob_163_to_174 = sum(freq for range_str, freq in heights.items() if (float(range_str.split('-')[0]) >= 1.63 and float(range_str.split('-')[1]) <= 1.74)) / total_students
frac_163_to_174 = Fraction(sum(freq for range_str, freq in heights.items() if (float(range_str.split('-')[0]) >= 1.63 and float(range_str.split('-')[1]) <= 1.74)), total_students).limit_denominator()
print(f"b) Todennäköisyys että opiskelija on 163-174 cm pitkä: {frac_163_to_174}")

prob_under_160 = sum(freq for range_str, freq in heights.items() if float(range_str.split('-')[1]) < 1.60) / total_students
frac_under_160 = Fraction(sum(freq for range_str, freq in heights.items() if float(range_str.split('-')[1]) < 1.60), total_students).limit_denominator()
print(f"c) Todennäköisyys että opiskelija on alle 160 cm pitkä: {frac_under_160}")


# Tehtävä 2
print("\nTehtävä 2: Janan pituuden arviointi")

estimations = [2, 3, 0, 5, 6, 1, 2, 4, 3, 1, 3, 2, 1, 0, 1, 1, 0, 2, 1, 1, 0, 5, 0, 2, 5, 3, 1, 1, 2, 0, 4, 3, 0, 0, 2, 1, 0, 3, 5, 4, 2, 0, 5, 3, 1, 6, 2, 4, 1, 1, 4, 7, 2, 0, 2, 1, 0, 4, 4, 3]

mean_estimation = np.mean(estimations)
std_estimation = np.std(estimations, ddof=1)

print(f"Arvioiden keskiarvo: {mean_estimation:.4f} cm")
print(f"Arvioiden keskihajonta: {std_estimation:.4f} cm")

unique_estimates, counts = np.unique(estimations, return_counts=True)
freq_dist = stats.rv_discrete(name='estimation', values=(unique_estimates, counts/len(estimations)))

correct_value = round(mean_estimation)
correct_estimations = sum(1 for e in estimations if abs(e - correct_value) <= 1)
prob_correct = correct_estimations / len(estimations)
frac_correct = Fraction(correct_estimations, len(estimations)).limit_denominator()

print(f"Todennäköisyys että satunnaisesti valittu opiskelija arvioi janan pituuden 1 cm tarkkuudella oikein: {frac_correct}")


# Tehtävä 3
print("\nTehtävä 3: Autojen korjaustilastot")

km_ranges = {"0-10000": 50, "10001-20000": 93, "20001-30000": 293, "30001-40000": 391, "40001-50000": 183, "50001+": 40}

total_cars = sum(km_ranges.values())
print(f"Autojen kokonaismäärä: {total_cars}")

range_midpoints, car_counts = [], []
for km_range, count in km_ranges.items():
    if '-' in km_range:
        lower, upper = map(int, km_range.split('-'))
        midpoint = (lower + upper) / 2
    else:
        midpoint = 55000
    range_midpoints.append(midpoint)
    car_counts.append(count)

car_dist = stats.rv_discrete(name='car_repair', values=(range(len(range_midpoints)), np.array(car_counts)/total_cars))

prob_a_b = (km_ranges["0-10000"] + km_ranges["10001-20000"]) / total_cars
frac_a_b = Fraction(km_ranges["0-10000"] + km_ranges["10001-20000"], total_cars).limit_denominator()
prob_b = km_ranges["20001-30000"] / total_cars
frac_b = Fraction(km_ranges["20001-30000"], total_cars).limit_denominator()
prob_c = km_ranges["30001-40000"] / total_cars
frac_c = Fraction(km_ranges["30001-40000"], total_cars).limit_denominator()
prob_d = (km_ranges["40001-50000"] + km_ranges["50001+"]) / total_cars
frac_d = Fraction(km_ranges["40001-50000"] + km_ranges["50001+"], total_cars).limit_denominator()

print(f"a) P(enintään 20 000 km): {frac_a_b}")
print(f"b) P(20 001 - 30 000 km): {frac_b}")
print(f"c) P(30 001 - 40 000 km): {frac_c}")
print(f"d) P(yli 40 000 km): {frac_d}")

sum_prob = prob_a_b + prob_b + prob_c + prob_d
frac_sum = Fraction(int(sum_prob * total_cars + 0.5), total_cars).limit_denominator()
print(f"Todennäköisyyksien summa: {frac_sum}")

cars_over_30k = km_ranges["30001-40000"] + km_ranges["40001-50000"] + km_ranges["50001+"]
prob_repair_next_10k = km_ranges["30001-40000"] / cars_over_30k
frac_repair_next_10k = Fraction(km_ranges["30001-40000"], cars_over_30k).limit_denominator()

print(f"e) Todennäköisyys että auto tarvitsee ensimmäisen korjauksen seuraavan 10 000 km aikana, jos se on ajanut 30 000 km ilman korjauksia: {frac_repair_next_10k}")


# Tehtävä 4
print("\nTehtävä 4: Kahden nopan summan todennäköisyys")

die1, die2 = stats.randint(1, 7), stats.randint(1, 7)

n_simulations = 100000
die1_rolls, die2_rolls = die1.rvs(size=n_simulations), die2.rvs(size=n_simulations)
sums = die1_rolls + die2_rolls

prob_sum_1, prob_sum_5 = np.mean(sums == 1), np.mean(sums == 5)
prob_sum_11, prob_sum_greater_7 = np.mean(sums == 11), np.mean(sums > 7)

sum_probs = np.zeros(13)
for i in range(1, 7):
    for j in range(1, 7):
        sum_probs[i+j] += 1/36

print(f"a) P(summa=1): {Fraction(0, 36)}")
print(f"b) P(summa=5): {Fraction(4, 36).limit_denominator()}")
print(f"c) P(summa=11): {Fraction(2, 36).limit_denominator()}")
print(f"d) P(summa>7): {Fraction(15, 36).limit_denominator()}")


# Tehtävä 5
print("\nTehtävä 5: Kolme kolikonheittoa")

n_flips, p_heads = 3, 0.5
coin_dist = stats.binom(n_flips, p_heads)

prob_4_heads, prob_3_heads, prob_2_heads = 0, coin_dist.pmf(3), coin_dist.pmf(2)
prob_1_head, prob_0_heads = coin_dist.pmf(1), coin_dist.pmf(0)

print(f"a) P(4 kruunaa): {Fraction(0, 8)}")
print(f"b) P(3 kruunaa): {Fraction(1, 8)}")
print(f"c) P(2 kruunaa): {Fraction(3, 8)}")
print(f"d) P(1 kruuna): {Fraction(3, 8)}")
print(f"e) P(0 kruunaa): {Fraction(1, 8)}")


# Tehtävä 6
print("\nTehtävä 6: Kaksinumeroinen luku jaollinen 2:lla tai 5:llä")

two_digit_numbers = [10*i + j for i in range(1, 6) for j in range(1, 6)]
total_numbers = len(two_digit_numbers)

numbers_array = np.array(two_digit_numbers)
divisible_by_2, divisible_by_5 = numbers_array[numbers_array % 2 == 0], numbers_array[numbers_array % 5 == 0]
divisible_by_either = np.union1d(divisible_by_2, divisible_by_5)

prob_divisible = len(divisible_by_either) / total_numbers
frac_divisible = Fraction(len(divisible_by_either), total_numbers).limit_denominator()
print(f"Todennäköisyys, että kaksinumeroinen luku on jaollinen 2:lla tai 5:llä: {frac_divisible}")


# Tehtävä 7
print("\nTehtävä 7: Kahden nopan pistesummaksi 10, 11, tai 12")

prob_sum_10_to_12 = sum_probs[10] + sum_probs[11] + sum_probs[12]
frac_sum_10_to_12 = Fraction(6, 36).limit_denominator()
print(f"Todennäköisyys saada pistesummaksi 10, 11 tai 12: {frac_sum_10_to_12}")


# Tehtävä 8
print("\nTehtävä 8: Todennäköisyys saada arvosana 5 vähintään yhdessä kokeessa")

prob_math_5, prob_physics_5, prob_both_5 = 0.15, 0.12, 0.07
prob_at_least_one_5 = prob_math_5 + prob_physics_5 - prob_both_5
frac_at_least_one_5 = Fraction(int(prob_at_least_one_5 * 100), 100).limit_denominator()

print(f"Todennäköisyys saada arvosana 5 vähintään yhdessä kokeessa: {frac_at_least_one_5}")


# Tehtävä 9
print("\nTehtävä 9: Suojatien ylittäjän odotusaika")

max_wait, green_time = 40, 20
cycle_time = max_wait + green_time

wait_dist = stats.uniform(0, max_wait)
prob_wait_at_most_30s = wait_dist.cdf(30)
frac_wait_at_most_30s = Fraction(30, 40).limit_denominator()

print(f"Todennäköisyys, että suojatien ylittäjä joutuu odottamaan korkeintaan 30s: {frac_wait_at_most_30s}") 