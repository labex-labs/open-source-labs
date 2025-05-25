# Gerar os dados

Em seguida, geraremos alguns dados de amostra para usar em nossos boxplots. Para este tutorial, usaremos os seguintes dados:

```python
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
```
