# Definindo diferentes estratégias de aprendizagem

Em seguida, precisamos definir as diferentes estratégias de aprendizagem que desejamos comparar. Definiremos vários cronogramas diferentes de taxa de aprendizagem e parâmetros de momento, incluindo taxa de aprendizagem constante, constante com momento, constante com momento de Nesterov, taxa de aprendizagem com escala inversa, com escala inversa com momento, com escala inversa com momento de Nesterov e adam. Também definiremos rótulos e plot_args para usar em nosso gráfico posteriormente.

```python
# diferentes cronogramas de taxa de aprendizagem e parâmetros de momento
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
    "taxa de aprendizagem constante",
    "constante com momento",
    "constante com momento de Nesterov",
    "taxa de aprendizagem com escala inversa",
    "escala inversa com momento",
    "escala inversa com momento de Nesterov",
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
