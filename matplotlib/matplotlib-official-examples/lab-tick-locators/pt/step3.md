# Definindo o Null Locator

O _null locator_ (localizador nulo) é um localizador que não coloca nenhum _tick_ (marca) no eixo. Podemos definir o _null locator_ usando `ticker.NullLocator()`.

```python
setup(axs[0], title="NullLocator()")
axs[0].xaxis.set_major_locator(ticker.NullLocator())
axs[0].xaxis.set_minor_locator(ticker.NullLocator())
```
