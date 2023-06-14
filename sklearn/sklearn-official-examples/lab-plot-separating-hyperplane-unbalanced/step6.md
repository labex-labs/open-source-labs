# Plot the Decision Functions for Both Classifiers

We will plot the decision functions for both classifiers using the `DecisionBoundaryDisplay` function from the `sklearn.inspection` library. We will set `plot_method` to `"contour"`, `colors` to `"k"` for the plain SVM and `"r"` for the weighted SVM, `levels` to `[0]`, `alpha` to `0.5`, and `linestyles` to `["-"]`. We will also set `ax` to `plt.gca()`.

```python
ax = plt.gca()
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)

wdisp = DecisionBoundaryDisplay.from_estimator(
    wclf,
    X,
    plot_method="contour",
    colors="r",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)
```


