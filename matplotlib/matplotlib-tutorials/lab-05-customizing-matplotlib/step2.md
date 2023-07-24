# Using style sheets

Another way to change the visual appearance of plots is to set the rcParams in a style sheet and import that style sheet with `matplotlib.style.use`. A style sheet is a file that contains a set of rcParams related to the style of a plot. Matplotlib provides a number of pre-defined styles that you can use. For example, the "ggplot" style emulates the aesthetics of the ggplot library in R. You can apply a style sheet like this:

```python
import matplotlib.pyplot as plt

print(plt.style.available)
plt.style.use('Solarize_Light2')
```

You can also define your own custom styles and use them by calling `.style.use` with the path or URL to the style sheet.
