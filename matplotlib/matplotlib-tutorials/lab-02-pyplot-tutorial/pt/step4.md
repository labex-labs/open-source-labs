# Plotando com Variáveis Categóricas

Matplotlib permite criar gráficos usando variáveis categóricas. Vamos criar um gráfico de barras, um gráfico de dispersão e um gráfico de linhas com variáveis categóricas:

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()
```

Explicação:

- Criamos uma lista `names` com três valores categóricos e uma lista `values` representando seus valores correspondentes.
- A função `figure` é chamada para criar uma nova figura com um tamanho especificado.
- Usamos a função `subplot` para criar uma grade de subplots. Neste exemplo, criamos três subplots, cada um com um tipo diferente de gráfico: gráfico de barras, gráfico de dispersão e gráfico de linhas.
- A função `suptitle` é usada para definir o super-título da figura.
