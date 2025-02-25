# Anpassen des Boxplots

Wir können den Boxplot anpassen, indem wir das Aussehen der Box, der Schnurrbögen und der Ausreißer verändern. Wir können auch mehrere Boxplots auf dem gleichen Diagramm erstellen, um verschiedene Datengruppen zu vergleichen. Hier sind einige Beispiele dafür, wie man den Boxplot anpasst:

```python
# Erstellen eines gekerbten Boxplots
plt.boxplot(data, notch=True)
plt.show()

# Ändern der Ausreißer-Punkt-Symbole in grüne Diamanten
plt.boxplot(data, flierprops=dict(marker='D', markerfacecolor='g', markersize=8))
plt.show()

# Erstellen horizontaler Boxplots
plt.boxplot(data, vert=False)
plt.show()

# Erstellen mehrerer Boxplots auf einem Diagramm
data1 = np.random.normal(0, 1, 50)
data2 = np.random.normal(1, 1, 50)
data3 = np.random.normal(2, 1, 50)

plt.boxplot([data1, data2, data3])
plt.show()
```
