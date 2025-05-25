# Criar Dados de Exemplo

Em seguida, criaremos dados de exemplo para nosso gráfico usando NumPy. Geraremos 100 pontos de dados entre 0 e 2π e calcularemos seus valores de seno correspondentes.

```python
x = np.linspace(0, 2 * np.pi, 100)
y = 2 * np.sin(x)
```
