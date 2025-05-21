# Configurando Bibliotecas e Criando Dados de Amostra

Neste primeiro passo, importaremos as bibliotecas necessárias e criaremos dados financeiros de amostra para nosso gráfico. Precisamos importar tanto o Matplotlib para visualização quanto o NumPy para geração de dados.

Na primeira célula do seu notebook, insira e execute o seguinte código para importar as bibliotecas necessárias:

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Display plots inline in the notebook
%matplotlib inline

print("Libraries imported successfully!")
```

Após executar o código (pressione Shift+Enter), você deverá ver a saída:

```
Libraries imported successfully!
```

![libraries-imported](../assets/screenshot-20250306-BN9E08ez@2x.png)

Agora, vamos criar alguns dados financeiros de amostra para visualizar. Dados financeiros frequentemente representam valores ao longo do tempo, então criaremos um conjunto de dados simples que pode representar a receita diária ao longo de um período.

Em uma nova célula, adicione e execute o seguinte código:

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

Após executar este código, você verá os primeiros 5 dias de nossos dados de receita de amostra:

```
Sample of daily revenue data (first 5 days):
Day 1: $3745.40
Day 2: $3992.60
Day 3: $2827.45
Day 4: $4137.54
Day 5: $1579.63
```

Esses dados de amostra representam valores de receita diária entre $1.000 e $5.000 por um período de 30 dias. Usaremos esses dados para criar nosso gráfico no próximo passo.
