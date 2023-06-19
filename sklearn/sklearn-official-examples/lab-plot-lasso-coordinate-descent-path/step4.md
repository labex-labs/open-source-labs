# Compute Regularization Path Using Elastic Net

In this step, we will compute the regularization path using the Elastic Net technique and display the results using matplotlib.

```python
from sklearn.linear_model import enet_path

# Compute regularization path using the Elastic Net
alphas_enet, coefs_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8)

# Display the results using matplotlib
plt.figure(3)
neg_log_alphas_enet = -np.log10(alphas_enet)
for coef_e, c in zip(coefs_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Elastic Net Path")
plt.axis("tight")
plt.show()
```


