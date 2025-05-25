# Ajustando a Rede Elástica

Agora podemos prosseguir com o ajuste. Devemos passar a matriz de projeto centralizada para o método `fit` para evitar que o estimador de rede elástica detecte que ela está não-centralizada e descarte a matriz Gram que passamos. No entanto, se passarmos a matriz de projeto escalonada, o código de pré-processamento a redimensionará incorretamente uma segunda vez. Também passamos os pesos normalizados para o parâmetro `sample_weight` da função `fit`.

```python
from sklearn.linear_model import ElasticNet

lm = ElasticNet(alpha=0.01, precompute=gram)
lm.fit(X_centered, y, sample_weight=normalized_weights)
```
