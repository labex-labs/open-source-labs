# Обучение и оценка гауссовского наивного байесовского классификатора

Теперь мы обучим гауссовский наивный байесовский классификатор на тренировочном наборе и оценим его производительность на тестовом наборе. Мы будем использовать класс `GaussianNB` из модуля `sklearn.naive_bayes`.

```python
from sklearn.naive_bayes import GaussianNB

# Create a Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Train the classifier
gnb.fit(X_train, y_train)

# Predict the target variable for the test set
y_pred = gnb.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = (y_pred == y_test).sum() / len(y_test)
print("Accuracy:", accuracy)
```
