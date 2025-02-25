# Personalizar la apariencia de la gráfica

Podemos personalizar aún más la apariencia de nuestra gráfica. Siga estos pasos:

1. Gire las etiquetas del eje x para que sean más legibles.

```python
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

2. Establezca los límites, etiquetas y título del eje x y del eje y.

```python
ax.set(xlim=[-10000, 140000],
       xlabel='Total Revenue',
       ylabel='Company',
       title='Company Revenue')
```

3. Muestre la gráfica nuevamente.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
```
