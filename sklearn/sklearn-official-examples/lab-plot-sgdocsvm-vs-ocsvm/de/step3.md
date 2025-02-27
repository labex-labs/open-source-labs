# Ein One-Class SVM anpassen

Wir werden zunächst ein One-Class SVM mit einem RBF-Kernel an unseren Datensatz anpassen.

```python
# OCSVM-Hyperparameter
nu = 0.05
gamma = 2.0

# Passt das One-Class SVM an
clf = OneClassSVM(gamma=gamma, kernel="rbf", nu=nu)
clf.fit(X_train)
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size

Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
```
