# Definir la clase UpdateDist

A continuación, definimos una clase llamada `UpdateDist` que se utilizará para actualizar la distribución beta a medida que se observan nuevos datos. La clase `UpdateDist` toma dos argumentos: el objeto de eje de Matplotlib y la probabilidad inicial de éxito.

```python
class UpdateDist:
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # Establecer los parámetros del gráfico
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 10)
        self.ax.grid(True)

        # Esta línea vertical representa el valor teórico, al
        # cual debe converger la distribución trazada.
        self.ax.axvline(prob, linestyle='--', color='black')
```

El método `__init__` inicializa la instancia de la clase estableciendo el número inicial de éxitos en cero (`self.success = 0`) y la probabilidad inicial de éxito al valor pasado como argumento (`self.prob = prob`). También creamos un objeto de línea para representar la distribución beta y configuramos los parámetros del gráfico.

El método `__call__` se llama cada vez que se actualiza la animación. Simula un experimento de lanzamiento de moneda y actualiza la distribución beta en consecuencia.

```python
def __call__(self, i):
        # De esta manera, el gráfico puede ejecutarse continuamente y solo
        # seguimos viendo nuevas realizaciones del proceso
        if i == 0:
            self.success = 0
            self.line.set_data([], [])
            return self.line,

        # Elegir éxito si se supera un umbral con una selección uniforme
        if np.random.rand() < self.prob:
            self.success += 1
        y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,
```

Si este es el primer fotograma de la animación (`if i == 0`), reiniciamos el número de éxitos a cero y eliminamos el objeto de línea. De lo contrario, simulamos un experimento de lanzamiento de moneda generando un número aleatorio entre 0 y 1 (`np.random.rand()`) y comparándolo con la probabilidad de éxito (`self.prob`). Si el número aleatorio es menor que la probabilidad de éxito, lo contamos como un éxito y actualizamos la distribución beta utilizando la función `beta_pdf`. Finalmente, actualizamos el objeto de línea con los nuevos datos y lo devolvemos.
