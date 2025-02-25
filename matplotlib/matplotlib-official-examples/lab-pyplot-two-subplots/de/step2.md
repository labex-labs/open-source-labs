# Definiere die Daten

Wir werden zwei Datensätze definieren, die wir verwenden werden, um unsere Subplots zu erstellen.

```python
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
```
