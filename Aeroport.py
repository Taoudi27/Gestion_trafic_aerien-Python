
# -*- coding: utf-8 -*-
from piste import Piste
from avion import Avion, EtatAvion
from meteo import Meteo, TypeMeteo
from collections import deque
import time

class Aeroport:
    def __init__(self, nom, nb_pistes):
        """Initialise un aéroport avec un nom et un certain nombre de pistes."""
        self.nom = nom
        self.pistes = [Piste(i+1) for i in range(nb_pistes)]
        self.file_attente = deque()  # File d'attente globale des avions
        self.meteo = Meteo()  # Météo actuelle
        self.historique_atterrissages = []  # Liste des avions qui ont atterri
        self.nombre_vols = 0  # Nombre total de vols traités

    def afficher_etat(self):
        """Affiche l'état des pistes, de la file d'attente et du trafic aérien."""
        print(f"\n=== État de l'Aéroport {self.nom} ===")
        print(f"Météo actuelle : {self.meteo.etat.value}")
        print(f"Nombre total de vols traités : {self.nombre_vols}")
        
        for piste in self.pistes:
            etat_piste = "Libre" if piste.est_libre() else f"Occupée par {piste.avion_en_cours.id}"
            print(f" - Piste {piste.id}: {etat_piste}")

        print(f"Avions en attente : {[avion.id for avion in self.file_attente]}")

        if self.historique_atterrissages:
            print("\n--- Historique des atterrissages ---")
            for avion in self.historique_atterrissages:
                print(f"Avion {avion.id} a atterri avec succès.")

    def assigner_avion_a_piste(self, avion):
        """Tente d'assigner un avion à une piste libre."""
        for piste in self.pistes:
            if piste.est_libre():
                piste.assigner_avion(avion, self.meteo)
                self.nombre_vols += 1  # Augmenter le compteur de vols
                self.historique_atterrissages.append(avion)  # Ajouter à l'historique
                return
        
        # Si aucune piste libre, ajouter à la file d'attente
        print(f"Aucune piste disponible. Avion {avion.id} ajouté à la file d'attente.")
        self.file_attente.append(avion)

    def gerer_file_attente(self):
        """Vérifie les pistes libres et y assigne les avions en attente."""
        while self.file_attente and any(piste.est_libre() for piste in self.pistes):
            avion = self.file_attente.popleft()
            self.assigner_avion_a_piste(avion)

    def liberer_piste(self, id_piste):
        """Libère une piste et assigne un avion en attente si possible."""
        for piste in self.pistes:
            if piste.id == id_piste and not piste.est_libre():
                piste.liberer_piste()
                self.gerer_file_attente()
                return
        print(f"Piste {id_piste} déjà libre ou inexistante.")

    def changer_meteo(self):
        """Change la météo et affiche l'impact."""
        self.meteo.changer_meteo()
        print(f"\nChangement de météo : {self.meteo.etat.value}")
