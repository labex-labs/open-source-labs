# Sintaxe de Métodos

_Métodos_ são semelhantes a funções: nós os declaramos com a palavra-chave `fn` e um nome, eles podem ter parâmetros e um valor de retorno, e contêm algum código que é executado quando o método é chamado de outro lugar. Diferentemente das funções, os métodos são definidos dentro do contexto de uma struct (ou de um enum ou de um objeto trait, que abordaremos no Capítulo 6 e no Capítulo 17, respectivamente), e seu primeiro parâmetro é sempre `self`, que representa a instância da struct em que o método está sendo chamado.
