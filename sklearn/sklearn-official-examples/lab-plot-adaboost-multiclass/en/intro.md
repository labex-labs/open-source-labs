# Introduction

In this lab, we will explore how boosting can improve prediction accuracy on a multi-class problem. We will use a dataset constructed by taking a ten-dimensional standard normal distribution and defining three classes separated by nested concentric ten-dimensional spheres such that roughly equal numbers of samples are in each class.

We will compare the performance of the SAMME and SAMME.R algorithms. SAMME.R uses the probability estimates to update the additive model, while SAMME uses the classifications only.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
