# Introduction

In classification tasks, it is often important to predict not only the class label but also the associated probability. The probability indicates the confidence of the prediction. However, not all classifiers provide well-calibrated probabilities, some being over-confident while others being under-confident. A separate calibration of predicted probabilities is often desirable as a postprocessing. This lab illustrates two different methods for this calibration and evaluates the quality of the returned probabilities using Brier's score.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
