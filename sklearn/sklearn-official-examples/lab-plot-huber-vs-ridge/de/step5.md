# Passt den Huber-Regressor an

Wir werden nun den HuberRegressor an den Datensatz anpassen. Wir werden das Modell über einen Bereich von Epsilon-Werten anpassen, um zu zeigen, wie sich die Entscheidungsfunktion an die der Ridge-Regression annähert, wenn der Wert von Epsilon zunimmt.

```python
# Definiere den Bereich der Epsilon-Werte
epsilon_values = [1, 1.5, 1.75, 1.9]

# Definiere die x-Werte zum Plotten
x = np.linspace(X.min(), X.max(), 7)

# Definiere die Farben zum Plotten
colors = ["r-", "b-", "y-", "m-"]

# Passt den Huber-Regressor über eine Reihe von Epsilon-Werten an.
for k, epsilon in enumerate(epsilon_values):
    huber = HuberRegressor(alpha=0.0, epsilon=epsilon)
    huber.fit(X, y)
    coef_ = huber.coef_ * x + huber.intercept_
    plt.plot(x, coef_, colors[k], label="huber loss, %s" % epsilon)

# Füge eine Legende zum Plot hinzu
plt.legend(loc=0)

# Zeige den Plot an
plt.title("HuberRegressor mit unterschiedlichen Epsilon-Werten")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
