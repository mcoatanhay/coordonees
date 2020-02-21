Help on module coord:

NAME
    coord

DESCRIPTION
    Changements de coordonn�es astronomiques par calcul matriciel.
    D'apr�s "connaissance des temps" �dition 2018.

FUNCTIONS
    egalite_vecteurs(U1, U2)
        V�rifie l'�galit� de deux vecteurs.
        Entr�e:
            U1 et U2 deux vecteurs (matrice)
        Retour :
            boleen : True ou False
    
    rotation1(theta, U)
        Transforme les coordonn�es cart�siennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Ox).
        Entr�e :
            theta, angle de rotation (float)
            U vecteur = [[x]
                         [y]
                         [z]]
        Retour :
            vecteur image
    
    rotation2(theta, U)
        Transforme les coordonn�es cart�siennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Oy).
        Entr�e :
            theta, angle de rotation (float)
            U vecteur = [[x]
                         [y]
                         [z]]
        Retour :
            vecteur image
    
    rotation3(theta, U)
        Transforme les coordonn�es cart�siennes (x, y, z) par une rotation
        d'angle theta autour de l'axe (Oz).
        Entr�e :
            theta, angle de rotation (float)
            U vecteur = [[x]
                         [y]
                         [z]]
        Retour :
            vecteur image
    
    vecteur(x, y, z)
        Compose un vecteur � trois dimensions avec les valeurs donn�es.
        Entr�e :
            x, y et z
        Retour :
            Vecteur image
    
    xyzdepolaire(psi, phi, r)
        Calcul les coordonn�es x, y et z � partir des coordonn�es polaires
        psi, phi et r.
        Entr�e :
            psi, phi et r
        Retour :
            Vecteur image

FILE
    c:\users\mc\mu_code\_mes_modules\coordonnees\coord.py


