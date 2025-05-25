# Criar Dados para Plotagem

Criaremos dados para plotar usando NumPy. Geraremos 31 pontos de dados entre -pi/2 e pi/2 e calcularemos o cosseno desses valores elevados à potência de 3.

```python
x = np.linspace(-np.pi/2, np.pi/2, 31)
y = np.cos(x)**3
```
