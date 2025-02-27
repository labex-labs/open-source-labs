# Kompakte Textrepräsentation

Die erste Möglichkeit, Schätzer anzuzeigen, besteht darin, eine kompakte Textrepräsentation zu verwenden. Wenn Schätzer als Zeichenfolge dargestellt werden, werden nur die Parameter angezeigt, die auf nicht-Standardwerte festgelegt wurden. Dadurch wird das visuelle Rauschen reduziert und es ist einfacher, die Unterschiede zu erkennen, wenn Instanzen verglichen werden.

```python
from sklearn.linear_model import LogisticRegression

# Erstellen einer Instanz von Logistic Regression mit l1-Strafe
lr = LogisticRegression(penalty="l1")

# Anzeige des Schätzers
print(lr)
```
