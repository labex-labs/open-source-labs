# Criar as subfiguras e chamar a função `test_rotation_mode`

Criaremos duas subfiguras e chamaremos a função `test_rotation_mode` com os parâmetros `fig` e `mode`.

```python
fig = plt.figure(figsize=(8, 5))
subfigs = fig.subfigures(1, 2)
test_rotation_mode(subfigs[0], "default")
test_rotation_mode(subfigs[1], "anchor")
plt.show()
```
