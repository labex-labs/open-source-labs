# Retrieve Decision Path and Leaf Nodes

We can retrieve the decision path of samples of interest using the `decision_path` method. This method outputs an indicator matrix that allows us to retrieve the nodes the samples of interest traverse through. The leaf ids reached by samples of interest can be obtained with the `apply` method. This returns an array of the node ids of the leaves reached by each sample of interest. Using the leaf ids and the `decision_path` we can obtain the splitting conditions that were used to predict a sample or a group of samples. Below is the code to retrieve the decision path and leaf nodes for one sample:

```python
node_indicator = clf.decision_path(X_test)
leaf_id = clf.apply(X_test)

sample_id = 0
# obtain ids of the nodes `sample_id` goes through, i.e., row `sample_id`
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print("Rules used to predict sample {id}:\n".format(id=sample_id))
for node_id in node_index:
    # continue to the next node if it is a leaf node
    if leaf_id[sample_id] == node_id:
        continue

    # check if value of the split feature for sample 0 is below threshold
    if X_test[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "decision node {node} : (X_test[{sample}, {feature}] = {value}) "
        "{inequality} {threshold})".format(
            node=node_id,
            sample=sample_id,
            feature=feature[node_id],
            value=X_test[sample_id, feature[node_id]],
            inequality=threshold_sign,
            threshold=threshold[node_id],
        )
    )
```


