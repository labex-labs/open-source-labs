# Introduction

This lab provides an example of how to use scikit-learn for text classification using out-of-core learning. The goal is to learn from data that does not fit into main memory. To achieve this, we make use of an online classifier that supports the partial_fit method, which will be fed with batches of examples. To ensure that the feature space remains the same over time, we leverage a HashingVectorizer that will project each example into the same feature space. This is especially useful in the case of text classification where new features (words) may appear in each batch.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
