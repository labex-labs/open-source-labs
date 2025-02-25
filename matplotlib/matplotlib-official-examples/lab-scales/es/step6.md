# Crear un gráfico con escala personalizada

El último tipo de transformación de escala que exploraremos es la personalizada. Esto nos permite definir nuestras propias funciones directas e inversas para la transformación de escala. En este ejemplo, definiremos una función personalizada para calcular la raíz cuadrada de los datos. Para crear un gráfico con escala personalizada, usamos el método `set_yscale()` y le pasamos la cadena `'function'`. También definimos las funciones `forward()` e `inverse()` y las pasamos como argumentos al parámetro `functions`. También agregamos un título y una cuadrícula al gráfico.

```python
# Función x**(1/2)
def forward(x):
    return x**(1/2)

def inverse(x):
    return x**2

plt.plot(x, y)
plt.yscale('function', functions=(forward, inverse))
plt.title('Custom Scale')
plt.grid(True)
```
