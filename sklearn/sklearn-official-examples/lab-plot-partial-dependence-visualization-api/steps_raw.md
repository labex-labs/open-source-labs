# Advanced Plotting with Partial Dependence Tutorial

## Introduction

This tutorial will guide you through the process of plotting partial dependence curves for multiple features. The partial dependence curves are used to analyze the effect of a feature on the predicted outcome of a machine learning model while holding all other features constant. This tutorial will demonstrate how to plot partial dependence curves for a decision tree and a multi-layer perceptron on the diabetes dataset.

## Steps

### Step 1: Train Models on the Diabetes Dataset

In this step, we will train a decision tree and a multi-layer perceptron on the diabetes dataset.

```python
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = diabetes.target

tree = DecisionTreeRegressor()
mlp = make_pipeline(
    StandardScaler(),
    MLPRegressor(hidden_layer_sizes=(100, 100), tol=1e-2, max_iter=500, random_state=0),
)
tree.fit(X, y)
mlp.fit(X, y)
```

### Step 2: Plotting Partial Dependence for Two Features

In this step, we will plot partial dependence curves for features "age" and "bmi" (body mass index) for the decision tree. With two features, `PartialDependenceDisplay.from_estimator` expects to plot two curves. Here the plot function place a grid of two plots using the space defined by `ax`.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Decision Tree")
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age", "bmi"], ax=ax)
```

The partial dependence curves can be plotted for the multi-layer perceptron. In this case, `line_kw` is passed to `PartialDependenceDisplay.from_estimator` to change the color of the curve.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Multi-layer Perceptron")
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age", "bmi"], ax=ax, line_kw={"color": "red"}
)
```

### Step 3: Plotting Partial Dependence of the Two Models Together

In this step, we will plot the partial dependence curves of the two models on the same plot.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
tree_disp.plot(ax=ax1)
ax1.set_title("Decision Tree")
mlp_disp.plot(ax=ax2, line_kw={"color": "red"})
ax2.set_title("Multi-layer Perceptron")
```

Another way to compare the curves is to plot them on top of each other. Here, we create a figure with one row and two columns. The axes are passed into the `PartialDependenceDisplay.plot` function as a list, which will plot the partial dependence curves of each model on the same axes. The length of the axes list must be equal to the number of plots drawn.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
tree_disp.plot(ax=[ax1, ax2], line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    ax=[ax1, ax2], line_kw={"label": "Multi-layer Perceptron", "color": "red"}
)
ax1.legend()
ax2.legend()
```

`tree_disp.axes_` is a numpy array container the axes used to draw the partial dependence plots. This can be passed to `mlp_disp` to have the same affect of drawing the plots on top of each other. Furthermore, the `mlp_disp.figure_` stores the figure, which allows for resizing the figure after calling `plot`. In this case `tree_disp.axes_` has two dimensions, thus `plot` will only show the y label and y ticks on the left most plot.

```python
tree_disp.plot(line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    line_kw={"label": "Multi-layer Perceptron", "color": "red"}, ax=tree_disp.axes_
)
tree_disp.figure_.set_size_inches(10, 6)
tree_disp.axes_[0, 0].legend()
tree_disp.axes_[0, 1].legend()
plt.show()
```

### Step 4: Plotting Partial Dependence for One Feature

In this step, we will plot the partial dependence curves for a single feature, "age", on the same axes. In this case, `tree_disp.axes_` is passed into the second plot function.

```python
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age"])
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age"], ax=tree_disp.axes_, line_kw={"color": "red"}
)
```

## Summary

This tutorial demonstrated how to plot partial dependence curves for multiple features using the `PartialDependenceDisplay` object. First, we trained a decision tree and a multi-layer perceptron on the diabetes dataset. Then, we plotted partial dependence curves for the decision tree and the multi-layer perceptron for two features. Next, we plotted the partial dependence curves of the two models on the same plot. Finally, we plotted the partial dependence curves for a single feature on the same axes.
