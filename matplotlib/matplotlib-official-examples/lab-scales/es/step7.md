# Crear un gráfico con escala de transformación de Mercator

Como bono, también crearemos un gráfico usando la función de transformación de Mercator. Esta no es una función integrada en Matplotlib, pero podemos definir nuestras propias funciones directas e inversas para crear un gráfico con escala de transformación de Mercator. En este ejemplo, definiremos las funciones `forward()` e `inverse()` para la transformación de Mercator. También agregamos un título y una cuadrícula al gráfico.

```python
# Función de transformación de Mercator
def forward(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.log(np.abs(np.tan(a) + 1.0 / np.cos(a))))

def inverse(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.arctan(np.sinh(a)))

t = np.arange(0, 170.0, 0.1)
s = t / 2.

plt.plot(t, s, '-', lw=2)
plt.yscale('function', functions=(forward, inverse))
plt.title('Mercator Transform Scale')
plt.grid(True)
plt.xlim([0, 180])
```
