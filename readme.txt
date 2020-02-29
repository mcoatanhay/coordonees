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
    
    parametres_precession(t)
        Calcul les paramètres de la précession à partir des coefficients
        uai 2000.
        Entrée :
            t en dizaine de siècles juliens à partir de l'époque 2000.0
                t = [(JJ) - (JJ)2000.0] / 365250
        Retour :
            z, theta, zeta, khi, omega, psi, epsilon
    
    polairedexyz(U)
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
    
    precession_uai2000_extract()
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
        Calcul les coordonnées x, y et z à partir des coordonnées polaires.
        Entrée :
            psi, phi et r
        Retour :
            Vecteur image

DATA
    precession_uai2000_coef = {'epsilon (")': ['84381.448', '-468.150', '-...
    precession_uai2000_file = 'precession_uai2000.dat'

FILE
    c:\users\mc\mu_code\_mes_modules\coordonnees\coord.py


