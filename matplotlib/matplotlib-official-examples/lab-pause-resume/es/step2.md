# Definir la animación

En este paso, definiremos la animación que queremos crear. Crearemos una animación que muestra una distribución normal que se mueve hacia la derecha en cada fotograma.

```python
class PauseAnimation:
    def __init__(self):
        # Crear la figura y el eje
        fig, ax = plt.subplots()
        ax.set_title('Haga clic para pausar/reenudar la animación')

        # Crear los valores del eje x
        x = np.linspace(-0.1, 0.1, 1000)

        # Comenzar con una distribución normal
        self.n0 = (1.0 / ((4 * np.pi * 2e-4 * 0.1) ** 0.5)
                   * np.exp(-x ** 2 / (4 * 2e-4 * 0.1)))

        # Crear la gráfica
        self.p, = ax.plot(x, self.n0)

        # Crear la animación
        self.animation = animation.FuncAnimation(
            fig, self.update, frames=200, interval=50, blit=True)

        # Establecer la animación como no pausada
        self.paused = False

        # Agregar un evento de pulsación de botón para alternar la pausa
        fig.canvas.mpl_connect('button_press_event', self.toggle_pause)

    def toggle_pause(self, *args, **kwargs):
        # Alternar entre pausado y no pausado
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused

    def update(self, i):
        # Actualizar la distribución normal
        self.n0 += i / 100 % 5
        self.p.set_ydata(self.n0 % 20)
        return (self.p,)
```
