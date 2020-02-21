Help on module coord:

NAME
    coord

DESCRIPTION
    Changements de coordonnées astronomiques par calcul matriciel.
    D'après "connaissance des temps" édition 2018.

FUNCTIONS
    egalite_vecteurs(U1, U2)
        Vérifie l'égalité de deux vecteurs.
        Entrée:
            U1 et U2 deux vecteurs (matrice)
        Retour :
            boleen : True ou False
    
    rotation1(theta, U)
        Transforme les coordonnées cartésiennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Ox).
        Entrée :
            theta, angle de rotation (float)
            U vecteur = [[x]
                         [y]
                         [z]]
        Retour :
            vecteur image
    
    rotation2(theta, U)
        Transforme les coordonnées cartésiennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Oy).
        Entrée :
            theta, angle de rotation (float)
            U vecteur = [[x]
                         [y]
                         [z]]
        Retour :
            vecteur image
    
    rotation3(theta, U)
        Transforme les coordonnées cartésiennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Oz).
        Entrée :
            theta, angle de rotation (float)
            U vecteur = [[x]
                         [y]
                         [z]]
        Retour :
            vecteur image
    
    vecteur(x, y, z)
        Compose un vecteur à trois dimensions avec les valeurs données.
        Entrée :
            x, y et z
        Retour :
            Vecteur image
    
    xyzdepolaire(psi, phi, r)
        Calcul les coordonnées x, y et z à partir des coordonnées polaires
        psi, phi et r.
        Entrée :
            psi, phi et r
        Retour :
            Vecteur image

FILE
    c:\users\mc\mu_code\_mes_modules\coordonnees\coord.py


