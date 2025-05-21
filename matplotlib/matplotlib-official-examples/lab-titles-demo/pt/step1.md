# Criação de Gráficos Básicos com Posição de Título Padrão

Nesta etapa, você criará um gráfico de linha simples e adicionará um título centralizado, que é a posição padrão no Matplotlib.

## Criando um Jupyter Notebook

Após a inicialização da VM ser concluída, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o Jupyter Notebook.

![click-notebook](https://file.labex.io/images/click-notebook.png)

Você pode precisar esperar alguns segundos para que o Jupyter Notebook termine de carregar. Devido a limitações no Jupyter Notebook, a validação das operações não pode ser automatizada.

Se você encontrar algum problema durante o laboratório, sinta-se à vontade para pedir ajuda ao Labby. Por favor, forneça feedback após a sessão para que possamos resolver prontamente quaisquer problemas.

## Importando Matplotlib

Agora, vamos começar importando a biblioteca Matplotlib. Na primeira célula do seu notebook, digite o seguinte código e execute-o pressionando Shift+Enter:

```python
import matplotlib.pyplot as plt
```

Isso importa o módulo pyplot do Matplotlib e atribui a ele o alias `plt`, que é uma convenção comum.

## Criando um Gráfico Simples

Em seguida, vamos criar um gráfico de linha básico. Em uma nova célula, insira o seguinte código e execute-o:

```python
plt.figure(figsize=(8, 5))  # Create a figure with a specific size
plt.plot(range(10))         # Plot numbers from 0 to 9
plt.grid(True)              # Add a grid for better readability
plt.show()                  # Display the plot
```

Você deve ver um gráfico de linha simples com valores de 0 a 9 exibidos na saída.

![line-plot](../assets/screenshot-20250306-g5knGobR@2x.png)

## Adicionando um Título Padrão (Centralizado)

Agora, vamos adicionar um título ao nosso gráfico. A posição padrão para um título é centralizada ao longo da parte superior do gráfico. Em uma nova célula, insira o seguinte código:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('My First Matplotlib Plot')  # Add a centered title
plt.show()
```

![line-plot-with-title](../assets/screenshot-20250306-XMODABB2@2x.png)

Execute a célula e você deverá ver o gráfico com um título centralizado na parte superior.

A função `title()` sem nenhum parâmetro adicional colocará o título no centro, que é a posição padrão.
