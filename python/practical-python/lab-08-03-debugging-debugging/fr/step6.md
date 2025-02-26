# Exécuter sous le débogueur

Vous pouvez également exécuter un programme complet sous le débogueur.

```bash
$ python3 -m pdb someprogram.py
```

Il entrera automatiquement dans le débogueur avant la première instruction. Vous permettant de définir des points d'arrêt et de modifier la configuration.

Commandes de débogueur courantes :

```code
(Pdb) help            # Obtenir de l'aide
(Pdb) w(here)         # Afficher la trace de pile
(Pdb) d(own)          # Descendre d'un niveau de pile
(Pdb) u(p)            # Monter d'un niveau de pile
(Pdb) b(reak) loc     # Définir un point d'arrêt
(Pdb) s(tep)          # Exécuter une instruction
(Pdb) c(ontinue)      # Continuer l'exécution
(Pdb) l(ist)          # Lister le code source
(Pdb) a(rgs)          # Afficher les arguments de la fonction actuelle
(Pdb)!statement      # Exécuter une instruction
```

Pour les points d'arrêt, la localisation peut être l'une des suivantes.

```code
(Pdb) b 45            # Ligne 45 dans le fichier actuel
(Pdb) b file.py:45    # Ligne 45 dans file.py
(Pdb) b foo           # Fonction foo() dans le fichier actuel
(Pdb) b module.foo    # Fonction foo() dans un module
```
