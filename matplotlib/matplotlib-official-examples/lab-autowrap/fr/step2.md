# Création d'un graphique de base

Commençons par créer un graphique de base avec un élément de texte. Dans votre script Python, ajoutez le code suivant :

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 5, "Hello, Matplotlib!", ha='center')
plt.show()
```
