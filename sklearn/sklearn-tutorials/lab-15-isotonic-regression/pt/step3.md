# Ajustar o modelo de regressão isotônica

Agora, podemos ajustar o modelo de regressão isotônica aos nossos dados. Criamos uma instância da classe `IsotonicRegression` e chamamos o método `fit` com nossos dados de entrada e valores-alvo.

```python
# Ajustar o modelo de regressão isotônica
ir = IsotonicRegression()
ir.fit(X, y)
```
