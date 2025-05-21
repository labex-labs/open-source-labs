# Entendendo o Matplotlib e Criando um Notebook

Neste primeiro passo, aprenderemos sobre o Matplotlib e criaremos um novo notebook Jupyter para nossa tarefa de visualização.

## O que é Matplotlib?

Matplotlib é uma biblioteca abrangente para criar visualizações estáticas, animadas e interativas em Python. Ela fornece uma API orientada a objetos para incorporar gráficos em aplicativos e é amplamente utilizada para visualização de dados por cientistas, engenheiros e analistas de dados.

## Criar um Novo Notebook

Na primeira célula do seu notebook, vamos importar a biblioteca Matplotlib. Digite o seguinte código e execute a célula pressionando Shift+Enter:

```python
import matplotlib.pyplot as plt
import numpy as np

# Check the Matplotlib version
print(f"NumPy version: {np.__version__}")
```

![libraries-imported](../assets/screenshot-20250306-K6iIFfj1@2x.png)

Ao executar este código, você deverá ver uma saída semelhante a:

```
NumPy version: 2.0.0
```

O número da versão exata pode variar dependendo do seu ambiente.

Agora temos o Matplotlib importado e pronto para usar. `plt` é um alias convencional usado para o módulo pyplot, que fornece uma interface semelhante ao MATLAB para criar gráficos.
