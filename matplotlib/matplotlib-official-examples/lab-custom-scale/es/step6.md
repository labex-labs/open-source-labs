# Usar la escala personalizada

Ahora podemos usar la escala personalizada en nuestros gráficos. Aquí hay un ejemplo de cómo usar la escala personalizada para datos de latitud en una proyección de Mercator.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    t = np.arange(-180.0, 180.0, 0.1)
    s = np.radians(t)/2.

    plt.plot(t, s, '-', lw=2)
    plt.yscale('mercator')

    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.title('Proyección de Mercator')
    plt.grid(True)

    plt.show()
```
