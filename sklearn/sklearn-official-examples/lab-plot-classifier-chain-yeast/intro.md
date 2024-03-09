# Introduction

This lab demonstrates an example of using classifier chain on a multilabel dataset. The Classifier Chain algorithm is a modification of the problem transformation method for multi-label classification. This method exploits the correlation among the classes by building a chain of binary classifiers. Each model gets the predictions of the preceding models in the chain as features. We will use the `yeast` dataset which contains 2417 datapoints each with 103 features and 14 possible labels. Each data point has at least one label. As a baseline we first train a logistic regression classifier for each of the 14 labels. To evaluate the performance of these classifiers we predict on a held-out test set and calculate the Jaccard score for each sample.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
