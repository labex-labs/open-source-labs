# Gerar dados

Geraremos alguns dados de teste aleatórios usando numpy.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]
```
