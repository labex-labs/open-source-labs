# Posicionamiento de Títulos a la Izquierda y a la Derecha

Matplotlib te permite posicionar el título a la izquierda o a la derecha del gráfico utilizando el parámetro `loc`. En este paso, aprenderás cómo alinear los títulos a la izquierda y a la derecha de tus gráficos.

## Creación de un Gráfico con un Título Alineado a la Izquierda

Vamos a crear un gráfico con el título posicionado en el lado izquierdo. En una nueva celda, escribe el siguiente código:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Left-Aligned Title', loc='left')  # Position the title at the left
plt.show()
```

![left-aligned-title](../assets/screenshot-20250306-9pLPZz36@2x.png)

Ejecuta la celda. Observa cómo el título ahora aparece alineado con el borde izquierdo del gráfico, en lugar de estar centrado.

El parámetro `loc` en la función `title()` determina la posición horizontal del título. Al establecer `loc='left'`, le estás indicando a Matplotlib que posicione el título en el lado izquierdo del gráfico.

## Creación de un Gráfico con un Título Alineado a la Derecha

Ahora, vamos a crear otro gráfico con el título posicionado en el lado derecho. En una nueva celda, escribe el siguiente código:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Right-Aligned Title', loc='right')  # Position the title at the right
plt.show()
```

![right-aligned-title](../assets/screenshot-20250306-PpNxbjp2@2x.png)

Ejecuta la celda. El título ahora debería aparecer alineado con el borde derecho del gráfico.

## Comparación de Diferentes Posiciones de Títulos

Vamos a crear una secuencia de tres gráficos para comparar las diferentes posiciones de los títulos (centro, izquierda y derecha). En una nueva celda, escribe el siguiente código:

```python
# Create a figure with 3 subplots arranged horizontally
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Center-aligned title (default)
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Center Title')

# Plot 2: Left-aligned title
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Left Title', loc='left')

# Plot 3: Right-aligned title
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Right Title', loc='right')

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
```

![three-title-positions](../assets/screenshot-20250306-EzNR2plC@2x.png)

Ejecuta la celda para ver las tres posiciones de los títulos una al lado de la otra. Esta comparación visual te ayuda a entender cómo el parámetro `loc` afecta el posicionamiento del título.

Ten en cuenta que cuando trabajas con subgráficos, usamos el método `set_title()` en los objetos de eje individuales en lugar de la función global `plt.title()`.
