# Criando o Gráfico de Barras

Agora estamos prontos para criar nosso gráfico de barras. Começaremos definindo algumas variáveis que nos ajudarão a definir a largura das barras e suas posições no eixo x.

```python
dim = len(data[0])
w = 0.75
dimw = w / dim
```

Em seguida, criaremos uma figura e um objeto de eixo usando o método `subplots()`. Então, usaremos um loop `for` para iterar por cada valor em nosso conjunto de dados e criar uma barra para cada um.

```python
fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
    y = [d[i] for d in data]
    b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)
```

Definimos o parâmetro `bottom` como `0.001` para evitar ter barras com altura 0, o que não é compatível com uma escala logarítmica.
