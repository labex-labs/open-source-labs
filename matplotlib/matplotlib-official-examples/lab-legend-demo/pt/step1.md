# Criar uma legenda para linhas específicas

Nesta etapa, criaremos uma legenda para linhas específicas.

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define data for the chart
t1 = np.arange(0.0, 2.0, 0.1)
t2 = np.arange(0.0, 2.0, 0.01)

# Create a plot with multiple lines
fig, ax = plt.subplots()
l1, = ax.plot(t2, np.exp(-t2))
l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 's-.')

# Create a legend for two of the lines
ax.legend((l2, l4), ('oscillatory', 'damped'), loc='upper right', shadow=True)

# Add labels and title to the chart
ax.set_xlabel('time')
ax.set_ylabel('volts')
ax.set_title('Damped oscillation')

# Display the chart
plt.show()
```
