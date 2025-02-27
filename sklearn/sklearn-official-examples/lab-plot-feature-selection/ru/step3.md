# Построение графика оценки признаков в задачах с одним признаком

Мы можем построить график оценок для каждого признака, чтобы увидеть, какие признаки являются значимыми.

```python
import matplotlib.pyplot as plt

X_indices = np.arange(X.shape[-1])
plt.figure(1)
plt.clf()
plt.bar(X_indices - 0.05, scores, width=0.2)
plt.title("Feature univariate score")
plt.xlabel("Feature number")
plt.ylabel(r"Univariate score ($-Log(p_{value})$)")
plt.show()
```
