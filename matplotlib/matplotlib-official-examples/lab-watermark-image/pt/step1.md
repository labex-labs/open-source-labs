# Criando um Jupyter Notebook e Importando as Bibliotecas Necessárias

Na primeira célula do seu notebook, insira o seguinte código para importar as bibliotecas necessárias:

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
```

Vamos entender o que cada uma destas bibliotecas faz:

- `matplotlib.pyplot` (apelidado como `plt`): Uma coleção de funções que fazem o matplotlib funcionar como o MATLAB, fornecendo uma interface conveniente para criar gráficos.
- `numpy` (apelidado como `np`): Um pacote fundamental para computação científica em Python, que usaremos para manipulação de dados.
- `matplotlib.cbook`: Uma coleção de funções utilitárias para matplotlib, incluindo funções para obter dados de exemplo.
- `matplotlib.image`: Um módulo para funcionalidades relacionadas a imagens no matplotlib, que usaremos para ler e exibir imagens.

Execute a célula clicando no botão "Run" na parte superior do notebook ou pressionando Shift+Enter.

![libraries-imported](../assets/screenshot-20250306-18gJ6FRZ@2x.png)

A execução desta célula deve ser concluída sem qualquer saída, indicando que todas as bibliotecas foram importadas com sucesso.
