# Crear clasificadores

Crearemos clasificadores MLP para cada valor de alfa. Crearemos una tubería que incluya StandardScaler para estandarizar los datos y MLPClassifier con diferentes valores de alfa. Estableceremos el resolutor en 'lbfgs', que es un optimizador de la familia de los métodos quasi-Newton. Estableceremos max_iter en 2000 y early_stopping en True para evitar el sobreajuste. Utilizaremos dos capas ocultas con 10 neuronas cada una.

```python
classifiers = []
names = []
for alpha in alphas:
    classifiers.append(
        make_pipeline(
            StandardScaler(),
            MLPClassifier(
                solver="lbfgs",
                alpha=alpha,
                random_state=1,
                max_iter=2000,
                early_stopping=True,
                hidden_layer_sizes=[10, 10],
            ),
        )
    )
    names.append(f"alpha {alpha:.2f}")
```
