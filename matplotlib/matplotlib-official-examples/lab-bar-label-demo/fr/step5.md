# Étiquetage des barres en utilisant une chaîne de formatage au style `{}`

Dans cette étape, nous allons montrer comment utiliser une chaîne de formatage au style `{}` pour formater les étiquettes des barres. Nous utiliserons certaines données sur les ventes de glace par saveur.

```python
fruit_names = ['Coffee', 'Salted Caramel', 'Pistachio']
fruit_counts = [4000, 2000, 7000]

fig, ax = plt.subplots()
bar_container = ax.bar(fruit_names, fruit_counts)
ax.set(ylabel='pints sold', title='Gelato sales by flavor', ylim=(0, 8000))
ax.bar_label(bar_container, fmt='{:,.0f}')
```
