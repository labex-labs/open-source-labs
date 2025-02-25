# Créer le graphique

Maintenant, nous pouvons créer le graphique avec l'indicateur personnalisé. Nous allons créer un graphique en barres avec des données d'échantillonnage et définir l'indicateur de l'axe des y pour utiliser notre fonction d'indicateur personnalisé.

```python
# Create a bar chart with sample data
fig, ax = plt.subplots()
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]
ax.bar(['Bill', 'Fred', 'Mary', 'Sue'], money)

# Set the y-axis ticker to use the custom ticker function
ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions))

# Display the plot
plt.show()
```
