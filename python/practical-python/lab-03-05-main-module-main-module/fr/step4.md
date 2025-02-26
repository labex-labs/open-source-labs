# Programmes principaux vs. importations de bibliothèques

N'importe quel fichier Python peut être exécuté en tant que principal ou en tant qu'importation de bibliothèque :

```bash
$ python3 prog.py # Exécuté en tant que principal
```

```python
import prog   # Exécuté en tant qu'importation de bibliothèque
```

Dans les deux cas, `__name__` est le nom du module. Cependant, il ne sera défini sur `__main__` que si le programme est exécuté en tant que principal.

Généralement, vous ne voulez pas que les instructions qui font partie du programme principal s'exécutent lors d'une importation de bibliothèque. Par conséquent, il est courant d'avoir une vérification `if` dans le code qui peut être utilisé de l'un ou l'autre manière.

```python
if __name__ == '__main__':
    # N'est pas exécuté si chargé avec import...
```
