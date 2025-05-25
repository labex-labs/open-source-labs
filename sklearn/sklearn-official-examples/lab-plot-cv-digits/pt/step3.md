# Definir os valores dos hiperparâmetros a testar

Vamos testar diferentes valores do parâmetro de regularização C, que controla o equilíbrio entre maximizar a margem e minimizar o erro de classificação. Vamos testar 10 valores espaçados logaritmicamente entre 10^-10 e 1.

```python
C_s = np.logspace(-10, 0, 10)
```
