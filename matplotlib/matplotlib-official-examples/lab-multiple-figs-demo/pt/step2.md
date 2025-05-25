# Criar dados

Em seguida, precisamos criar alguns dados para plotar. Criaremos duas ondas senoidais que plotaremos em figuras separadas.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)
```
