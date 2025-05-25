# Criar o primeiro subplot

Criaremos o primeiro subplot com o parâmetro `rstride` definido como `10` e o parâmetro `cstride` definido como `0`.

```python
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")
```
