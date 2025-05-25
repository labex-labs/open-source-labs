# Gerar os dados do histograma

Agora que temos nossos dados aleatórios, podemos gerar um histograma usando numpy. Usaremos 50 bins para criar nosso histograma. Adicione o seguinte código:

```python
n, bins = np.histogram(data, 50)
```
