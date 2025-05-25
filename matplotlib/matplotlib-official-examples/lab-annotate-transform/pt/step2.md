# Criar Dados

Em seguida, criaremos alguns dados para plotar. Usaremos a biblioteca `numpy` para criar uma onda senoidal.

```python
x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)
```
