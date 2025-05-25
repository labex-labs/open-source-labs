# Criando Dados

Em seguida, criaremos alguns dados para nossos gráficos. Neste exemplo, criaremos três ondas senoidais com diferentes frequências.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(3*np.pi*t)
s3 = np.sin(4*np.pi*t)
```
