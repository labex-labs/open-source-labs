# Mögliche Lösungen

Wir werden einige mögliche Lösungen für die Einschränkungen des k-Means-Clusterings diskutieren. Im folgenden Codeblock zeigen wir, wie man die richtige Anzahl von Clustern für den ersten Datensatz findet und wie man mit ungleichmäßig großen Blobs umgeht, indem man die Anzahl der zufälligen Initialisierungen erhöht.

```python
y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("Optimal Number of Clusters")
plt.show()

y_pred = KMeans(n_clusters=3, n_init=10, random_state=random_state).fit_predict(
    X_filtered
)
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("Unevenly Sized Blobs \nwith several initializations")
plt.show()
```
