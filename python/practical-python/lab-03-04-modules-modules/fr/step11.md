# Chemin de recherche des modules

Comme indiqué, `sys.path` contient les chemins de recherche. Vous pouvez l'ajuster manuellement si nécessaire.

```python
import sys
sys.path.append('/project/foo/pyfiles')
```

Les chemins peuvent également être ajoutés via des variables d'environnement.

```python
% env PYTHONPATH=/project/foo/pyfiles python3
Python 3.6.0 (default, Feb 3 2017, 05:53:21)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)]
>>> import sys
>>> sys.path
['','/project/foo/pyfiles',...]
```

En règle générale, il n'est pas nécessaire d'ajuster manuellement le chemin de recherche des modules. Cependant, cela peut arriver si vous essayez d'importer du code Python situé dans un emplacement inhabituel ou difficilement accessible depuis le répertoire de travail actuel.

Pour cet exercice sur les modules, il est crucial de vous assurer que vous exécutez Python dans un environnement approprié. Les modules posent souvent des problèmes aux nouveaux programmeurs liés au répertoire de travail actuel ou aux paramètres de chemin de Python. Pour ce cours, il est supposé que vous écrivez tout votre code dans le répertoire `~/project`. Pour obtenir les meilleurs résultats, vous devriez vous assurer également d'être dans ce répertoire lorsque vous lancez l'interpréteur. Sinon, vous devez vous assurer que `~/project` est ajouté à `sys.path`.
