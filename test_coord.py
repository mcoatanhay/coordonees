#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: test_coord.py
# Auteur: Marc COATANHAY

"""
    Tests pour le module coordonnees.
"""

# Import des modules
from coord import *
import math
import unittest

# Définitions constantes et variables globales

# Définitions fonctions et classes
class CoordTest(unittest.TestCase):
    def test_rotations(self):
        U0 = vecteur(1, 2, 3)
        U1 = rotation1(math.pi/2, U0)
        U2 = rotation2(math.pi/2, U1)
        U3 = rotation3(math.pi/2, U2)
        reponse = vecteur(3, -2, 1)
        test = True
        i = 0
        for ligne in U3:
            j = 0
            for colonne in ligne:
                test = test and (colonne == reponse[i][j])
                j += 1
            i += 1
        self.assertTrue(egalite_vecteurs(reponse, U3))

if (__name__ == "__main__"):
    unittest.main()