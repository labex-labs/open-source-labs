# Graficar las distribuciones de los objetivos

Graficamos las funciones de densidad de probabilidad del objetivo antes y después de aplicar las funciones logarítmicas.

```python
f, (ax0, ax1) = plt.subplots(1, 2)

ax0.hist(y, bins=100, density=True)
ax0.set_xlim([0, 2000])
ax0.set_ylabel("Probabilidad")
ax0.set_xlabel("Objetivo")
ax0.set_title("Distribución del objetivo")

ax1.hist(y_trans, bins=100, density=True)
ax1.set_ylabel("Probabilidad")
ax1.set_xlabel("Objetivo")
ax1.set_title("Distribución del objetivo transformado")

f.suptitle("Datos sintéticos", y=1.05)
plt.tight_layout()
```
