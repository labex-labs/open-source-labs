# Compute Regularization Path Using Positive Lasso

In this step, we will compute the regularization path using the positive Lasso technique and display the results using matplotlib.

```python
# Compute regularization path using the positive Lasso
alphas_positive_lasso, coefs_positive_lasso, _ = lasso_path(X, y, eps=eps, positive=True)

# Display the results using matplotlib
plt.figure(2)
neg_log_alphas_positive_lasso = -np.log10(alphas_positive_lasso)
for coef_l, coef_pl, c in zip(coefs_lasso, coefs_positive_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)
    l2 = plt.plot(neg_log_alphas_positive_lasso, coef_pl, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Lasso and Positive Lasso")
plt.legend((l1[-1], l2[-1]), ("Lasso", "Positive Lasso"), loc="lower left")
plt.axis("tight")
plt.show()
```
