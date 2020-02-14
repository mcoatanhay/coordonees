#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: coordonnees.py
# Auteur: Marc COATANHAY

"""
    Changements de coordonnées, calcul matriciel.
    D'après "connaissance des temps" édition 2018.
"""

# Import des modules
try:
    import mes_modules_path
except:
    pass
from incertitudes.incert import cos, sin
import numpy as np

# Définitions constantes et variables globales

# Définitions fonctions et classes
def rotation1(theta, x, y, z):
    """
        Transforme les coordonnées cartésiennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Ox).
    """
    R = np.array([[1, 0,           0],
                  [0, cos(theta),  sin(theta)],
                  [0, -sin(theta), cos(theta)]])
    U = np.array([[x],
                  [y],
                  [z]])
    return np.dot(R, U)

def rotation2(theta, x, y, z):
    """
        Transforme les coordonnées cartésiennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Oy).
    """
    R = np.array([[cos(theta), 0, -sin(theta)],
                  [0,          1, 0],
                  [sin(theta), 0, cos(theta)]])
    U = np.array([[x],
                  [y],
                  [z]])
    return np.dot(R, U)

def rotation3(theta, x, y, z):
    """
        Transforme les coordonnées cartésiennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Oz).
    """
    R = np.array([[cos(theta),  sin(theta), 0],
                  [-sin(theta), cos(theta), 0],
                  [0,           0,          1]])
    U = np.array([[x],
                  [y],
                  [z]])
    return np.dot(R, U)

def xyzdepolaire(psi, phi, r):
    """
        Calcul les coordonnées x, y et z à partir des coordonnées polaires
        psi, phi et r.
    """
    x = r*cos(psi)*cos(phi)
    y = r*sin(psi)*cos(phi)
    z = r*sin(phi)
    return np.array([[x],
                     [y],
                     [z]])

