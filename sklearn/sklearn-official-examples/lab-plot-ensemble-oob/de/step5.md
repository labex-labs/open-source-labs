# Visualisieren der OOB-Fehlerrate

Schließlich werden wir die OOB-Fehlerrate für jeden Klassifizierer als Funktion der Anzahl der Schätzer plotten. Dies wird uns ermöglichen, die Anzahl der Schätzer zu identifizieren, bei der die Fehlerrate stabilisiert. Wir werden Matplotlib verwenden, um das Diagramm zu generieren.

```python
for label, clf_err in error_rate.items():
    xs, ys = zip(*clf_err)
    plt.plot(xs, ys, label=label)

plt.xlim(min_estimators, max_estimators)
plt.xlabel("n_estimators")
plt.ylabel("OOB error rate")
plt.legend(loc="upper right")
plt.show()
```
