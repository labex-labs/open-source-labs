# Configuración de Bibliotecas y Creación de Datos de Muestra

En este primer paso, importaremos las bibliotecas necesarias y crearemos datos financieros de muestra para nuestra gráfica. Necesitamos importar tanto Matplotlib para la visualización como NumPy para la generación de datos.

En la primera celda de su cuaderno (notebook), ingrese y ejecute el siguiente código para importar las bibliotecas requeridas:

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Display plots inline in the notebook
%matplotlib inline

print("Libraries imported successfully!")
```

Después de ejecutar el código (presione Shift+Enter), debería ver la salida:

```
Libraries imported successfully!
```

![libraries-imported](../assets/screenshot-20250306-BN9E08ez@2x.png)

Ahora, creemos algunos datos financieros de muestra para visualizar. Los datos financieros a menudo representan valores a lo largo del tiempo, por lo que crearemos un conjunto de datos simple que podría representar los ingresos diarios durante un período de tiempo.

En una nueva celda, agregue y ejecute el siguiente código:

```python
# Set a random seed for reproducibility
np.random.seed(42)

# Generate financial data: 30 days of revenue data
days = np.arange(1, 31)
daily_revenue = np.random.uniform(low=1000, high=5000, size=30)

print("Sample of daily revenue data (first 5 days):")
for i in range(5):
    print(f"Day {days[i]}: ${daily_revenue[i]:.2f}")
```

Después de ejecutar este código, verá los primeros 5 días de nuestros datos de ingresos de muestra:

```
Sample of daily revenue data (first 5 days):
Day 1: $3745.40
Day 2: $3992.60
Day 3: $2827.45
Day 4: $4137.54
Day 5: $1579.63
```

Este conjunto de datos de muestra representa valores de ingresos diarios entre $1,000 y $5,000 durante un período de 30 días. Usaremos estos datos para crear nuestra gráfica en el siguiente paso.
