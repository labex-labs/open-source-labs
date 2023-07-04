# Gaussian Process Classification (GPC)

GaussianProcessClassifier class implements GPC for probabilistic classification. It places a GP prior on a latent function, which is then squashed through a link function to obtain the class probabilities. GPC supports multi-class classification by performing either one-versus-rest or one-versus-one based training and prediction.

```python
from sklearn.gaussian_process import GaussianProcessClassifier

# Create a GPC model with an RBF kernel
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict using the trained model
y_pred = model.predict(X_test)
```
