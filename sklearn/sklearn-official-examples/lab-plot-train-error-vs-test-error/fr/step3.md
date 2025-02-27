# Tracer les fonctions des résultats

Nous allons tracer les fonctions des résultats à l'aide de la bibliothèque `matplotlib`. Nous utiliserons la fonction `plt.subplot()` pour créer deux sous-graphiques. Dans le premier sous-graphique, nous tracerons les erreurs d'entraînement et de test en fonction du paramètre de régularisation. Nous tracerons également une ligne verticale au niveau du paramètre de régularisation optimal. Dans le second sous-graphique, nous tracerons les coefficients réels et les coefficients estimés.

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
plt.xlabel("Paramètre de régularisation")
plt.ylabel("Performance")

# Afficher coef_ estimé vs coef réel
plt.subplot(2, 1, 2)
plt.plot(coef, label="Coef réel")
plt.plot(coef_, label="Coef estimé")
plt.legend()
plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.26)
plt.show()
```
