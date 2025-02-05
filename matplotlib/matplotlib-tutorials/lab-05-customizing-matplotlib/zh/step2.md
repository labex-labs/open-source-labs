# 使用样式表

另一种更改图表视觉外观的方法是在样式表中设置rcParams，并使用`matplotlib.style.use`导入该样式表。样式表是一个包含与图表样式相关的一组rcParams的文件。Matplotlib提供了许多预定义的样式供你使用。例如，“ggplot”样式模仿了R语言中ggplot库的美学风格。你可以像这样应用样式表：

```python
import matplotlib.pyplot as plt

print(plt.style.available)
plt.style.use('Solarize_Light2')
```

你也可以定义自己的自定义样式，并通过调用`.style.use`并传入样式表的路径或URL来使用它们。
