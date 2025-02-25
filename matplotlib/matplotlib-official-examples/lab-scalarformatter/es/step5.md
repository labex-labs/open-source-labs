# Configurar el formato de las etiquetas de los ejes

Configuraremos el formato de las etiquetas de los ejes para nuestras subgráficas. La primera subgráfica utilizará los ajustes predeterminados, la segunda subgráfica utilizará un formato elegante de expresiones matemáticas y la tercera subgráfica no utilizará la notación de desplazamiento.

```python
# Subgráfica 1 (ajustes predeterminados)
axs[0, 0].set_title("ajustes predeterminados")

# Subgráfica 2 (useMathText=True)
for ax in axs[:, 1]:
    ax.ticklabel_format(useMathText=True)
axs[0, 1].set_title("useMathText=True")

# Subgráfica 3 (useOffset=False)
for ax in axs[:, 2]:
    ax.ticklabel_format(useOffset=False)
axs[0, 2].set_title("useOffset=False")
```
