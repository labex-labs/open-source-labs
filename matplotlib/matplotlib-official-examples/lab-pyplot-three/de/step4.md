# Beschriftungen und Titel hinzufügen

In diesem Schritt werden wir einem Diagramm einen Titel hinzufügen und die x- und y-Achsen beschriften.

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.title("Multiple Datasets")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.show()
```
