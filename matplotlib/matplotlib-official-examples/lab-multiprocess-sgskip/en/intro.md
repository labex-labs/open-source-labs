# Introduction

In this lab, you will learn how to use the multiprocessing library and Matplotlib to plot data generated from a separate process. We will create two classes - `ProcessPlotter` and `NBPlot` - to handle the plotting and data generation, respectively. The `NBPlot` class will generate random data and send it to the `ProcessPlotter` class through a pipe, which will then plot the data in real-time.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
