# Graficar las funciones de resultados

Graficaremos las funciones de resultados usando la librería `matplotlib`. Usaremos la función `plt.subplot()` para crear dos subgráficos. En el primer subgráfico, graficaremos los errores de entrenamiento y prueba en función del parámetro de regularización. También graficaremos una línea vertical en el parámetro de regularización óptimo. En el segundo subgráfico, graficaremos los coeficientes reales y los coeficientes estimados.

```python
import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
plt.semilogx(alphas, train_errors, label="Train")
plt.semilogx(alphas, test_errors, label="Test")
plt.vlines(
    alpha_optim,
    plt.ylim()[0],
    np.max(test_errors),
    color="k",
    linewidth=3,
    label="Optimum on test",
)
plt.legend(loc="lower right")
plt.ylim([0, 1.2])
plt.xlabel("Regularization parameter")
plt.ylabel("Performance")

# Show estimated coef_ vs true coef
plt.subplot(2, 1, 2)
plt.plot(coef, label="True coef")
plt.plot(coef_, label="Estimated coef")
plt.legend()
plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.26)
plt.show()
```
