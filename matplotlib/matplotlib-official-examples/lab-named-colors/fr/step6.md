# Création d'un camembert

Nous pouvons également utiliser Matplotlib pour créer un camembert. Dans cet exemple, nous allons créer un camembert qui montre le pourcentage de personnes qui préfèrent différents types de pizza.

```python
import matplotlib.pyplot as plt

# données à tracer
sizes = [30, 40, 10, 20]
labels = ["Pepperoni", "Mushroom", "Onion", "Sausage"]

# création du camembert
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# définition du titre
plt.title("Simple Pie Chart")

# affichage du graphique
plt.show()
```
