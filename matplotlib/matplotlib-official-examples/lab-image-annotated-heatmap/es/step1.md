# Mapa de calor categórico simple

Comenzaremos definiendo algunos datos. Necesitamos una lista o matriz bidimensional que defina los datos para codificar por colores. Luego también necesitamos dos listas o matrices de categorías. El mapa de calor en sí es una gráfica `imshow` con las etiquetas establecidas en las categorías. Usaremos la función `text` para etiquetar los datos mismos creando un `Text` dentro de cada celda que muestre el valor de esa celda.

```python
import matplotlib.pyplot as plt
import numpy as np

vegetales = ["pepino", "tomate", "lechuga", "espárrago", "patata", "trigo", "cebada"]
granjeros = ["Granjero Joe", "Upland Bros.", "Smith Gardening", "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

cosecha = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

fig, ax = plt.subplots()
im = ax.imshow(cosecha)

# Muestra todas las marcas de división y las etiqueta con las respectivas entradas de la lista
ax.set_xticks(np.arange(len(granjeros)), labels=granjeros)
ax.set_yticks(np.arange(len(vegetales)), labels=vegetales)

# Rota las etiquetas de las marcas de división y establece su alineación
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Itera sobre las dimensiones de los datos y crea anotaciones de texto
for i in range(len(vegetales)):
    for j in range(len(granjeros)):
        text = ax.text(j, i, cosecha[i, j], ha="center", va="center", color="w")

ax.set_title("Cosecha de los granjeros locales (en toneladas/anio)")
fig.tight_layout()
plt.show()
```
