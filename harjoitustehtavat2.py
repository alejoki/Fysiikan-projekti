from math import comb, factorial

# 19. Montako erilaista istumajärjestystä luokan 32 opiskelijasta saadaan?
tulos = factorial(32)
print(f"19. Istumajärjestysten määrä: {tulos}")

# 20. a) 10 henkilöä kättelevät kaikki toisiaan. Montako kättelyä suoritetaan?
tulos = comb(10, 2)
print(f"20a. Kättelyjen määrä: {tulos}")

# 20. b) 8 joukkuetta pelaavat pareittain. Montako ottelua pelataan?
tulos = comb(8, 2)
print(f"20b. Ottelujen määrä: {tulos}")

# 21. Mielipidekyselyssä oli 6 kysymystä ja niissä jokaisessa oli 5 erilaista vastausmahdollisuutta
tulos = 5 ** 6
print(f"21. Vastausmahdollisuuksien määrä: {tulos}")

# 22. Jonossa on 3 poikaa ja 4 tyttöä niin, että tytöt ovat jonon alussa
tulos = factorial(4) * factorial(3)
print(f"22. Erilaisten jonojen määrä: {tulos}")

# 23.Opiskelijan tulee vastata 10 kysymykestä kahdeksaan.
# a) Montako erilaista vastausyhdistelmää hänellä on?
tulos = comb(10, 8)
print(f"23a. Vastausyhdistelmien määrä: {tulos}")

# b) Entä jos näiden 8 vastauksen joukossa tulee olla vastaukset 3 ensimmäiseen kysymykseen?
tulos = comb(7, 5)
print(f"23b. Vastausyhdistelmien määrä kun 3 ensimmäistä pakko valita: {tulos}")

# 24. Montako erilaista ryhmää, jossa on 3 miestä ja 2 naista voidaan valita 7 miehestä ja 5 naisesta?
tulos = comb(7, 3) * comb(5, 2)
print(f"24. Erilaisten ryhmien määrä: {tulos}")