# Get Class Probabilities for the First Sample in the Dataset

We will get the class probabilities for the first sample in the dataset and store them in class1_1 and class2_1.

```python
class1_1 = [pr[0, 0] for pr in probas]
class2_1 = [pr[0, 1] for pr in probas]
```


