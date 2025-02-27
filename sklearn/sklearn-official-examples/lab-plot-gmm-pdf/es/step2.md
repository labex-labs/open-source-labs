# Generar datos

A continuación, generaremos un conjunto de datos de mezcla gaussiana con dos componentes. Crearemos un conjunto de datos gaussiano desplazado centrado en (20, 20) y un conjunto de datos gaussiano estirado centrado en cero. Luego concatenaremos los dos conjuntos de datos en el conjunto de entrenamiento final.

```python
n_samples = 300

# generar muestra aleatoria, dos componentes
np.random.seed(0)

# generar datos esféricos centrado en (20, 20)
shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])

# generar datos gaussianos estirados centrado en cero
C = np.array([[0.0, -0.7], [3.5, 0.7]])
stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)

# concatenar los dos conjuntos de datos en el conjunto de entrenamiento final
X_train = np.vstack([shifted_gaussian, stretched_gaussian])
```
