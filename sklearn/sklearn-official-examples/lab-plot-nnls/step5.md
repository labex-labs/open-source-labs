# Compare Regression Coefficients

We will now compare the regression coefficients between non-negative least squares regression and classic linear regression. We will plot the coefficients against each other and observe that they are highly correlated. However, the non-negative constraint shrinks some coefficients to 0. This is because non-negative least squares inherently yield sparse results.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(reg_ols.coef_, reg_nnls.coef_, linewidth=0, marker=".")

low_x, high_x = ax.get_xlim()
low_y, high_y = ax.get_ylim()
low = max(low_x, low_y)
high = min(high_x, high_y)
ax.plot([low, high], [low, high], ls="--", c=".3", alpha=0.5)
ax.set_xlabel("OLS regression coefficients", fontweight="bold")
ax.set_ylabel("NNLS regression coefficients", fontweight="bold")
```
