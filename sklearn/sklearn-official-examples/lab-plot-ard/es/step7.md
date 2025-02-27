# Graficando regresiones polinómicas con errores estándar de las puntuaciones

Las barras de error representan una desviación estándar de la distribución gaussiana predicha de los puntos de consulta. Observe que la regresión ARD captura la verdadera situación de mejor manera al usar los parámetros predeterminados en ambos modelos, pero reducir aún más el hiperparámetro `lambda_init` de Bayesian Ridge puede reducir su sesgo. Finalmente, debido a las limitaciones intrínsecas de una regresión polinómica, ambos modelos fallan al extrapolar.

```python
ax = sns.scatterplot(
    data=full_data, x="característica de entrada", y="variable objetivo", color="black", alpha=0.75
)
ax.plot(X_plot, y_plot, color="black", label="Verdadera situación")
ax.plot(X_plot, y_brr, color="red", label="BayesianRidge con características polinómicas")
ax.plot(X_plot, y_ard, color="navy", label="ARD con características polinómicas")
ax.fill_between(
    X_plot.ravel(),
    y_ard - y_ard_std,
    y_ard + y_ard_std,
    color="navy",
    alpha=0.3,
)
ax.fill_between(
    X_plot.ravel(),
    y_brr - y_brr_std,
    y_brr + y_brr_std,
    color="red",
    alpha=0.3,
)
ax.legend()
_ = ax.set_title("Ajuste polinómico de una característica no lineal")
```
