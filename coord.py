#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: coordonnees.py
# Auteur: Marc COATANHAY

"""
    Changements de coordonnées astronomiques par calcul matriciel.
    D'après "connaissance des temps" édition 2018.
"""

# Import des modules
try:
    import mes_modules_path
except:
    pass
from incertitudes.incert import cos, sin, i
import numpy as np

# Définitions constantes et variables globales

# Définitions fonctions et classes
def egalite_vecteurs(U1, U2):
    """
        Vérifie l'égalité de deux vecteurs.
        Entrée:
            U1 et U2 deux vecteurs (matrice)
        Retour :
            boleen : True ou False
    """
    test = True
    i = 0
    for ligne in U1:
        j = 0
        for colonne in ligne:
            test = test and (colonne == U2[i][j])
            j += 1
        i += 1
    return test

def rotation1(theta, U):
    """
        Transforme les coordonnées cartésiennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Ox).
        Entrée :
            theta, angle de rotation (float)
            U vecteur = [[x]
                         [y]
                         [z]]
        Retour :
            vecteur image
    """
    R = np.array([[1, 0,           0],
                  [0, cos(theta),  sin(theta)],
                  [0, -sin(theta), cos(theta)]])
    return np.dot(R, U)

def rotation2(theta, U):
    """
        Transforme les coordonnées cartésiennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Oy).
        Entrée :
            theta, angle de rotation (float)
            U vecteur = [[x]
                         [y]
                         [z]]
        Retour :
            vecteur image
    """
    R = np.array([[cos(theta), 0, -sin(theta)],
                  [0,          1, 0],
                  [sin(theta), 0, cos(theta)]])
    return np.dot(R, U)

def rotation3(theta, U):
    """
        Transforme les coordonnées cartésiennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Oz).
        Entrée :
            theta, angle de rotation (float)
            U vecteur = [[x]
                         [y]
                         [z]]
        Retour :
            vecteur image
    """
    R = np.array([[cos(theta),  sin(theta), 0],
                  [-sin(theta), cos(theta), 0],
                  [0,           0,          1]])
    return np.dot(R, U)

def vecteur(x, y, z):
    """
        Compose un vecteur à trois dimensions avec les valeurs données.
        Entrée :
            x, y et z
        Retour :
            Vecteur image
    """
    return np.array([[i(x)],
                     [i(y)],
                     [i(z)]])

def xyzdepolaire(psi, phi, r):
    """
        Calcul les coordonnées x, y et z à partir des coordonnées polaires
        psi, phi et r.
        Entrée :
            psi, phi et r
        Retour :
            Vecteur image
    """
    x = r*cos(psi)*cos(phi)
    y = r*sin(psi)*cos(phi)
    z = r*sin(phi)
    return np.array([[x],
                     [y],
                     [z]])
