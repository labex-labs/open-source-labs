# Introduction

This lab will demonstrate how to use polynomial kernel approximation in scikit-learn to efficiently generate polynomial kernel feature-space approximations. This is used to train linear classifiers that approximate the accuracy of kernelized ones. We will be using the Covtype dataset, which contains 581,012 samples with 54 features each, distributed among 6 classes. The goal of this dataset is to predict forest cover type from cartographic variables only (no remotely sensed data). After loading, we transform it into a binary classification problem to match the version of the dataset in the LIBSVM webpage, which was the one used in the original paper.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
