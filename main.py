# -*- coding: utf-8 -*-
import time
from avion import Avion
from aeroport import Aeroport
from meteo import Meteo

print("\n=== DÉMARRAGE DE LA SIMULATION ===\n")

# Création de l'aéroport avec 2 pistes
aeroport = Aeroport("Charles de Gaulle", 2)

# Initialisation de la météo avec mise à jour automatique toutes les 5 secondes
meteo = Meteo(intervalle=5)
aeroport.meteo = meteo  # On passe la météo à l'aéroport

# Création des avions
avions = [
    Avion("AF123", (50, 100), 800, "CDG"),
    Avion("BA456", (60, 110), 750, "LHR"),
    Avion("LH789", (70, 120), 820, "FRA"),
    Avion("DL321", (80, 130), 780, "ATL"),
    Avion("EK654", (90, 140), 900, "DXB")
]

# Affichage initial
print("\n--- ÉTAT INITIAL DES AVIONS ---")
for avion in avions:
    avion.afficher_info()

aeroport.afficher_etat()

# Tentative d'atterrissage des avions
print("\n--- DÉBUT DES ATTERRISSAGES ---")
for avion in avions:
    aeroport.assigner_avion_a_piste(avion)
    time.sleep(2)  # Simule un petit délai entre chaque atterrissage

# Affichage après les atterrissages
print("\n--- ÉTAT DES AVIONS APRÈS ATTERRISSAGE ---")
for avion in avions:
    avion.afficher_info()

aeroport.afficher_etat()

# Attente pour voir la météo changer plusieurs fois en temps réel
print("\n--- OBSERVATION DE LA MÉTÉO EN TEMPS RÉEL (10s) ---")
time.sleep(10)  # Laisse tourner la simulation pour voir la météo changer plusieurs fois

# Libération des pistes et gestion de la file d'attente
print("\n--- LIBÉRATION DES PISTES ---")
for i in range(1, 3):  # On libère les deux pistes une par une
    aeroport.liberer_piste(i)

# Affichage après libération des pistes
aeroport.afficher_etat()

# Arrêt du thread de mise à jour météo
meteo.arreter_meteo()

# Affichage final des avions et statistiques de l’aéroport
print("\n=== STATISTIQUES FINALES ===")
aeroport.afficher_etat()

print("\n=== FIN DE LA SIMULATION ===\n")
