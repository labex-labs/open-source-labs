# Personalizar o estilo do gráfico

Podemos alterar o estilo do nosso gráfico para torná-lo mais visualmente atraente. Siga estes passos:

1. Imprima a lista de estilos disponíveis usando `print(plt.style.available)`.

```python
print(plt.style.available)
```

2. Escolha um estilo e aplique-o usando `plt.style.use(style_name)`.

```python
plt.style.use('fivethirtyeight')
```

3. Vamos mostrar o gráfico novamente.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
```
