# Outils de test tiers

Le module `unittest` intégré a l'avantage d'être disponible partout - c'est une partie de Python. Cependant, de nombreux programmeurs le trouvent également assez verbeux. Une alternative populaire est [pytest](https://docs.pytest.org/en/latest/). Avec pytest, votre fichier de test se simplifie comme suit :

```python
# test_simple.py
import simple

def test_simple():
    assert simple.add(2,2) == 4

def test_str():
    assert simple.add('hello','world') == 'helloworld'
```

Pour exécuter un test, il suffit de taper une commande comme `python -m pytest`. Il trouvera et exécutera ensuite tous les tests. Le module peut être installé à l'aide de `pip install pytest`.

Il y a bien plus à `pytest` que cet exemple, mais il est généralement assez facile de commencer si vous décidez d'essayer.

Dans cet exercice, vous explorerez les mécanismes de base de l'utilisation du module `unittest` de Python.

Dans les exercices précédents, vous avez écrit un fichier `stock.py` qui contenait une classe `Stock`. Pour cet exercice, on suppose que vous utilisez le code écrit pour l'Exercice 7.9 relatif aux propriétés typées. Si, pour une raison quelconque, cela ne fonctionne pas, vous pouvez vouloir copier la solution de `Solutions/7_9` dans votre répertoire de travail.
