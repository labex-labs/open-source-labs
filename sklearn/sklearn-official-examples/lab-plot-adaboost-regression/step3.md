# Plotting the results

Finally, we plot how well our two regressors, single decision tree regressor and AdaBoost regressor, could fit the data. We use Matplotlib's `scatter()` function to plot the training samples and the predicted values from both regressors. We use Matplotlib's `plot()` function to plot the predicted values against the data for both regressors. We add a legend to the plot to distinguish between the two regressors.

```python
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette("colorblind")

plt.figure()
plt.scatter(X, y, color=colors[0], label="training samples")
plt.plot(X, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
plt.plot(X, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Boosted Decision Tree Regression")
plt.legend()
plt.show()
```
