# Preparar os Dados

Geraremos duas ondas senoidais com diferentes frequências usando NumPy.

```python
t = np.linspace(0, 1)
y1 = 2 * np.sin(2*np.pi*t)
y2 = 4 * np.sin(2*np.pi*2*t)
```
