# Définir l'animation

Dans cette étape, nous allons définir l'animation que nous souhaitons créer. Nous allons créer une animation qui affiche une distribution normale qui se déplace vers la droite à chaque image.

```python
class PauseAnimation:
    def __init__(self):
        # Créer la figure et l'axe
        fig, ax = plt.subplots()
        ax.set_title('Cliquez pour mettre en pause / reprendre l\'animation')

        # Créer les valeurs de l'axe x
        x = np.linspace(-0.1, 0.1, 1000)

        # Commencer avec une distribution normale
        self.n0 = (1.0 / ((4 * np.pi * 2e-4 * 0.1) ** 0.5)
                   * np.exp(-x ** 2 / (4 * 2e-4 * 0.1)))

        # Créer le tracé
        self.p, = ax.plot(x, self.n0)

        # Créer l'animation
        self.animation = animation.FuncAnimation(
            fig, self.update, frames=200, interval=50, blit=True)

        # Définir l'animation comme non mise en pause
        self.paused = False

        # Ajouter un événement de pression de bouton pour basculer la pause
        fig.canvas.mpl_connect('button_press_event', self.toggle_pause)

    def toggle_pause(self, *args, **kwargs):
        # Basculer entre mis en pause et non mis en pause
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused

    def update(self, i):
        # Mettre à jour la distribution normale
        self.n0 += i / 100 % 5
        self.p.set_ydata(self.n0 % 20)
        return (self.p,)
```
