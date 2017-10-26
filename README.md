Client de consultation (exemple) des flux ATOM Ameli
====================================================

Ce projet fournit un exemple de consultation des flux ATOM XML 
d'informations sur les référentiels améli : CCAM, UCD, LPP

Il permet de déterminer les fichiers à traiter lorsqu'une nouvelle version est disponible.

En positionnement une date ou une version, le programme liste toutes les versions 
postérieures et les fichiers à télécharger.

# Utilisation
    python3 client.py -h
    usage: client.py [-h] [-u URL] [--date DATE] [--version VERSION]

    optional arguments:
      -h, --help         show this help message and exit
      -u URL, --url URL  URL du flux ATOM
      --date DATE        Date à comparer. Format YYYY-MM-DD
      --version VERSION  Version à comparer
      
# Consultation des flux
Les flux consultés sont :
- [https://www.opikanoba.org/feeds/ameli_ccam.xml](https://www.opikanoba.org/feeds/ameli_ccam.xml)
- [https://www.opikanoba.org/feeds/ameli_lpp.xml](https://www.opikanoba.org/feeds/ameli_lpp.xml)
- [https://www.opikanoba.org/feeds/ameli_ucd.xml](https://www.opikanoba.org/feeds/ameli_ucd.xml)

Ces fichiers sont produits par le projet [ref-ameli](https://github.com/flrt/ref-ameli)

# Exemples
La version actuelle de la version de la 466.
Si l'on consulte les versions disponibles après le version 470, il ne doit pas y en avoir.

    # python3 client.py -u https://www.opikanoba.org/feeds/ameli_lpp.xml --version 470
    Last updated (feed) : 2017-10-25 14:39:29

    Nombre d'entrées avec une version supérieure à 470 : 0

Par contre, si on consulte les versions disponibles après la version 460 :

    # python3 client.py -u https://www.opikanoba.org/feeds/ameli_lpp.xml --version 460
    Last updated (feed) : 2017-10-25 14:39:29
    
    Nombre d'entrées avec une version supérieure à 460 : 7
      Version : 467 du 25/10/2017
      ===========================
      Liens à télécharger
        http://www.codage.ext.cnamts.fr/f_mediam/fo/tips/LPP467.zip
    
      Version : 466 du 25/10/2017
      ===========================
      Liens à télécharger
        http://www.codage.ext.cnamts.fr/f_mediam/fo/tips/LPP466.zip
    
      Version : 465 du 11/10/2017
      ===========================
      Liens à télécharger
        http://www.codage.ext.cnamts.fr/f_mediam/fo/tips/LPP465.zip
    
      Version : 464 du 29/09/2017
      ===========================
      Liens à télécharger
        http://www.codage.ext.cnamts.fr/f_mediam/fo/tips/LPP464.zip
    
      Version : 463 du 15/09/2017
      ===========================
      Liens à télécharger
        http://www.codage.ext.cnamts.fr/f_mediam/fo/tips/LPP463.zip
    
      Version : 462 du 08/09/2017
      ===========================
      Liens à télécharger
        http://www.codage.ext.cnamts.fr/f_mediam/fo/tips/LPP462.zip
    
      Version : 461 du 17/08/2017
      ===========================
      Liens à télécharger
        http://www.codage.ext.cnamts.fr/f_mediam/fo/tips/LPP461.zip

En utilisant la date, il est possible de savoir les versions à traiter qui ont 
été publiées postérieurement au 20/10/2017 :

    # python3 client.py -u https://www.opikanoba.org/feeds/ameli_ucd.xml --date 2017-10-20
    Last updated (feed) : 2017-10-26 08:58:46
    
    Nombre d'entrées avec une date supérieure à 2017-10-20 : 2
      Version : 382 du 26/10/2017
      ===========================
      Liens à télécharger
        http://www.codage.ext.cnamts.fr/f_mediam/fo/bdm_it/ucd_total_00382_20171025.dbf
        http://www.codage.ext.cnamts.fr/f_mediam/fo/bdm_it/ucd_histo_prix_00382_20171025.dbf
        http://www.codage.ext.cnamts.fr/f_mediam/fo/bdm_it/retro_histo_taux_00382_20171025.dbf
        http://www.codage.ext.cnamts.fr/f_mediam/fo/bdm_it/retro_histo_cout_sup_00382_20171025.dbf
    
      Version : 381 du 24/10/2017
      ===========================
      Liens à télécharger
        http://www.codage.ext.cnamts.fr/f_mediam/fo/bdm_it/ucd_total_00381_20171018.dbf
        http://www.codage.ext.cnamts.fr/f_mediam/fo/bdm_it/ucd_histo_prix_00381_20171018.dbf
        http://www.codage.ext.cnamts.fr/f_mediam/fo/bdm_it/retro_histo_taux_00381_20171018.dbf
        http://www.codage.ext.cnamts.fr/f_mediam/fo/bdm_it/retro_histo_cout_sup_00381_20171018.dbf

# Licence 

[MIT](LICENSE) pour le code