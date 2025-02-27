# Определение SequenceKernel

Мы определяем класс `SequenceKernel`, который наследуется от классов `Kernel` и `GenericKernelMixin` из scikit-learn. Этот ядро определяет меру сходства между последовательностями переменной длины. Для этого используется R-конволюция, которая включает интегрирование бинарного ядра по буквам для всех пар букв между парой строк. Затем мы можем использовать это ядро для выполнения задач регрессии и классификации на последовательностях.

```python
import numpy as np
from sklearn.gaussian_process.kernels import Kernel, Hyperparameter
from sklearn.gaussian_process.kernels import GenericKernelMixin
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.base import clone


class SequenceKernel(GenericKernelMixin, Kernel):
    """
    Минимальное (но валидное) сверточное ядро для последовательностей
    переменной длины."""

    def __init__(self, baseline_similarity=0.5, baseline_similarity_bounds=(1e-5, 1)):
        self.baseline_similarity = baseline_similarity
        self.baseline_similarity_bounds = baseline_similarity_bounds

    @property
    def hyperparameter_baseline_similarity(self):
        return Hyperparameter(
            "baseline_similarity", "numeric", self.baseline_similarity_bounds
        )

    def _f(self, s1, s2):
        """
        Значение ядра между парой последовательностей
        """
        return sum(
            [1.0 if c1 == c2 else self.baseline_similarity for c1 in s1 for c2 in s2]
        )

    def _g(self, s1, s2):
        """
        Производная ядра между парой последовательностей
        """
        return sum([0.0 if c1 == c2 else 1.0 for c1 in s1 for c2 in s2])

    def __call__(self, X, Y=None, eval_gradient=False):
        if Y is None:
            Y = X

        if eval_gradient:
            return (
                np.array([[self._f(x, y) for y in Y] for x in X]),
                np.array([[[self._g(x, y)] for y in Y] for x in X]),
            )
        else:
            return np.array([[self._f(x, y) for y in Y] for x in X])

    def diag(self, X):
        return np.array([self._f(x, x) for x in X])

    def is_stationary(self):
        return False

    def clone_with_theta(self, theta):
        cloned = clone(self)
        cloned.theta = theta
        return cloned
```
