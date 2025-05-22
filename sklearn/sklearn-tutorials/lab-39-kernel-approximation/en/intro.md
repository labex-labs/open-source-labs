# Introduction

This tutorial will guide you through the process of using kernel approximation techniques in scikit-learn.

Kernel methods, such as support vector machines (SVM), are powerful techniques for non-linear classification. These methods rely on the concept of a kernel function that maps input data into a high-dimensional feature space. However, working with explicit feature mappings can be computationally expensive, especially for large datasets. Kernel approximation methods provide a solution by generating low-dimensional approximations of the kernel feature space.

In this tutorial, we will explore several kernel approximation techniques available in scikit-learn, including the Nystroem method, Radial Basis Function (RBF) kernel approximation, Additive Chi Squared (ACS) kernel approximation, Skewed Chi Squared (SCS) kernel approximation, and Polynomial kernel approximation using Tensor Sketch. We will demonstrate how to use these techniques and discuss their advantages and limitations.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
