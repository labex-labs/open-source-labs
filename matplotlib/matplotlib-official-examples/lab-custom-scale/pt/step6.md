# Usar a escala personalizada

Agora podemos usar a escala personalizada em nossos gráficos. Aqui está um exemplo de como usar a escala personalizada para dados de latitude em uma projeção de Mercator.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    t = np.arange(-180.0, 180.0, 0.1)
    s = np.radians(t)/2.

    plt.plot(t, s, '-', lw=2)
    plt.yscale('mercator')

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Mercator projection')
    plt.grid(True)

    plt.show()
```
