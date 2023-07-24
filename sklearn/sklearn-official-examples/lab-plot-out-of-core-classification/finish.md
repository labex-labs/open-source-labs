# Summary

In this lab, we learned how to use scikit-learn for text classification using out-of-core learning. We used an online classifier that supports the partial_fit method, which was fed with batches of examples. We also leveraged a HashingVectorizer to ensure that the feature space remained the same over time. We then held out a test set and iterated over mini-batches of examples to update the classifiers. Finally, we plotted the results to visualize the accuracy evolution and training times.
