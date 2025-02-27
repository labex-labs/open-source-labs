# Charger le jeu de données

Nous allons charger le jeu de données 20 newsgroups et le vectoriser. Nous utilisons quelques heuristiques pour éliminer précocement les termes inutiles : les messages sont dépouillés de leurs en-têtes, pieds de page et réponses citées, et les mots anglais courants, les mots apparaissant dans un seul document ou dans au moins 95 % des documents sont supprimés.

```python
from sklearn.datasets import fetch_20newsgroups

n_samples = 2000
n_features = 1000

print("Chargement du jeu de données...")
data, _ = fetch_20newsgroups(
    shuffle=True,
    random_state=1,
    remove=("headers", "footers", "quotes"),
    return_X_y=True,
)
data_samples = data[:n_samples]
```
