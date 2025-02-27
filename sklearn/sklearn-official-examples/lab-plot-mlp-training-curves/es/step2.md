# Definir diferentes estrategias de aprendizaje

A continuación, necesitamos definir las diferentes estrategias de aprendizaje que queremos comparar. Definiremos varios diferentes planes de tasa de aprendizaje y parámetros de impulso, incluyendo tasa de aprendizaje constante, constante con impulso, constante con impulso de Nesterov, tasa de aprendizaje de escalado inverso, escalado inverso con impulso, escalado inverso con impulso de Nesterov y adam. También definiremos etiquetas y argumentos de trazado para usarlos en nuestro trazado más adelante.

```python
# diferentes planes de tasa de aprendizaje y parámetros de impulso
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
    "tasa de aprendizaje constante",
    "constante con impulso",
    "constante con impulso de Nesterov",
    "tasa de aprendizaje de escalado inverso",
    "escalado inverso con impulso",
    "escalado inverso con impulso de Nesterov",
    "adam",
]

plot_args = [
    {"c": "rojo", "linestyle": "-"},
    {"c": "verde", "linestyle": "-"},
    {"c": "azul", "linestyle": "-"},
    {"c": "rojo", "linestyle": "--"},
    {"c": "verde", "linestyle": "--"},
    {"c": "azul", "linestyle": "--"},
    {"c": "negro", "linestyle": "-"},
]
```
