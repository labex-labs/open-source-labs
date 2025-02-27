# Parameter definieren

Wir werden die Parameter für unseren Gradient Boosting Classifier definieren. Wir werden die folgenden Parameter verwenden:

- n_estimators: Anzahl der Boosting-Stufen, die ausgeführt werden sollen
- max_leaf_nodes: maximale Anzahl von Blättern in jedem Baum
- max_depth: maximale Tiefe des Baumes
- random_state: Zufallszahl für Konsistenz
- min_samples_split: minimale Anzahl von Proben, die erforderlich sind, um einen internen Knoten aufzuteilen

```python
original_params = {
    "n_estimators": 400,
    "max_leaf_nodes": 4,
    "max_depth": None,
    "random_state": 2,
    "min_samples_split": 5,
}
```
