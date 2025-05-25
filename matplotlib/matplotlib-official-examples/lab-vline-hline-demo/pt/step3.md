# Adicionar Ruído aos Dados

Nesta etapa, adicionaremos um pouco de ruído aos dados para torná-los mais realistas. Usaremos a função `normal` do NumPy para gerar números aleatórios com uma média de 0.0 e um desvio padrão de 0.3.

```python
# Add noise to the data
nse = np.random.normal(0.0, 0.3, t.shape) * s
```
