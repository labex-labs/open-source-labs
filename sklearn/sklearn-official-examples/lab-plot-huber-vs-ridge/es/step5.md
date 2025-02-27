# Ajustar el regresor Huber

Ahora ajustaremos el HuberRegressor al conjunto de datos. Ajustaremos el modelo para una serie de valores de epsilon para mostrar cómo la función de decisión se aproxima a la de la regresión Ridge a medida que aumenta el valor de epsilon.

```python
# Define the range of values for epsilon
epsilon_values = [1, 1.5, 1.75, 1.9]

# Define the x values for plotting
x = np.linspace(X.min(), X.max(), 7)

# Define the colors for plotting
colors = ["r-", "b-", "y-", "m-"]

# Fit the huber regressor over a series of epsilon values.
for k, epsilon in enumerate(epsilon_values):
    huber = HuberRegressor(alpha=0.0, epsilon=epsilon)
    huber.fit(X, y)
    coef_ = huber.coef_ * x + huber.intercept_
    plt.plot(x, coef_, colors[k], label="huber loss, %s" % epsilon)

# Add a legend to the plot
plt.legend(loc=0)

# Show the plot
plt.title("HuberRegressor with Different Epsilon Values")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
