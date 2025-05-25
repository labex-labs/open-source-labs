# Gerar Dados

Geramos 40 pontos separáveis usando a função `random.randn` do numpy. Os primeiros 20 pontos têm uma média de [-2, -2] e os próximos 20 pontos têm uma média de [2, 2]. Em seguida, atribuímos uma etiqueta de classe 0 aos primeiros 20 pontos e uma etiqueta de classe 1 aos próximos 20 pontos.

```python
np.random.seed(0)
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
Y = [0] * 20 + [1] * 20
```
