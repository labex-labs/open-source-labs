# Initialize the VotingClassifier

We will then initialize a soft-voting VotingClassifier with weights `[1, 1, 5]`, which means that the predicted probabilities of the RandomForestClassifier count 5 times as much as the weights of the other classifiers when the averaged probability is calculated.

```python
eclf = VotingClassifier(
    estimators=[("lr", clf1), ("rf", clf2), ("gnb", clf3)],
    voting="soft",
    weights=[1, 1, 5],
)
```


