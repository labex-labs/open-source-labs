# Criando os Dados

Em seguida, criaremos os dados para o plot. Criaremos uma onda senoidal usando a biblioteca `numpy`.

```python
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
```
