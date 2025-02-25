# Personalizar el estilo de la gráfica

Podemos cambiar el estilo de nuestra gráfica para que sea más atractiva visualmente. Siga estos pasos:

1. Imprima la lista de estilos disponibles utilizando `print(plt.style.available)`.

```python
print(plt.style.available)
```

2. Elija un estilo y aplíquelo utilizando `plt.style.use(style_name)`.

```python
plt.style.use('fivethirtyeight')
```

3. Vamos a mostrar la gráfica nuevamente.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
```
