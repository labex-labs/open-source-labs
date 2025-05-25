# Introdução

Este laboratório apresenta o desempate SVM e seu efeito na fronteira de decisão. No SVM, o desempate é o mecanismo usado para resolver conflitos entre duas ou mais classes quando suas distâncias são iguais. Ele não está habilitado por padrão quando `decision_function_shape='ovr'` porque é custoso. Portanto, este laboratório ilustra o efeito do parâmetro `break_ties` para um problema de classificação multiclasse e `decision_function_shape='ovr'`.

## Dicas da Máquina Virtual

Após o início da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão e resolveremos o problema rapidamente para você.
