# Créer le tracé et connecter l'écouteur d'événements de pression de touches

Nous créons un tracé simple en utilisant `np.random.rand()` pour générer des données aléatoires. Ensuite, nous configurons l'écouteur d'événements de pression de touches en utilisant `fig.canvas.mpl_connect()` et en passant le nom de l'événement pour lequel nous voulons écouter (`'key_press_event'`) et la fonction que nous voulons appeler lorsque l'événement se produit (`on_press`).

```python
fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
```
