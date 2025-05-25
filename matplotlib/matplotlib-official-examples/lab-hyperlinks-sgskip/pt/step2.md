# Criar um Gráfico de Dispersão com Hiperlinks

Nesta etapa, criaremos um gráfico de dispersão e adicionaremos hiperlinks aos marcadores. Aqui está o código para criar o gráfico de dispersão:

```python
fig = plt.figure()
s = plt.scatter([1, 2, 3], [4, 5, 6])
```

Para adicionar hiperlinks, precisamos usar o método `set_urls()` do objeto do gráfico de dispersão. Este método recebe uma lista de URLs como seu argumento. Aqui está o código atualizado:

```python
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])
```

Os dois primeiros marcadores terão hiperlinks para `https://www.bbc.com/news` e `https://www.google.com/`, respectivamente. O terceiro marcador não terá um hiperlink. Finalmente, podemos salvar o gráfico como um arquivo SVG usando `fig.savefig()`:

```python
fig.savefig('scatter.svg')
```
