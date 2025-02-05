# 定义不同的学习策略

接下来，我们需要定义想要比较的不同学习策略。我们将定义几种不同的学习率调度和动量参数，包括恒定学习率、带动量的恒定学习率、带Nesterov动量的恒定学习率、逆缩放学习率、带动量的逆缩放学习率、带Nesterov动量的逆缩放学习率以及Adam。我们还将定义标签和绘图参数，以便稍后在绘图中使用。

```python
# 不同的学习率调度和动量参数
params = [
    {
        "solver": "sgd",
        "learning_rate": "constant",
        "momentum": 0,
        "learning_rate_init": 0.2,
    },
    {
        "solver": "sgd",
        "learning_rate": "constant",
        "momentum": 0.9,
        "nesterovs_momentum": False,
        "learning_rate_init": 0.2,
    },
    {
        "solver": "sgd",
        "learning_rate": "constant",
        "momentum": 0.9,
        "nesterovs_momentum": True,
        "learning_rate_init": 0.2,
    },
    {
        "solver": "sgd",
        "learning_rate": "invscaling",
        "momentum": 0,
        "learning_rate_init": 0.2,
    },
    {
        "solver": "sgd",
        "learning_rate": "invscaling",
        "momentum": 0.9,
        "nesterovs_momentum": True,
        "learning_rate_init": 0.2,
    },
    {
        "solver": "sgd",
        "learning_rate": "invscaling",
        "momentum": 0.9,
        "nesterovs_momentum": False,
        "learning_rate_init": 0.2,
    },
    {"solver": "adam", "learning_rate_init": 0.01},
]

labels = [
    "恒定学习率",
    "带动量的恒定学习率",
    "带Nesterov动量的恒定学习率",
    "逆缩放学习率",
    "带动量的逆缩放学习率",
    "带Nesterov动量的逆缩放学习率",
    "Adam",
]

plot_args = [
    {"c": "红色", "linestyle": "-"},
    {"c": "绿色", "linestyle": "-"},
    {"c": "蓝色", "linestyle": "-"},
    {"c": "红色", "linestyle": "--"},
    {"c": "绿色", "linestyle": "--"},
    {"c": "蓝色", "linestyle": "--"},
    {"c": "黑色", "linestyle": "-"},
]
```
