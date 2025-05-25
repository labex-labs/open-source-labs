# Desenvolvimento Orientado a Testes (TDD)

Agora que extraímos a lógica para `src/lib.rs` e deixamos a coleta de argumentos e o tratamento de erros em `src/main.rs`, é muito mais fácil escrever testes para a funcionalidade principal do nosso código. Podemos chamar funções diretamente com vários argumentos e verificar os valores de retorno sem ter que chamar nosso binário a partir da linha de comando.

Nesta seção, adicionaremos a lógica de busca ao programa `minigrep` usando o processo de Desenvolvimento Orientado a Testes (TDD) com as seguintes etapas:

1.  Escreva um teste que falhe e execute-o para garantir que ele falhe pela razão que você espera.
2.  Escreva ou modifique código suficiente para fazer o novo teste passar.
3.  Refatore o código que você acabou de adicionar ou alterar e certifique-se de que os testes continuem passando.
4.  Repita a partir da etapa 1!

Embora seja apenas uma das muitas maneiras de escrever software, o TDD pode ajudar a impulsionar o design do código. Escrever o teste antes de escrever o código que faz o teste passar ajuda a manter uma alta cobertura de testes durante todo o processo.

Vamos testar a implementação da funcionalidade que realmente fará a busca pela string de consulta no conteúdo do arquivo e produzir uma lista de linhas que correspondem à consulta. Adicionaremos essa funcionalidade em uma função chamada `search`.
