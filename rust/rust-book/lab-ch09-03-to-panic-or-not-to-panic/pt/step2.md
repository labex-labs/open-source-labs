# Exemplos, Código Protótipo e Testes

Ao escrever um exemplo para ilustrar algum conceito, incluir também código robusto de tratamento de erros pode tornar o exemplo menos claro. Em exemplos, entende-se que uma chamada a um método como `unwrap` que pode entrar em pânico é pretendida como um espaço reservado para a maneira como você gostaria que seu aplicativo lidasse com erros, o que pode diferir com base no que o restante do seu código está fazendo.

Da mesma forma, os métodos `unwrap` e `expect` são muito úteis ao prototipar, antes de estar pronto para decidir como lidar com erros. Eles deixam marcadores claros em seu código para quando você estiver pronto para tornar seu programa mais robusto.

Se uma chamada de método falhar em um teste, você gostaria que todo o teste falhasse, mesmo que esse método não seja a funcionalidade em teste. Como `panic!` é a maneira como um teste é marcado como uma falha, chamar `unwrap` ou `expect` é exatamente o que deve acontecer.
