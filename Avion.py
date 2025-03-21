# -*- coding: utf-8 -*-
from enum import Enum

class EtatAvion(Enum):
    EN_VOL = "En vol"
    EN_ATTENTE = "En attente"
    ATTERRISSAGE = "Atterrissage"
    DECOLLAGE = "Décollage"

class Avion:
    def __init__(self, id_avion, position, vitesse, destination):
        self.id = id_avion  # Identifiant unique de l'avion
        self.position = position  # Position (x, y)
        self.vitesse = vitesse  # Vitesse en km/h
        self.destination = destination  # Destination de l'avion
        self.etat = EtatAvion.EN_VOL  # Par défaut, l'avion est en vol

    def deplacer(self, nouvelle_position):
        """Met à jour la position de l'avion."""
        self.position = nouvelle_position

    def changer_etat(self, nouvel_etat):
        """Change l'état de l'avion."""
        self.etat = nouvel_etat

    def afficher_info(self):
        """Affiche les informations de l'avion."""
        print(f"Avion {self.id} - Position: {self.position}, Vitesse: {self.vitesse} km/h, "
              f"Destination: {self.destination}, État: {self.etat.value}")
