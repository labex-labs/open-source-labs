# Criar o segundo subplot

Criaremos o segundo subplot com o parâmetro `rstride` definido como `0` e o parâmetro `cstride` definido como `10`.

```python
ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")
```
