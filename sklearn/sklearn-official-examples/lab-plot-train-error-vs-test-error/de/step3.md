# Ergebnissefunktionen plotten

Wir werden die Ergebnissefunktionen mit der Bibliothek `matplotlib` plotten. Wir werden die Funktion `plt.subplot()` verwenden, um zwei Teilplots zu erstellen. Im ersten Teilplot werden wir die Trainings- und Testfehler als Funktion des Regularisierungsparameters plotten. Wir werden auch eine vertikale Linie bei dem optimalen Regularisierungsparameter plotten. Im zweiten Teilplot werden wir die wahren Koeffizienten und die geschätzten Koeffizienten plotten.

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
plt.xlabel("Regularisierungsparameter")
plt.ylabel("Leistung")

# Zeige geschätzten coef_ vs wahren coef
plt.subplot(2, 1, 2)
plt.plot(coef, label="Wahrer coef")
plt.plot(coef_, label="Geschätzter coef")
plt.legend()
plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.26)
plt.show()
```
