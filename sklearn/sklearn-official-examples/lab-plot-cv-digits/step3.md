# Define the hyperparameter values to test

We will test different values of the regularization parameter C, which controls the trade-off between maximizing the margin and minimizing the classification error. We will test 10 logarithmically-spaced values between 10^-10 and 1.

```python
C_s = np.logspace(-10, 0, 10)
```
