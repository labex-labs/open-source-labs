# Desenhar a Curva Senoidal

O quarto passo é desenhar a curva senoidal no subplot da direita. Criamos um array de ângulos e, em seguida, plotamos o seno de cada ângulo. Também salvamos o objeto de plotagem `sine`, que atualizaremos mais tarde na animação.

```python
sine, = axr.plot(x, np.sin(x))
```
