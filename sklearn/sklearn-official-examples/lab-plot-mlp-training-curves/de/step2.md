# Definieren unterschiedlicher Lernstrategien

Als nächstes müssen wir die verschiedenen Lernstrategien definieren, die wir vergleichen möchten. Wir werden mehrere verschiedene Lernraten-Schedules und Momentum-Parameter definieren, einschließlich konstanter Lernrate, konstant mit Momentum, konstant mit Nesterovs Momentum, invers skalierende Lernrate, invers skalierende mit Momentum, invers skalierende mit Nesterovs Momentum und Adam. Wir definieren auch Labels und plot_args, die wir später in unserem Plot verwenden werden.

```python
# verschiedene Lernraten-Schedules und Momentum-Parameter
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
    "konstante Lernrate",
    "konstant mit Momentum",
    "konstant mit Nesterovs Momentum",
    "invers skalierende Lernrate",
    "invers skalierende mit Momentum",
    "invers skalierende mit Nesterovs Momentum",
    "Adam",
]

plot_args = [
    {"c": "rot", "linestyle": "-"},
    {"c": "grün", "linestyle": "-"},
    {"c": "blau", "linestyle": "-"},
    {"c": "rot", "linestyle": "--"},
    {"c": "grün", "linestyle": "--"},
    {"c": "blau", "linestyle": "--"},
    {"c": "schwarz", "linestyle": "-"},
]
```