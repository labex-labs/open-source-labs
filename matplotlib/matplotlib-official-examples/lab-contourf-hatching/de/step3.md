# Einfacher gekreuzter Plot mit Farbskala

In diesem Schritt werden wir den einfachsten gekreuzten Plot mit einer Farbskala erstellen. Wir werden die `contourf`-Funktion verwenden, um den gefüllten Konturlinienplot zu erstellen und die Kreuzmuster mit dem `hatches`-Parameter anzugeben.

```python
fig1, ax1 = plt.subplots()
cs = ax1.contourf(x, y, z, hatches=['-', '/', '\\', '//'],
                  cmap='gray', extend='both', alpha=0.5)
fig1.colorbar(cs)
```
