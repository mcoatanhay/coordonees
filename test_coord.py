#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: test_coord.py
# Auteur: Marc COATANHAY

"""
    Tests pour le module coordonnees.
"""

# Import des modules
try:
    import mes_modules_path
except:
    pass
from coord import *
import incertitudes.incert as incert
import unittest

# Définitions constantes et variables globales

# Définitions fonctions et classes
class CoordTest(unittest.TestCase):
    def test_polairedexyz(self):
        afficher_calculs = False
        reponses = []
        resultats = []
        for i in range(0, 9):
            psi = incert.pi*(i - 4)/4
            for j in range(0,5):
                phi = incert.pi*(j - 2)/4
                reponses.append((psi, phi, incert.un))
                resultats.append(
                    polairedexyz(
                        xyzdepolaire(psi, phi, incert.un)))
        if afficher_calculs:
            print()
            print("----------- test_polairedexyz")
            compteur = 0
            for resultat in resultats:
                form = '>6.1f'
                print(
                    format((resultat[0]*180/incert.pi).valeur, form),
                    format((reponses[compteur][0]*180/incert.pi).valeur, form),
                    format((resultat[1]*180/incert.pi).valeur, form),
                    format((reponses[compteur][1]*180/incert.pi).valeur, form)
                    )
                compteur += 1
        self.assertEqual(reponses, resultats)

    def test_parametres_precession(self):
        afficher_calculs = False
        reponses = {
        'epsilon (")': 84371.1487,
        'omega (")': 84381.4448,
        'psi (")': 1108.4134,
        'khi (")': 2.2063,
        'theta (")': 440.9273,
        'zeta (")': 507.3828,
        'z (")': 507.4212}
        t = incert.it(22/1000, 0)
        resultat = parametres_precession(t)
        if afficher_calculs:
            print()
            print("----------- test_parametres_precession")
            for ligne in resultat['calculs']:
                print(ligne)
            print('epsilon (") :', resultat['epsilon (")'])
            print('omega (") :', resultat['omega (")'])
            print('psi (") :', resultat['psi (")'])
            print('khi (") :', resultat['khi (")'])
            print('theta (") :', resultat['theta (")'])
            print('zeta (") :', resultat['zeta (")'])
            print('z (") :', resultat['z (")'])
        del resultat['calculs']
        self.assertEqual(reponses, resultat)

    def test_rotations(self):
        afficher_calculs = False
        reponses = {}
        reponse = vecteur(incert.i(3), incert.i(-2), incert.i(1))
        U0 = vecteur(incert.i(1), incert.i(2), incert.i(3))
        U1 = rotation1(incert.pi/2, U0)
        reponse1 = vecteur(incert.i(1), incert.i(3), incert.i(-2))
        self.assertTrue(egalite_vecteurs(U1, reponse1))
        U2 = rotation2(incert.pi/2, U0)
        reponse2 = vecteur(incert.i(-3), incert.i(2), incert.i(1))
        self.assertTrue(egalite_vecteurs(U2, reponse2))
        U3 = rotation3(incert.pi/2, U0)
        reponse3 = vecteur(incert.i(2), incert.i(-1), incert.i(3))
        self.assertTrue(egalite_vecteurs(U3, reponse3))

if (__name__ == "__main__"):
    unittest.main()