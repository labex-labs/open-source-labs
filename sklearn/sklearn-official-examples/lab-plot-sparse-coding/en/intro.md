# Introduction

In this lab, we will learn how to transform a signal as a sparse combination of Ricker wavelets using sparse coding methods. The Ricker (also known as Mexican hat or the second derivative of a Gaussian) is not a particularly good kernel to represent piecewise constant signals like this one. It can therefore be seen how much adding different widths of atoms matters and it therefore motivates learning the dictionary to best fit your type of signals.

We will visually compare different sparse coding methods using the `SparseCoder` estimator. The richer dictionary on the right is not larger in size, heavier subsampling is performed in order to stay on the same order of magnitude.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
