# Tests en ligne

Les assertions peuvent également être utilisées pour effectuer des tests simples.

```python
def add(x, y):
    return x + y

assert add(2,2) == 4
```

De cette manière, vous incluez le test dans le même module que votre code.

_Avantage : Si le code est manifestement cassé, les tentatives d'importer le module provoqueront une erreur._

Cela n'est pas recommandé pour les tests exhaustifs. C'est plutôt un "test de fumée" de base. La fonction fonctionne-t-elle avec n'importe quel exemple? Si ce n'est pas le cas, alors quelque chose est certainement cassé.
