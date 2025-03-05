# Creating a Jupyter Notebook and Importing Required Libraries

First, we need to create a new Jupyter Notebook and import the required libraries for our plotting task.

1. In the Jupyter Notebook environment, create a new notebook by clicking on the "New" button in the top right corner and selecting "Python 3 (ipykernel)".

2. Rename your notebook to `watermark-image.ipynb` by clicking on "Untitled" at the top of the page and entering the new name.

3. In the first cell of your notebook, enter the following code to import the necessary libraries:

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
```

Let's understand what each of these libraries does:

- `matplotlib.pyplot` (aliased as `plt`): A collection of functions that make matplotlib work like MATLAB, providing a convenient interface for creating plots.
- `numpy` (aliased as `np`): A fundamental package for scientific computing in Python, which we'll use for data manipulation.
- `matplotlib.cbook`: A collection of utility functions for matplotlib, including functions to get sample data.
- `matplotlib.image`: A module for image-related functionality in matplotlib, which we'll use to read and display images.

4. Run the cell by clicking the "Run" button at the top of the notebook or by pressing Shift+Enter.

This cell execution should complete without any output, indicating that all libraries were successfully imported.
