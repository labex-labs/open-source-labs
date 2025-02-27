# Análisis de Componentes Independientes (ICA)

#### ICA para la separación de fuentes ciegas

El Análisis de Componentes Independientes (ICA, por sus siglas en inglés) se utiliza para separar señales mezcladas en sus componentes de origen original. Asume que los componentes son estadísticamente independientes y se pueden extraer a través de un proceso de desmezcla lineal. El ICA se puede implementar utilizando la clase `FastICA` de scikit-learn.

```python
from sklearn.decomposition import FastICA

# Crea un objeto ICA con n_components como el número de componentes deseados
ica = FastICA(n_components=2)

# Ajusta el modelo ICA a las señales mezcladas
ica.fit(mixed_signals)

# Separa las señales mezcladas en los componentes de origen original
source_components = ica.transform(mixed_signals)
```
