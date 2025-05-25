# Treinar uma Floresta Aleatória e Plotar a Curva ROC

Neste passo, treinaremos um classificador de floresta aleatória e plotaremos sua curva ROC ao lado da curva ROC do SVC. Para fazer isso, criaremos um novo objeto `RandomForestClassifier`, ajustá-lo aos dados de treinamento e, em seguida, criaremos um novo objeto `RocCurveDisplay` usando este classificador. Também passaremos o parâmetro `ax` para esta função para plotar as curvas no mesmo eixo. Finalmente, chamaremos o método `plot()` do objeto `svc_disp` para plotar a curva ROC do SVC.

```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=10, random_state=42)
rfc.fit(X_train, y_train)

ax = plt.gca()
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax, alpha=0.8)
svc_disp.plot(ax=ax, alpha=0.8)
plt.show()
```
