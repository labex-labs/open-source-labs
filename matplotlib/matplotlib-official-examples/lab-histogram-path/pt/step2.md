# Definir a semente aleatória e gerar dados

Usaremos numpy para gerar dados aleatórios. Para tornar nossos resultados reproduzíveis, definiremos uma semente aleatória. Adicione o seguinte código ao seu arquivo:

```python
np.random.seed(19680801)
data = np.random.randn(1000)
```
