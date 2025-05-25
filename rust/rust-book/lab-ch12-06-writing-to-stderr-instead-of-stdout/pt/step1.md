# Escrevendo Mensagens de Erro para Saída de Erro Padrão em Vez de Saída Padrão

No momento, estamos escrevendo toda a nossa saída para o terminal usando a macro `println!`. Na maioria dos terminais, existem dois tipos de saída: _saída padrão_ (`stdout`) para informações gerais e _saída de erro padrão_ (`stderr`) para mensagens de erro. Essa distinção permite que os usuários escolham direcionar a saída bem-sucedida de um programa para um arquivo, mas ainda imprimir mensagens de erro na tela.

A macro `println!` é capaz apenas de imprimir na saída padrão, então temos que usar outra coisa para imprimir na saída de erro padrão.
