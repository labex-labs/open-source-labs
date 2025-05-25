# Desenhar o Círculo e o Ponto Inicial

O terceiro passo é desenhar o círculo e o ponto inicial no subplot da esquerda. Criamos um array de ângulos para gerar o círculo e, em seguida, plotamos o seno e o cosseno de cada ângulo. Também plotamos um único ponto na origem.

```python
x = np.linspace(0, 2 * np.pi, 50)
axl.plot(np.cos(x), np.sin(x), "k", lw=0.3)
point, = axl.plot(0, 0, "o")
```
