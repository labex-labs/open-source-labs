# Trainingseabweichung darstellen

Schließlich werden wir die Ergebnisse visualisieren. Dazu berechnen wir zunächst die Testset-Abweichung und plotten sie dann gegen die Boosting-Iterationen.

```python
test_score = np.zeros((params["n_estimators"],), dtype=np.float64)
for i, y_pred in enumerate(reg.staged_predict(X_test)):
    test_score[i] = mean_squared_error(y_test, y_pred)

fig = plt.figure(figsize=(6, 6))
plt.subplot(1, 1, 1)
plt.title("Abweichung")
plt.plot(
    np.arange(params["n_estimators"]) + 1,
    reg.train_score_,
    "b-",
    label="Trainingsset-Abweichung",
)
plt.plot(
    np.arange(params["n_estimators"]) + 1, test_score, "r-", label="Testset-Abweichung"
)
plt.legend(loc="upper right")
plt.xlabel("Boosting-Iterationen")
plt.ylabel("Abweichung")
fig.tight_layout()
plt.show()
```
