# Criar Classificadores

Criaremos classificadores MLP para cada valor de alpha. Criaremos um pipeline que inclui `StandardScaler` para padronizar os dados e `MLPClassifier` com diferentes valores de alpha. Definiremos o solucionador para 'lbfgs', que é um otimizador da família de métodos quase-Newton. Definiremos `max_iter` para 2000 e `early_stopping` para True para evitar o superajuste. Usaremos duas camadas ocultas com 10 neurônios cada.

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
