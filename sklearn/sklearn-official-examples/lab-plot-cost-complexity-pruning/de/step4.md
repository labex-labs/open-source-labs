# Trainieren der Entscheidungsbäume

Als nächstes werden wir einen Entscheidungsbaum mit jeder der effektiven Alpha-Werte trainieren. Der letzte Wert in `ccp_alphas` ist der Alpha-Wert, der den gesamten Baum präunt und den Baum mit nur einem Knoten zurücklässt.

```python
clfs = []
for ccp_alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)
print(
    "Anzahl der Knoten im letzten Baum ist: {} mit ccp_alpha: {}".format(
        clfs[-1].tree_.node_count, ccp_alphas[-1]
    )
)
```
