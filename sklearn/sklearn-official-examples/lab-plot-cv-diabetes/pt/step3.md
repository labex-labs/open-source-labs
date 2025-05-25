# Plotar os erros

Agora, plotaremos os erros para visualizar o melhor valor de alfa. Plotaremos as pontuações médias de teste e os erros padrão das pontuações.

```python
scores = clf.cv_results_["mean_test_score"]
scores_std = clf.cv_results_["std_test_score"]

plt.figure().set_size_inches(8, 6)
plt.semilogx(alphas, scores)

std_error = scores_std / np.sqrt(n_folds)

plt.semilogx(alphas, scores + std_error, "b--")
plt.semilogx(alphas, scores - std_error, "b--")

plt.fill_between(alphas, scores + std_error, scores - std_error, alpha=0.2)

plt.ylabel("Pontuação CV +/- erro padrão")
plt.xlabel("alfa")
plt.axhline(np.max(scores), linestyle="--", color=".5")
plt.xlim([alphas[0], alphas[-1]])
```
