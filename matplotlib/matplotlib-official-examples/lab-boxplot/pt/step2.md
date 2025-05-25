# Gerar Dados

Geraremos alguns dados aleatórios para usar em nossos exemplos. Usaremos a função NumPy `random.lognormal()` para gerar dados log-normais com uma média de 1.5 e um desvio padrão de 1.75. Geraremos 37 amostras de 4 variáveis e as armazenaremos na variável `data`. Também criaremos uma lista de rótulos para cada variável.

```python
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```
