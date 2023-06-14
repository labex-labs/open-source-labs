# Visualize the OOB Error Rate

Finally, we will plot the OOB error rate for each classifier as a function of the number of estimators. This will allow us to identify the number of estimators at which the error rate stabilizes. We will use Matplotlib to generate the plot.

```python
for label, clf_err in error_rate.items():
    xs, ys = zip(*clf_err)
    plt.plot(xs, ys, label=label)

plt.xlim(min_estimators, max_estimators)
plt.xlabel("n_estimators")
plt.ylabel("OOB error rate")
plt.legend(loc="upper right")
plt.show()
```
