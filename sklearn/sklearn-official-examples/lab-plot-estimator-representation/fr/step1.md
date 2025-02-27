# Représentation textuelle compacte

La première façon dont nous pouvons afficher des estimateurs est à travers une représentation textuelle compacte. Les estimateurs ne montreront que les paramètres qui ont été définis sur des valeurs autres que les valeurs par défaut lorsqu'ils sont affichés sous forme de chaîne de caractères. Cela réduit le bruit visuel et facilite la détection des différences lors de la comparaison d'instances.

```python
from sklearn.linear_model import LogisticRegression

# Créez une instance de Régression logistique avec une pénalité l1
lr = LogisticRegression(penalty="l1")

# Affichez l'estimateur
print(lr)
```
