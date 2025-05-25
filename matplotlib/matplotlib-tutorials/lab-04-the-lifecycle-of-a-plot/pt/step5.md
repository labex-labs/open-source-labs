# Personalizar a aparência do gráfico

Podemos personalizar ainda mais a aparência do nosso gráfico. Siga estes passos:

1. Rotacione os rótulos do eixo x para torná-los mais legíveis.

```python
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

2. Defina os limites, rótulos e título dos eixos x e y.

```python
ax.set(xlim=[-10000, 140000],
       xlabel='Total Revenue',
       ylabel='Company',
       title='Company Revenue')
```

3. Mostre o gráfico novamente.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
```
