# Créez les fonctions de rappel pour les boutons

Maintenant, nous allons créer deux fonctions de rappel pour les boutons `Next` et `Previous`. Ces fonctions mettront à jour la trame avec une nouvelle onde sinusoïdale ayant une fréquence différente.

```python
class Index:
    ind = 0

    def next(self, event):
        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

callback = Index()
```
