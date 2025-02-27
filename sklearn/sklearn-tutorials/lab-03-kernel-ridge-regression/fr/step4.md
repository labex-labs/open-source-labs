# Visualiser la fonction prédite

Une fois que le modèle est entraîné, visualisons la fonction prédite ainsi que les points de données originaux.

```python
# Generate test data points
X_test = np.linspace(0, 5, 100)[:, None]

# Predict the target values
y_pred = krr.predict(X_test)

# Visualize the data and the predicted function
plt.scatter(X, y, color='blue', label='Données')
plt.plot(X_test, y_pred, color='red', label='Fonction prédite')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
