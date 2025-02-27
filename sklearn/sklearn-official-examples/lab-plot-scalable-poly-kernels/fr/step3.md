# Établir le modèle d'approximation du noyau

Nous allons maintenant entraîner des SVM linéaires sur les caractéristiques générées par PolynomialCountSketch avec différentes valeurs pour n_components. Nous utiliserons une boucle pour itérer sur différentes valeurs de n_components et afficher la précision de chaque modèle.

```python
from sklearn.kernel_approximation import PolynomialCountSketch

n_runs = 1
N_COMPONENTS = [250, 500, 1000, 2000]

for n_components in N_COMPONENTS:
    ps_lsvm_score = 0
    for _ in range(n_runs):
        # Entraîner un SVM linéaire sur les caractéristiques générées par PolynomialCountSketch
        pipeline = make_pipeline(
            PolynomialCountSketch(n_components=n_components, degree=4),
            LinearSVC(dual="auto"),
        )
        pipeline.fit(X_train, y_train)
        ps_lsvm_score += 100 * pipeline.score(X_test, y_test)

    ps_lsvm_score /= n_runs

    # Afficher la précision du modèle
    print(f"Linear SVM score on {n_components} PolynomialCountSketch features: {ps_lsvm_score:.2f}%")
```
