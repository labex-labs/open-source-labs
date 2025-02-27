# Clustering bewerten

Um die Leistung des K-Means-Clustering-Algorithmus zu bewerten, können wir die Trägheit (Inertia)-Score berechnen. Der Trägheit-Score misst die Summe der Entfernungen zwischen jedem Datenpunkt und seinem zugewiesenen Clusterzentrum. Ein niedrigerer Trägheit-Score zeigt ein besseres Clustering an.

```python
print("Inertia Score:", kmeans.inertia_)
```
