# Classifier Chain Ensemble

## Introduction

This lab demonstrates an example of using classifier chain on a multilabel dataset. The Classifier Chain algorithm is a modification of the problem transformation method for multi-label classification. This method exploits the correlation among the classes by building a chain of binary classifiers. Each model gets the predictions of the preceding models in the chain as features. We will use the `yeast` dataset which contains 2417 datapoints each with 103 features and 14 possible labels. Each data point has at least one label. As a baseline we first train a logistic regression classifier for each of the 14 labels. To evaluate the performance of these classifiers we predict on a held-out test set and calculate the Jaccard score for each sample.

## Steps

### Step 1: Load the yeast dataset

```python
X, Y = fetch_openml("yeast", version=4, return_X_y=True, parser="pandas")
Y = Y == "TRUE"
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
```

### Step 2: Train an independent logistic regression model for each class

```python
base_lr = LogisticRegression()
ovr = OneVsRestClassifier(base_lr)
ovr.fit(X_train, Y_train)
Y_pred_ovr = ovr.predict(X_test)
ovr_jaccard_score = jaccard_score(Y_test, Y_pred_ovr, average="samples")
```

### Step 3: Train an ensemble of logistic regression classifier chains

```python
chains = [ClassifierChain(base_lr, order="random", random_state=i) for i in range(10)]
for chain in chains:
    chain.fit(X_train, Y_train)

Y_pred_chains = np.array([chain.predict(X_test) for chain in chains])
chain_jaccard_scores = [
    jaccard_score(Y_test, Y_pred_chain >= 0.5, average="samples")
    for Y_pred_chain in Y_pred_chains
]
```

### Step 4: Take the average prediction of all the chains

```python
Y_pred_ensemble = Y_pred_chains.mean(axis=0)
ensemble_jaccard_score = jaccard_score(
    Y_test, Y_pred_ensemble >= 0.5, average="samples"
)
```

### Step 5: Plot the Jaccard similarity scores

```python
model_scores = [ovr_jaccard_score] + chain_jaccard_scores
model_scores.append(ensemble_jaccard_score)

model_names = (
    "Independent",
    "Chain 1",
    "Chain 2",
    "Chain 3",
    "Chain 4",
    "Chain 5",
    "Chain 6",
    "Chain 7",
    "Chain 8",
    "Chain 9",
    "Chain 10",
    "Ensemble",
)

x_pos = np.arange(len(model_names))

fig, ax = plt.subplots(figsize=(7, 4))
ax.grid(True)
ax.set_title("Classifier Chain Ensemble Performance Comparison")
ax.set_xticks(x_pos)
ax.set_xticklabels(model_names, rotation="vertical")
ax.set_ylabel("Jaccard Similarity Score")
ax.set_ylim([min(model_scores) * 0.9, max(model_scores) * 1.1])
colors = ["r"] + ["b"] * len(chain_jaccard_scores) + ["g"]
ax.bar(x_pos, model_scores, alpha=0.5, color=colors)
plt.tight_layout()
plt.show()
```

## Summary

This lab showed how to use the Classifier Chain algorithm to build an ensemble of logistic regression classifier chains to exploit correlations among the classes. The Jaccard similarity score for each chain tends to be greater than that of the set independent logistic models. Finally, we constructed a voting ensemble of classifier chains by averaging the binary predictions of the chains and applied a threshold of 0.5. The Jaccard similarity score of the ensemble was greater than that of the independent models and tended to exceed the score of each chain in the ensemble.
