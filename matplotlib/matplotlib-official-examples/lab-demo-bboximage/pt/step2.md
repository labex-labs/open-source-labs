# Criar um BboxImage com Texto

Começamos criando um BboxImage com texto. Criamos um objeto `text` com o método `text()` e o adicionamos ao objeto `ax1`. Em seguida, criamos um objeto `BboxImage` usando o método `add_artist()`. Passamos o método `get_window_extent` do objeto `text` para o construtor `BboxImage` para obter a caixa delimitadora (bounding box) para o texto. Também passamos um array 1D de forma (1, 256) para o parâmetro `data` do construtor `BboxImage` para criar uma imagem.

```python
fig, (ax1, ax2) = plt.subplots(ncols=2)

txt = ax1.text(0.5, 0.5, "test", size=30, ha="center", color="w")
ax1.add_artist(
    BboxImage(txt.get_window_extent, data=np.arange(256).reshape((1, -1))))
```
