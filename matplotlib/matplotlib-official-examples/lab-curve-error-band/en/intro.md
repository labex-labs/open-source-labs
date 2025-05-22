# Introduction

This tutorial will guide you on how to draw a curve with an error band using Python Matplotlib. An error band is used to indicate the uncertainty of the curve. In this example, we assume that the error can be given as a scalar _err_ that describes the uncertainty perpendicular to the curve in every point. We visualize this error as a colored band around the path using a `.PathPatch`. The patch is created from two path segments _(xp, yp)_, and _(xn, yn)_ that are shifted by +/- _err_ perpendicular to the curve _(x, y)_.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
