# Die Animation definieren

In diesem Schritt definieren wir die Animation, die wir erstellen möchten. Wir werden eine Animation erstellen, die eine Normalverteilung zeigt, die sich in jedem Frame nach rechts bewegt.

```python
class PauseAnimation:
    def __init__(self):
        # Erzeuge die Figur und die Achse
        fig, ax = plt.subplots()
        ax.set_title('Klicken, um die Animation zu pausieren/fortzusetzen')

        # Erzeuge die x-Achsenwerte
        x = np.linspace(-0.1, 0.1, 1000)

        # Beginne mit einer Normalverteilung
        self.n0 = (1.0 / ((4 * np.pi * 2e-4 * 0.1) ** 0.5)
                   * np.exp(-x ** 2 / (4 * 2e-4 * 0.1)))

        # Erzeuge die Darstellung
        self.p, = ax.plot(x, self.n0)

        # Erzeuge die Animation
        self.animation = animation.FuncAnimation(
            fig, self.update, frames=200, interval=50, blit=True)

        # Setze die Animation als nicht pausiert
        self.paused = False

        # Füge ein Ereignis für das Betätigen des Buttons hinzu, um die Pause umzuschalten
        fig.canvas.mpl_connect('button_press_event', self.toggle_pause)

    def toggle_pause(self, *args, **kwargs):
        # Schalte zwischen pausiert und nicht pausiert
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused

    def update(self, i):
        # Aktualisiere die Normalverteilung
        self.n0 += i / 100 % 5
        self.p.set_ydata(self.n0 % 20)
        return (self.p,)
```
