# Python Matplotlib Lab

## Artist within an Artist

### Introduction

This lab demonstrates how to override basic methods so an artist can contain another artist in Python Matplotlib.

### Steps

1. Import the required libraries:
   ```python
   import matplotlib.pyplot as plt
   import numpy as np
   import matplotlib.lines as lines
   import matplotlib.text as mtext
   import matplotlib.transforms as mtransforms
   ```
2. Create a class called `MyLine` that inherits from `lines.Line2D`:

   ```python
   class MyLine(lines.Line2D):
       def __init__(self, *args, **kwargs):
           # we'll update the position when the line data is set
           self.text = mtext.Text(0, 0, '')
           super().__init__(*args, **kwargs)

           # we can't access the label attr until *after* the line is
           # initiated
           self.text.set_text(self.get_label())

       def set_figure(self, figure):
           self.text.set_figure(figure)
           super().set_figure(figure)

       def set_axes(self, axes):
           self.text.set_axes(axes)
           super().set_axes(axes)

       def set_transform(self, transform):
           # 2 pixel offset
           texttrans = transform + mtransforms.Affine2D().translate(2, 2)
           self.text.set_transform(texttrans)
           super().set_transform(transform)

       def set_data(self, x, y):
           if len(x):
               self.text.set_position((x[-1], y[-1]))

           super().set_data(x, y)

       def draw(self, renderer):
           # draw my label at the end of the line with 2 pixel offset
           super().draw(renderer)
           self.text.draw(renderer)
   ```

3. Set a seed for random state reproducibility:
   ```python
   np.random.seed(19680801)
   ```
4. Create a figure and axis object using `plt.subplots()`:
   ```python
   fig, ax = plt.subplots()
   ```
5. Generate random x and y values with the `np.random.rand()` function:
   ```python
   x, y = np.random.rand(2, 20)
   ```
6. Create an instance of the `MyLine` class with the generated x and y values, and set the fill color to red, marker size to 12 and label to 'line label':
   ```python
   line = MyLine(x, y, mfc='red', ms=12, label='line label')
   ```
7. Set the color of the text object to red and font size to 16:
   ```python
   line.text.set_color('red')
   line.text.set_fontsize(16)
   ```
8. Add the line to the axis object using the `add_line()` method:
   ```python
   ax.add_line(line)
   ```
9. Display the plot using `plt.show()`:
   ```python
   plt.show()
   ```

### Summary

This lab demonstrated how to override basic methods so an artist can contain another artist in Python Matplotlib. We created a custom class called `MyLine` which inherited from `lines.Line2D` and contained a `mtext.Text` instance to label it. We then added the line to an axis object and displayed the plot.
