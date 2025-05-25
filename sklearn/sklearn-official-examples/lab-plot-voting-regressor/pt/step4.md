# Fazendo Previsões

Agora, usaremos cada um dos regressores para fazer as 20 primeiras previsões.

```python
# Fazer previsões
xt = X[:20]

pred1 = reg1.predict(xt)
pred2 = reg2.predict(xt)
pred3 = reg3.predict(xt)
pred4 = ereg.predict(xt)
```
