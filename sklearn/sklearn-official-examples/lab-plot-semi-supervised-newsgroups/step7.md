# Train and Evaluate the LabelSpreading Model

In this step, we will use LabelSpreading on 20% of the labeled data. We will randomly select 20% of the labeled data, train the model on that data, and then use the model to predict labels for the remaining unlabeled data.

```python
# Train and evaluate the LabelSpreading pipeline
ls_pipeline.fit(X_train, y_train)
y_pred = ls_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
