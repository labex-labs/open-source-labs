# Feature-Wichtigkeit aus Koeffizienten

Um eine Vorstellung von der Wichtigkeit der Features zu erhalten, verwenden wir den RidgeCV-Schätzer. Die Features mit dem höchsten absoluten `coef_`-Wert werden als die wichtigsten betrachtet.

```python
from sklearn.linear_model import RidgeCV

ridge = RidgeCV(alphas=np.logspace(-6, 6, num=5)).fit(X, y)
importance = np.abs(ridge.coef_)
feature_names = np.array(diabetes.feature_names)
plt.bar(height=importance, x=feature_names)
plt.title("Feature importances via coefficients")
plt.show()
```
