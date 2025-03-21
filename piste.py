# -*- coding: utf-8 -*-
from enum import Enum
from collections import deque
from avion import Avion, EtatAvion
from meteo import Meteo, TypeMeteo
import time  # Pour simuler les retards

class EtatPiste(Enum):
    LIBRE = "Libre"
    OCCUPEE = "Occupée"

class Piste:
    def __init__(self, id_piste):
        self.id = id_piste  # Identifiant unique de la piste
        self.etat = EtatPiste.LIBRE  # État initial de la piste
        self.avion_en_cours = None  # Avion actuellement sur la piste
        self.file_attente = deque()  # File d'attente FIFO des avions

    def est_libre(self):
        """Vérifie si la piste est libre."""
        return self.etat == EtatPiste.LIBRE

    def assigner_avion(self, avion, meteo):
        """Assigne un avion à la piste si elle est libre ou l'ajoute à la file d'attente en fonction de la météo."""
        if meteo.etat in [TypeMeteo.ORAGE, TypeMeteo.TEMPETE]:
            print(f"ATTENTION : Météo dangereuse ({meteo.etat.value}) ! Avion {avion.id} en attente.")
            self.file_attente.append(avion)
            avion.changer_etat(EtatAvion.EN_ATTENTE)
            return

        if self.est_libre():
            self.avion_en_cours = avion
            self.etat = EtatPiste.OCCUPEE
            avion.changer_etat(EtatAvion.ATTERRISSAGE)
            print(f"Piste {self.id} assignée à l'avion {avion.id}. Atterrissage en cours...")

            # Ajout d'un délai en cas de mauvaise météo
            if meteo.etat in [TypeMeteo.PLUIE, TypeMeteo.BROUILLARD]:
                print(f"Météo difficile ({meteo.etat.value}) : Atterrissage retardé...")
                time.sleep(2)  # Simule un retard

            print(f"Avion {avion.id} a atterri sur la piste {self.id}.")
        else:
            self.file_attente.append(avion)
            avion.changer_etat(EtatAvion.EN_ATTENTE)
            print(f"Piste {self.id} occupée. Avion {avion.id} ajouté à la file d'attente.")

    def liberer_piste(self):
        """Libère la piste après utilisation et assigne le prochain avion en attente si possible."""
        if self.avion_en_cours:
            print(f"Piste {self.id} libérée de l'avion {self.avion_en_cours.id}.")
        self.avion_en_cours = None
        self.etat = EtatPiste.LIBRE

        if self.file_attente:
            prochain_avion = self.file_attente.popleft()
            self.assigner_avion(prochain_avion, Meteo())  # On utilise la météo actuelle
