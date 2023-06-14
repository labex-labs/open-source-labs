# Plot Contour

We plot the contour of the decision function. We first create a meshgrid using the `xx` and `yy` arrays. We then reshape the meshgrid into a 2D array and apply the `decision_function` method of the `SVC` class to get the predicted values. We then plot the contour using the `contourf` method.

```python
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

plt.contourf(XX, YY, Z, cmap=plt.get_cmap("RdBu"), alpha=0.5, linestyles=["-"])

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(())
plt.yticks(())
```


