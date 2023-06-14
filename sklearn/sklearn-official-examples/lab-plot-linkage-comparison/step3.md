# Analyze the Results

We will now analyze the results of our hierarchical clustering. Based on the toy datasets that we used, we can make the following observations:

- Single linkage is fast, and can perform well on non-globular data, but it performs poorly in the presence of noise.
- Average and complete linkage perform well on cleanly separated globular clusters, but have mixed results otherwise.
- Ward is the most effective method for noisy data.

It is important to note that while these observations give us some intuition about the algorithms, this intuition might not apply to very high dimensional data.
