# Festlegen der Tick-Labels

Standardmäßig werden Tick-Labels bei negativen Werten mit einem Unicode-Minuszeichen und nicht mit einem ASCII-Hyphen gerendert. Wir können jedoch dieses Verhalten ändern, indem wir `axes.unicode_minus` auf `False` setzen.

```python
plt.rcParams['axes.unicode_minus'] = False
```
