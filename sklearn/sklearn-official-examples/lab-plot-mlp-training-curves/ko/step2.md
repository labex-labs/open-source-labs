# 서로 다른 학습 전략 정의

다음으로, 비교하고자 하는 서로 다른 학습 전략을 정의해야 합니다. 일정 학습률, 일정 학습률 (모멘텀 포함), 일정 학습률 (Nesterov 모멘텀 포함), 역스케일링 학습률, 역스케일링 학습률 (모멘텀 포함), 역스케일링 학습률 (Nesterov 모멘텀 포함), adam 등 여러 가지 서로 다른 학습률 스케줄과 모멘텀 매개변수를 정의합니다. 또한, 나중에 플롯에 사용할 레이블과 plot_args 를 정의합니다.

```python
# 서로 다른 학습률 스케줄과 모멘텀 매개변수
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
    "일정 학습률",
    "일정 학습률 (모멘텀 포함)",
    "일정 학습률 (Nesterov 모멘텀 포함)",
    "역스케일링 학습률",
    "역스케일링 학습률 (모멘텀 포함)",
    "역스케일링 학습률 (Nesterov 모멘텀 포함)",
    "adam",
]

plot_args = [
    {"c": "red", "linestyle": "-"},
    {"c": "green", "linestyle": "-"},
    {"c": "blue", "linestyle": "-"},
    {"c": "red", "linestyle": "--"},
    {"c": "green", "linestyle": "--"},
    {"c": "blue", "linestyle": "--"},
    {"c": "black", "linestyle": "-"},
]
```
