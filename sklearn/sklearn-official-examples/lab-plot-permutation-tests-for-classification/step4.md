# Plot the Results

We plot a histogram of the permutation scores (the null distribution) for both the original iris dataset and the randomized data. We also indicate the score obtained by the classifier on the original data using a red line. The p-value is displayed on each graph.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Original data
ax.hist(perm_scores_iris, bins=20, density=True)
ax.axvline(score_iris, ls="--", color="r")
score_label = f"Score on original\ndata: {score_iris:.2f}\n(p-value: {pvalue_iris:.3f})"
ax.text(0.7, 10, score_label, fontsize=12)
ax.set_xlabel("Accuracy score")
_ = ax.set_ylabel("Probability density")

plt.show()

fig, ax = plt.subplots()

# Random data
ax.hist(perm_scores_rand, bins=20, density=True)
ax.set_xlim(0.13)
ax.axvline(score_rand, ls="--", color="r")
score_label = f"Score on original\ndata: {score_rand:.2f}\n(p-value: {pvalue_rand:.3f})"
ax.text(0.14, 7.5, score_label, fontsize=12)
ax.set_xlabel("Accuracy score")
ax.set_ylabel("Probability density")

plt.show()
```
