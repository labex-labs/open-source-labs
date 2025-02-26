# Modèle de script

Enfin, voici un modèle de code commun pour les programmes Python exécutés en tant que scripts de ligne de commande :

```python
#!/usr/bin/env python3
#./prog.py

# Importations (bibliothèques)
import modules

# Fonctions
def spam():
  ...

def blah():
  ...

# Fonction principale
def main(argv):
    # Analyser les arguments de la ligne de commande, l'environnement, etc.
  ...

if __name__ == '__main__':
    import sys
    main(sys.argv)
```
