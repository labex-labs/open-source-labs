# Introduction

This lab demonstrates a multi-label document classification problem using scikit-learn. The dataset is generated randomly based on the following process:

- Pick the number of labels: n ~ Poisson(n_labels)
- N times, choose a class c: c ~ Multinomial(theta)
- Pick the document length: k ~ Poisson(length)
- K times, choose a word: w ~ Multinomial(theta_c)

In this process, rejection sampling is used to ensure that n is more than 2, and that the document length is never zero. Likewise, classes that have already been chosen are rejected. The documents that are assigned to both classes are plotted surrounded by two colored circles.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
