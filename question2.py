# MBANGA TSHIBANDA ---PREPOLYTECHNIQUE UNIKIN---
# TRAVAIL PRATIQUE D'INFORMATIQUE N°1
# QUESTION 2 

import random
from datetime import datetime

# IPs locales (réseau national simulé)
ips_locales = ["192.168.1." + str(i) for i in range(1, 30)]

# IPs étrangères suspectes
ips_etrangeres = ["203.0.113." + str(i) for i in range(1, 15)]

# Simuler un flux réseau (log fictif)
flux_reseau = []

for _ in range(50):  # 50 connexions simulées
    ip_source = random.choice(ips_locales + ips_etrangeres)
    port = random.choice([22, 80, 443, 8080, 3306, 21])  # ports courants ou sensibles
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    flux_reseau.append((timestamp, ip_source, port))

# Analyse : détection des IPs étrangères
print("== DÉTECTION D'INTRUSIONS POTENTIELLES ==")
for log in flux_reseau:
    timestamp, ip, port = log
    if ip.startswith("203.0.113."):  # IP étrangère simulée
        print(f"[ALERTE] Suspicion de trafic étranger : IP = {ip}, Port = {port}, Heure = {timestamp}")
