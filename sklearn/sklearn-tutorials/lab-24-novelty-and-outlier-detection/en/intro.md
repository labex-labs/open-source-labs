# Introduction

Novelty and outlier detection are techniques used to identify whether a new observation belongs to the same distribution as existing observations or if it should be considered as different. These techniques are commonly used to clean real datasets by identifying abnormal or unusual observations.

There are two important distinctions in this context:

1. Outlier detection: The training data contains outliers, which are observations that are far from the others. Outlier detection estimators try to fit the regions where the training data is the most concentrated, ignoring the deviant observations.
2. Novelty detection: The training data is not polluted by outliers, and the goal is to detect whether a new observation is an outlier. In this context, an outlier is also called a novelty.

The scikit-learn project provides a set of machine learning tools that can be used for both novelty and outlier detection. These tools are implemented using unsupervised learning algorithms, which means they learn patterns from the data without the need for labeled examples.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
