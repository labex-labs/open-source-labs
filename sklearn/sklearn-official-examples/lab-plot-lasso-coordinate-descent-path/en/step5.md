# Compute Regularization Path Using Positive Elastic Net

In this step, we will compute the regularization path using the positive Elastic Net technique and display the results using matplotlib.

```python
# Compute regularization path using the positive Elastic Net
alphas_positive_enet, coefs_positive_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8, positive=True)

# Display the results using matplotlib
plt.figure(4)
neg_log_alphas_positive_enet = -np.log10(alphas_positive_enet)
for coef_e, coef_pe, c in zip(coefs_enet, coefs_positive_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)
    l2 = plt.plot(neg_log_alphas_positive_enet, coef_pe, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Elastic Net and Positive Elastic Net")
plt.legend((l1[-1], l2[-1]), ("Elastic Net", "Positive Elastic Net"), loc="lower left")
plt.axis("tight")
plt.show()
```
