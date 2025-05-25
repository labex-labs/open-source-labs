# Criar Pesos de Amostra

Criaremos dois conjuntos de pesos de amostra. O primeiro conjunto de pesos de amostra será constante para todos os pontos, e o segundo conjunto de pesos de amostra será maior para alguns valores discrepantes.

```python
sample_weight_last_ten = abs(np.random.randn(len(X)))
sample_weight_constant = np.ones(len(X))
sample_weight_last_ten[15:] *= 5
sample_weight_last_ten[9] *= 15
```
