# Personnalisez le style du graphique

Nous pouvons modifier le style de notre graphique pour le rendre plus visuellement attrayant. Suivez ces étapes :

1. Affichez la liste des styles disponibles à l'aide de `print(plt.style.available)`.

```python
print(plt.style.available)
```

2. Choisissez un style et appliquez-le à l'aide de `plt.style.use(style_name)`.

```python
plt.style.use('fivethirtyeight')
```

3. Montrons à nouveau le graphique.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
```
