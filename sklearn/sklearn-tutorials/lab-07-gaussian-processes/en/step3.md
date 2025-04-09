# Gaussian Process Classification (GPC)

GaussianProcessClassifier class implements GPC for probabilistic classification. It places a GP prior on a latent function, which is then squashed through a link function to obtain the class probabilities. GPC supports multi-class classification by performing either one-versus-rest or one-versus-one based training and prediction.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.gaussian_process import GaussianProcessClassifier

# Create a GPC model with an RBF kernel
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict using the trained model
y_pred = model.predict(X_test)
```
