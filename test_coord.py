#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: test_coord.py
# Auteur: Marc COATANHAY

"""
    Tests pour le module coordonnees.
"""

# Import des modules
import coord
import math
import unittest

# Définitions constantes et variables globales

# Définitions fonctions et classes
class CoordTest(unittest.TestCase):
    def test_rotations(self):
        U0 = coord.vecteur(1, 2, 3)
        U1 = coord.rotation1(math.pi/2, U0)
        U2 = coord.rotation2(math.pi/2, U1)
        U3 = coord.rotation3(math.pi/2, U2)
        reponse = coord.vecteur(3, -2, 1)
        test = True
        i = 0
        for ligne in U3:
            j = 0
            for colonne in ligne:
                test = test and (colonne == reponse[i][j])
                j += 1
            i += 1
        self.assertTrue(test)

if (__name__ == "__main__"):
    unittest.main()