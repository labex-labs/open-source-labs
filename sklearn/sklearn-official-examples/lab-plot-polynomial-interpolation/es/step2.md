# Interpolación con Características Polinómicas

Usaremos `PolynomialFeatures` para generar características polinómicas y ajustar un modelo de regresión con regularización L2 a los datos de entrenamiento. Luego graficaremos la función, los puntos de entrenamiento y la interpolación utilizando características polinómicas.

```python
# graficar función
lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(
    color=["black", "teal", "yellowgreen", "gold", "darkorange", "tomato"]
)
ax.plot(x_plot, f(x_plot), linewidth=lw, label="verdadero valor")

# graficar puntos de entrenamiento
ax.scatter(x_train, y_train, label="puntos de entrenamiento")

# características polinómicas
for degree in [3, 4, 5]:
    model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot = model.predict(X_plot)
    ax.plot(x_plot, y_plot, label=f"grado {degree}")

ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```
