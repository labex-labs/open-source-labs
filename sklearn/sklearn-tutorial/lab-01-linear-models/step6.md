# Perceptron

#### Introduction:

The Perceptron is a simple linear classification algorithm suitable for large-scale learning. It updates its model only on mistakes, making it faster to train than the stochastic gradient descent (SGD) with hinge loss. The resulting models are also sparser.

#### Code:

Let's fit a perceptron model.

```python
clf = linear_model.Perceptron(alpha=0.1)
clf.fit(X, y)

print(clf.coef_)
```

#### Explanation:

- We create an instance of `Perceptron` with the regularization parameter `alpha` set to 0.1.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the perceptron model.
