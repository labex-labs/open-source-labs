# Créez le graphique

Maintenant que nous avons nos données, nous pouvons créer notre graphique. Nous commencerons par créer un objet d'axes à l'aide de `matplotlib.pyplot.subplots()`. Nous tracerons ensuite notre premier ensemble de données sur cet objet d'axes et définirons la couleur de l'étiquette en rouge.

```python
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('temps (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
```

Ensuite, nous allons instancier un second objet d'axes qui partage le même axe x que le premier objet d'axes à l'aide de la méthode `ax1.twinx()`. Nous tracerons ensuite notre second ensemble de données sur ce nouvel objet d'axes et définirons la couleur de l'étiquette en bleu.

```python
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
```

Enfin, nous ajusterons la disposition de notre graphique à l'aide de la méthode `fig.tight_layout()` et le visualiserons à l'aide de `matplotlib.pyplot.show()`.

```python
fig.tight_layout()
plt.show()
```
