# Preparando o Ambiente e Criando Dados

Nesta primeira etapa, configuraremos nosso ambiente de trabalho importando as bibliotecas necessárias e criando dados de exemplo para nossa visualização. Nos concentraremos em gerar dados que incluem alguns _outliers_ (valores discrepantes), o que demonstrará o valor de usar um gráfico com eixo quebrado.

## Importando as Bibliotecas Necessárias

Vamos começar importando as bibliotecas que precisamos para este tutorial. Usaremos Matplotlib para criar nossas visualizações e NumPy para gerar e manipular dados numéricos.

Crie uma nova célula no seu Jupyter Notebook e digite o seguinte código:

```python
import matplotlib.pyplot as plt
import numpy as np

print(f"NumPy version: {np.__version__}")
```

Ao executar esta célula, você deverá ver uma saída semelhante a esta:

```
NumPy version: 2.0.0
```

![numpy-version](../assets/screenshot-20250306-Um0MaTKw@2x.png)

Os números exatos das versões podem variar dependendo do seu ambiente, mas isso confirma que as bibliotecas estão devidamente instaladas e prontas para uso.

## Gerando Dados de Exemplo com _Outliers_

Agora, vamos criar um conjunto de dados de exemplo que inclua alguns _outliers_. Geraremos números aleatórios e, em seguida, adicionaremos deliberadamente valores maiores a certas posições para criar nossos _outliers_.

Crie uma nova célula e adicione o seguinte código:

```python
# Set random seed for reproducibility
np.random.seed(19680801)

# Generate 30 random points with values between 0 and 0.2
pts = np.random.rand(30) * 0.2

# Add 0.8 to two specific points to create outliers
pts[[3, 14]] += 0.8

# Display the first few data points to understand our dataset
print("First 10 data points:")
print(pts[:10])
print("\nData points containing outliers:")
print(pts[[3, 14]])
```

Ao executar esta célula, você deverá ver uma saída semelhante a:

```
First 10 data points:
[0.01182225 0.11765474 0.07404329 0.91088185 0.10502995 0.11190702
 0.14047499 0.01060192 0.15226977 0.06145634]

Data points containing outliers:
[0.91088185 0.97360754]
```

Nesta saída, você pode ver claramente que os valores nos índices 3 e 14 são muito maiores do que os outros valores. Estes são nossos _outliers_. A maioria dos nossos pontos de dados está abaixo de 0.2, mas esses dois _outliers_ estão acima de 0.9, criando uma disparidade significativa em nosso conjunto de dados.

Este tipo de distribuição de dados é perfeito para demonstrar a utilidade de um gráfico com eixo quebrado. Na próxima etapa, criaremos a estrutura do gráfico e a configuraremos para exibir corretamente tanto os dados principais quanto os _outliers_.
