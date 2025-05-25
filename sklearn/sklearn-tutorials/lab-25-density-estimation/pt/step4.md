# Avaliar as amostras

Após ajustar o estimador, podemos usar o método `score_samples` para calcular a probabilidade logarítmica das amostras sob a função de densidade estimada. Isso nos fornecerá uma medida de quão provável cada amostra é de acordo com a estimativa de densidade.

```python
scores = kde.score_samples(X)
```
