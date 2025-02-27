# Définissez différentes stratégies d'apprentissage

Ensuite, nous devons définir les différentes stratégies d'apprentissage que nous voulons comparer. Nous définirons plusieurs programmes de taux d'apprentissage différents et des paramètres de momentum, y compris un taux d'apprentissage constant, constant avec momentum, constant avec le momentum de Nesterov, taux d'apprentissage à mise à l'échelle inverse, à mise à l'échelle inverse avec momentum, à mise à l'échelle inverse avec le momentum de Nesterov et adam. Nous définirons également des étiquettes et des arguments de tracé à utiliser dans notre tracé plus tard.

```python
# différents programmes de taux d'apprentissage et paramètres de momentum
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
    "taux d'apprentissage constant",
    "constant avec momentum",
    "constant avec le momentum de Nesterov",
    "taux d'apprentissage à mise à l'échelle inverse",
    "à mise à l'échelle inverse avec momentum",
    "à mise à l'échelle inverse avec le momentum de Nesterov",
    "adam",
]

plot_args = [
    {"c": "rouge", "linestyle": "-"},
    {"c": "vert", "linestyle": "-"},
    {"c": "bleu", "linestyle": "-"},
    {"c": "rouge", "linestyle": "--"},
    {"c": "vert", "linestyle": "--"},
    {"c": "bleu", "linestyle": "--"},
    {"c": "noir", "linestyle": "-"},
]
```
