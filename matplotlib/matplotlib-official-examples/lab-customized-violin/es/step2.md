# Crear un diagrama de violín predeterminado

A continuación, crearemos un diagrama de violín predeterminado utilizando la función `violinplot` de Matplotlib. Esto proporcionará una línea base para la comparación cuando personalicemos el gráfico en pasos posteriores.

```python
# create default violin plot
fig, ax1 = plt.subplots()
ax1.set_title('Default Violin Plot')
ax1.set_ylabel('Observed Values')
ax1.violinplot(data)
```
