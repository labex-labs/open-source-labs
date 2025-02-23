# Crear la animación

Utilizaremos un bucle `for` para iterar a través de cada fotograma de la animación. En cada iteración, limpiaremos el eje, graficaremos el fotograma actual, estableceremos el título y pausaremos durante un corto período de tiempo para permitir que se muestre la animación.

```python
fig, ax = plt.subplots()

for i, img in enumerate(data):
    ax.clear()
    ax.imshow(img)
    ax.set_title(f"frame {i}")
    plt.pause(0.1)
```
