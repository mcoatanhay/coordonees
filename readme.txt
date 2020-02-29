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
    
    parametres_precession(t)
        Calcul les param�tres de la pr�cession � partir des coefficients
        uai 2000.
        Entr�e :
            t en dizaine de si�cles juliens � partir de l'�poque 2000.0
                t = [(JJ) - (JJ)2000.0] / 365250
        Retour :
            z, theta, zeta, khi, omega, psi, epsilon
    
    polairedexyz(U)
        Calcul les coordonn�es polaires � partir des coordonn�es cart�siennes.
        Entr�e :
            U vecteur = [[x]
                         [y]
                         [z]]
        Retour :
            tuple :
                    psi dans ]-pi, pi]
                    phi dans ]-pi, pi]
                    r
    
    precession_uai2000_extract()
        Extraction des coefficients de pr�cession uai 2000.
        Retour :
            dictionnaire
                'epsilon (")'   :[liste coefs]
                'omega (")'     :[liste coefs]
                'psi (")'       :[liste coefs]
                'khi (")'       :[liste coefs]
                'theta (")'     :[liste coefs]
                'zeta (")'      :[liste coefs]
                'z (")'         :[liste coefs]
    
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
        Calcul les coordonn�es x, y et z � partir des coordonn�es polaires.
        Entr�e :
            psi, phi et r
        Retour :
            Vecteur image

DATA
    precession_uai2000_coef = {'epsilon (")': ['84381.448', '-468.150', '-...
    precession_uai2000_file = 'precession_uai2000.dat'

FILE
    c:\users\mc\mu_code\_mes_modules\coordonnees\coord.py


