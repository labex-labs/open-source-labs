# Introduction

This lab introduces SVM tie-breaking and its effect on decision boundary. In SVM, tie-breaking is the mechanism used to resolve the conflicts between the two or more classes when their distances are equal. It is not enabled by default when `decision_function_shape='ovr'` because it is costly. Therefore, this lab illustrates the effect of the `break_ties` parameter for a multiclass classification problem and `decision_function_shape='ovr'`.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
