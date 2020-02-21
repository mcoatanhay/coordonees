#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: readme_coordonnees_compose.py
# Auteur: Marc COATANHAY

"""
    Module pour écrire un fichier d'aide du module.
"""

# Import des modules
import mes_modules_path
from repertoire import filerep
import coord
import sys

# Définitions constantes et variables globales
filerep()
file = open('readme.md', 'w')
sys.stdout = file
help(coord)
file.close()
sys.stdout = sys.__stdout__

# Définitions fonctions et classes

