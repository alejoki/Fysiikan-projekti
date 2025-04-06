import numpy as np
import math
from scipy import stats
import matplotlib.pyplot as plt
from itertools import combinations

# Tehtävä 31
print("Tehtävä 31:")
p_jokeri = 1/8
x_values = np.arange(0, 4)
pmf = stats.binom.pmf(x_values, 3, p_jokeri)
    
print("Todennäköisyysjakauma:")
for x, p in zip(x_values, pmf):
    print(f"P(X = {x}) = {p:.6f}")
    
odotusarvo = 3 * p_jokeri
print(f"Odotusarvo: E(X) = {odotusarvo}")


# Tehtävä 32
print("\nTehtävä 32:")
p_success = 0.70
x_values = np.arange(0, 3)
pmf = stats.binom.pmf(x_values, 2, p_success)

print("Todennäköisyysjakauma:")
for x, p in zip(x_values, pmf):
    print(f"P(X = {x}) = {p:.6f}")

odotusarvo = 2 * p_success
print(f"Onnistuneiden heittojen lukumäärän odotusarvo: E(X) = {odotusarvo}")


# Tehtävä 34
print("\nTehtävä 34:")
p_kuutonen = 1/6
x_values = np.arange(0, 5)
pmf = stats.binom.pmf(x_values, 4, p_kuutonen)

print("Todennäköisyysjakauma kuutosten lukumäärälle:")
for x, p in zip(x_values, pmf):
    print(f"P(X = {x}) = {p:.6f}")


# Tehtävä 35
print("\nTehtävä 35:")
p_hylky = 0.20
x_values = np.arange(0, 3)
pmf = stats.binom.pmf(x_values, 2, p_hylky)
    
print("Todennäköisyysjakauma hylättävien tuotteiden määrälle:")
for x, p in zip(x_values, pmf):
    print(f"P(X = {x}) = {p:.6f}")
    
odotusarvo = 2 * p_hylky
keskihajonta = math.sqrt(2 * p_hylky * (1 - p_hylky))
print(f"Odotusarvo: E(X) = {odotusarvo}")
print(f"Keskihajonta: σ = {keskihajonta:.6f}")


# Tehtävä 36
print("\nTehtävä 36:")
x_values = np.arange(0, 4)
pmf = stats.hypergeom.pmf(x_values, M=6, n=3, N=3)
    
print("Todennäköisyysjakauma valkoisten pallojen lukumäärälle:")
for x, p in zip(x_values, pmf):
    print(f"P(X = {x}) = {p:.6f}")
    
odotusarvo = 3 * (3/6)
print(f"Valkoisten pallojen lukumäärän odotusarvo: E(X) = {odotusarvo}")


# Tehtävä 37:
print("\nTehtävä 37:")
kirjekuoret = [10, 20, 30, 40, 50]
kombinaatiot = list(combinations(kirjekuoret, 2))
summat = [sum(kombi) for kombi in kombinaatiot]
p = 1 / len(kombinaatiot)
summa_count = {}
for s in summat:
    if s in summa_count:
        summa_count[s] += 1
    else:
        summa_count[s] = 1
    
jakauma = {s: count * p for s, count in summa_count.items()}  
x_values = sorted(jakauma.keys())
    
print("Todennäköisyysjakauma voittosummille:")
for x in x_values:
    print(f"P(X = {x}€) = {jakauma[x]:.6f}")
    
odotusarvo = sum(x * jakauma[x] for x in jakauma)
print(f"Voittosumman odotusarvo: E(X) = {odotusarvo}€")