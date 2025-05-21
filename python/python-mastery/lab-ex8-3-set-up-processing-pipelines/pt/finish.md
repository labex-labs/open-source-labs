# Resumo

Neste laboratório, você aprendeu como usar corrotinas para construir pipelines de processamento de dados em Python. Os principais conceitos incluem a compreensão dos fundamentos das corrotinas, como elas operam, a necessidade de _priming_ (inicialização) e o uso de decoradores para inicialização. Você também explorou o fluxo de dados, empurrando dados por meio de um pipeline via o método `send()`, diferente do modelo "pull" (puxar) do gerador.

Além disso, você criou corrotinas especializadas para tarefas como análise de dados CSV, filtragem de registros e formatação de saída. Você aprendeu a compor pipelines conectando múltiplas corrotinas e implementou operações de filtragem e transformação. As corrotinas oferecem uma abordagem poderosa para o processamento de dados em streaming, permitindo uma separação limpa de preocupações e fácil modificação de estágios individuais.
