# Calculez les valeurs d'espérance conditionnelle individuelle pour une caractéristique spécifique

```python
x_index = 0
ice, axes = partial_dependence(model, X, features=[x_index], kind='individual')

# Tracez les valeurs d'espérance conditionnelle individuelle
for i in range(len(ice)):
    plt.plot(axes[x_index], ice[i], color='lightgray')
plt.plot(axes[x_index], np.mean(ice, axis=0), color='blue')
plt.xlabel(feature_names[x_index])
plt.ylabel("Espérance conditionnelle individuelle")
plt.title("Graphique d'espérance conditionnelle individuelle")

plt.show()
```
