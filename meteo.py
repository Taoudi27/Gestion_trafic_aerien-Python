# -*- coding: utf-8 -*-
import random
import time
import threading
from enum import Enum

class TypeMeteo(Enum):
    BEAU_TEMPS = "Beau temps"
    PLUIE = "Pluie"
    BROUILLARD = "Brouillard"
    ORAGE = "Orage"
    TEMPETE = "Tempête"

class Meteo:
    def __init__(self, intervalle=5):
        """Initialise la météo avec un état aléatoire et un changement automatique."""
        self.etat = random.choice(list(TypeMeteo))
        self.intervalle = intervalle  # Temps en secondes entre chaque mise à jour
        self._stop_event = threading.Event()  # Permet d'arrêter proprement le thread
        self.thread = threading.Thread(target=self._maj_meteo_en_continue, daemon=True)
        self.thread.start()  # Lancer la mise à jour automatique

    def changer_meteo(self):
        """Change la météo aléatoirement."""
        self.etat = random.choice(list(TypeMeteo))
        print(f"\n[INFO] Nouvelle météo : {self.etat.value}")

    def _maj_meteo_en_continue(self):
        """Change automatiquement la météo toutes les X secondes."""
        while not self._stop_event.is_set():
            time.sleep(self.intervalle)
            self.changer_meteo()

    def arreter_meteo(self):
        """Arrête le thread proprement."""
        self._stop_event.set()
        self.thread.join()

    def afficher_meteo(self):
        """Affiche la météo actuelle."""
        print(f"Météo actuelle : {self.etat.value}")
