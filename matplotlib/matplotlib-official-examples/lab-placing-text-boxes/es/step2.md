# Creación de un histograma básico

Ahora que tenemos nuestros datos, creemos un histograma para visualizar su distribución. Un histograma divide los datos en intervalos (rangos) y muestra la frecuencia de los puntos de datos dentro de cada intervalo.

## Creación del histograma

En una nueva celda de su Jupyter Notebook, ingrese y ejecute el siguiente código:

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()
```

Cuando ejecute esta celda, debería ver un histograma que muestra la distribución de sus datos aleatorios. La salida se parecerá a una curva en forma de campana (distribución normal) centrada cerca de cero.

## Comprensión del código

Analicemos lo que hace cada línea del código:

1. `fig, ax = plt.subplots(figsize=(10, 6))`: Crea un objeto figura y ejes. El parámetro `figsize` establece el tamaño del gráfico en pulgadas (ancho, alto).

2. `histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')`: Crea un histograma de nuestros datos `x` con 50 intervalos. Los intervalos están coloreados de azul cielo con bordes negros.

3. `ax.set_title('Distribution of Random Data', fontsize=16)`: Agrega un título al gráfico con un tamaño de fuente de 16.

4. `ax.set_xlabel('Value', fontsize=12)` y `ax.set_ylabel('Frequency', fontsize=12)`: Agrega etiquetas a los ejes x e y con un tamaño de fuente de 12.

5. `plt.tight_layout()`: Ajusta automáticamente el gráfico para que se ajuste al área de la figura.

6. `plt.show()`: Muestra el gráfico.

El histograma muestra cómo se distribuyen nuestros datos. Dado que usamos `np.random.randn()`, que genera datos de una distribución normal, el histograma tiene forma de campana centrada en 0. La altura de cada barra representa cuántos puntos de datos caen dentro de ese rango.
