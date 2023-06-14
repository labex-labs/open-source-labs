# Predict Cluster Membership for Unknown Instances

In this step, we will use the inductive learning model to predict the cluster membership for the generated new samples. We will use the `predict` function from the `InductiveClusterer` class and plot the new samples with their probable clusters.

```python
probable_clusters = inductive_learner.predict(X_new)

plt.subplot(133)
plot_scatter(X, cluster_labels)
plot_scatter(X_new, probable_clusters)
plt.title("Classify unknown instances")
```
