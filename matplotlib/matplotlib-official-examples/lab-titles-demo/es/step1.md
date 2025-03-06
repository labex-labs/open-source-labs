# Gráficos Básicos con Posición de Título Predeterminada

En este paso, crearás un gráfico de línea simple y agregarás un título centrado, que es la posición predeterminada en Matplotlib.

## Creación de un Jupyter Notebook

Después de que la máquina virtual (VM) haya terminado de iniciarse, haz clic en la esquina superior izquierda para cambiar a la pestaña **Notebook** y acceder al Jupyter Notebook.

![click-notebook](https://file.labex.io/images/click-notebook.png)

Es posible que debas esperar unos segundos para que el Jupyter Notebook termine de cargarse. Debido a las limitaciones del Jupyter Notebook, la validación de las operaciones no se puede automatizar.

Si encuentras algún problema durante el laboratorio, no dudes en pedir ayuda a Labby. Por favor, brinda comentarios después de la sesión para que podamos resolver cualquier problema de inmediato.

## Importación de Matplotlib

Ahora, comencemos importando la librería Matplotlib. En la primera celda de tu cuaderno, escribe el siguiente código y ejecútalo presionando Shift+Enter:

```python
import matplotlib.pyplot as plt
```

Esto importa el módulo `pyplot` de Matplotlib y le asigna el alias `plt`, que es una convención común.

## Creación de un Gráfico Simple

A continuación, creemos un gráfico de línea básico. En una nueva celda, escribe el siguiente código y ejecútalo:

```python
plt.figure(figsize=(8, 5))  # Create a figure with a specific size
plt.plot(range(10))         # Plot numbers from 0 to 9
plt.grid(True)              # Add a grid for better readability
plt.show()                  # Display the plot
```

Deberías ver un gráfico de línea simple con valores del 0 al 9 en la salida.

![line-plot](../assets/screenshot-20250306-g5knGobR@2x.png)

## Adición de un Título Predeterminado (Centrado)

Ahora, agreguemos un título a nuestro gráfico. La posición predeterminada para un título es centrada en la parte superior del gráfico. En una nueva celda, escribe el siguiente código:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('My First Matplotlib Plot')  # Add a centered title
plt.show()
```

![line-plot-with-title](../assets/screenshot-20250306-XMODABB2@2x.png)

Ejecuta la celda y deberías ver el gráfico con un título centrado en la parte superior.

La función `title()` sin parámetros adicionales colocará el título en el centro, que es la posición predeterminada.
