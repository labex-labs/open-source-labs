# Aplicando a Função

Agora que temos as funções, podemos usá-las para criar um _heatmap_ com anotações. Criamos um novo conjunto de dados, fornecemos argumentos adicionais para `imshow`, usamos um formato inteiro nas anotações e fornecemos algumas cores. Também ocultamos os elementos diagonais (que são todos 1) usando um `matplotlib.ticker.FuncFormatter`.

```python
data = np.random.randint(2, 100, size=(7, 7))
y = [f"Book {i}" for i in range(1, 8)]
x = [f"Store {i}" for i in list("ABCDEFG")]

fig, ax = plt.subplots()
im, _ = heatmap(data, y, x, ax=ax, vmin=0, cmap="magma_r", cbarlabel="weekly sold copies")
annotate_heatmap(im, valfmt="{x:d}", size=7, threshold=20, textcolors=("red", "white"))

def func(x, pos):
    return f"{x:.2f}".replace("0.", ".").replace("1.00", "")

annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)
```
