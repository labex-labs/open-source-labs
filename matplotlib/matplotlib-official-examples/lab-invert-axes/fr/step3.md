# Création du tracé

Maintenant, nous pouvons créer le tracé à l'aide de Matplotlib. Nous utiliserons la fonction `plot` pour tracer nos données et définir les limites de l'axe x à l'aide de la fonction `set_xlim`.

```python
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(5, 0)  # decreasing time
ax.set_xlabel('decreasing time (s)')
ax.set_ylabel('voltage (mV)')
ax.set_title('Should be growing...')
ax.grid(True)

plt.show()
```
