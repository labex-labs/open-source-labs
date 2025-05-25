# Introdução

Este laboratório demonstra o efeito da escala do parâmetro de regularização ao utilizar Máquinas de Vetores de Suporte (SVMs) para classificação. Na classificação SVM, estamos interessados na minimização de risco para a equação:

```math
C \sum_{i=1, n} \mathcal{L} (f(x_i), y_i) + \Omega (w)
```

onde:

- `C` é usado para definir a quantidade de regularização
- `L` é uma função de perda das nossas amostras e dos nossos parâmetros do modelo.
- `Ω` é uma função de penalidade dos nossos parâmetros do modelo

## Dicas da VM

Após o arranque da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para a prática.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar o carregamento. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante a aprendizagem, não hesite em contactar o Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para si.
