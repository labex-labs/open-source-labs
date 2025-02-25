# Lineare und nichtlineare Arrays erstellen

Wir müssen zwei Arrays erstellen, eines mit linearen Werten und eines mit nicht-linearen Werten. Diese Arrays werden verwendet, um unser NonUniformImage zu erstellen.

```python
# Lineares x-Array für Zellzentren:
x = np.linspace(-4, 4, 9)

# Sehr nichtlineares x-Array:
x2 = x**3

y = np.linspace(-4, 4, 9)

z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
```
