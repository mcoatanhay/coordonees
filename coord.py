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
    from coordonnees.repertoire import filerep
    filerep()
    precession_uai2000_file = 'precession_uai2000.dat'
except:
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    # Définitions constantes et variables globales
    root = Tk()
    precession_uai2000_file = askopenfilename(
            parent=root,
            filetypes=( ("Tous les fichiers", "*.*"),
                        ("Fichier dat", "*.dat")
                            ),
            title="**Indiquer le chemin du fichier 'precession_uai2000.dat'")
    root.destroy()

import incertitudes.incert as incert
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

def parametres_precession(t):
    """
        Calcul les paramètres de la précession à partir des coefficients
        uai 2000.
        Entrée :
            t en dizaine de siècles juliens à partir de l'époque 2000.0
                t = [(JJ) - (JJ)2000.0] / 365250
        Retour :
            z, theta, zeta, khi, omega, psi, epsilon
    """
    calculs = []
    resultat = {}
    for parametre, coefs_liste in precession_uai2000_coef.items():
        valeur = 0
        poly = ""
        max_i = len(coefs_liste)
        for i in range(0, max_i):
            monome = coefs_liste[i]*(t**i)
            valeur += monome
            poly += coefs_liste[i] + "*t^" + str(i)
            if i < (max_i - 1):
                poly += " + "
        calculs.append({parametre: poly})
        calculs.append({parametre: valeur})
        resultat[parametre] = valeur
    resultat['calculs'] = calculs
    return resultat

def polairedexyz(U):
    """
        Calcul les coordonnées polaires à partir des coordonnées cartésiennes.
        Entrée :
            U vecteur = [[x]
                         [y]
                         [z]]
        Retour :
            tuple :
                    psi dans ]-pi, pi]
                    phi dans ]-pi, pi]
                    r
    """
    x = U[0][0]
    y = U[1][0]
    z = U[2][0]
    r = incert.sqrt(x**2 + y**2 + z**2)
    om = incert.sqrt(x**2 + y**2)
    phi = incert.asin(z/r)
    if(x.valeur > 0):
        theta = incert.atan(incert.iabs(y/x))
        if(y.valeur < 0):
            psi = -theta
        else:
            psi = theta
    elif(x.valeur < 0):
        theta = incert.atan(incert.iabs(y/x))
        if(y.valeur < 0):
            psi = theta - incert.pi
        else:
            psi = incert.pi - theta
    else:
        if(y.valeur < 0):
            psi =  -incert.pi/2
        elif(y.valeur > 0):
            psi = incert.pi/2
        else:
            message = "x et y sont égaux à zéro !"
            raise ValueError(message)
    return (psi, phi, r)

def precession_uai2000_extract():
    """
        Extraction des coefficients de précession uai 2000.
        Retour :
            dictionnaire
                'epsilon (")'   :[liste coefs]
                'omega (")'     :[liste coefs]
                'psi (")'       :[liste coefs]
                'khi (")'       :[liste coefs]
                'theta (")'     :[liste coefs]
                'zeta (")'      :[liste coefs]
                'z (")'         :[liste coefs]
    """
    f = open('precession_uai2000.dat', "r")
    # Lecture complète du fichier, data = liste des lignes
    lignes = f.readlines()
    f.close()
    for ligne in lignes:
        data = []
        # Séparation des différents éléments
        # split, séparation autour du caractère ';'
        # strip, enlève les espaces et caractèrs spéciaux
        ligne = ligne.strip().split(";")
        parametre = ligne[0]
        # Conversion des valeurs en incert
        for valeur in ligne[1:]:
            data.append(valeur)
        precession_uai2000_coef[parametre] = data

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
    R = np.array([[1, 0,                    0],
                  [0, incert.cos(theta),    incert.sin(theta)],
                  [0, -incert.sin(theta),   incert.cos(theta)]])
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
    R = np.array([[incert.cos(theta),   0, -incert.sin(theta)],
                  [0,                   1, 0],
                  [incert.sin(theta),   0, incert.cos(theta)]])
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
    R = np.array([[incert.cos(theta),   incert.sin(theta),  0],
                  [-incert.sin(theta),  incert.cos(theta),  0],
                  [0,                   0,                  1]])
    return np.dot(R, U)

def vecteur(x, y, z):
    """
        Compose un vecteur à trois dimensions avec les valeurs données.
        Entrée :
            x, y et z
        Retour :
            Vecteur image
    """
    return np.array([[x],
                     [y],
                     [z]])

def xyzdepolaire(psi, phi, r):
    """
        Calcul les coordonnées x, y et z à partir des coordonnées polaires.
        Entrée :
            psi, phi et r
        Retour :
            Vecteur image
    """
    x = r*incert.cos(psi)*incert.cos(phi)
    y = r*incert.sin(psi)*incert.cos(phi)
    z = r*incert.sin(phi)
    return np.array([[x],
                     [y],
                     [z]])

precession_uai2000_coef = {}
precession_uai2000_extract()