# A Diferença Entre Macros e Funções

Fundamentalmente, macros são uma forma de escrever código que escreve outro código, o que é conhecido como _metaprogramação_ (metaprogramming). No Apêndice C, discutimos o atributo `derive`, que gera uma implementação de vários traits para você. Também usamos as macros `println!` e `vec!` ao longo do livro. Todas essas macros _expandem-se_ para produzir mais código do que o código que você escreveu manualmente.

A metaprogramação é útil para reduzir a quantidade de código que você precisa escrever e manter, que também é um dos papéis das funções. No entanto, as macros têm alguns poderes adicionais que as funções não têm.

Uma assinatura de função deve declarar o número e o tipo de parâmetros que a função possui. Macros, por outro lado, podem receber um número variável de parâmetros: podemos chamar `println!("hello")` com um argumento ou `println!("hello {}", name)` com dois argumentos. Além disso, as macros são expandidas antes que o compilador interprete o significado do código, então uma macro pode, por exemplo, implementar um trait em um determinado tipo. Uma função não pode, porque ela é chamada em tempo de execução e um trait precisa ser implementado em tempo de compilação.

A desvantagem de implementar uma macro em vez de uma função é que as definições de macro são mais complexas do que as definições de função, porque você está escrevendo código Rust que escreve código Rust. Devido a essa indireção, as definições de macro são geralmente mais difíceis de ler, entender e manter do que as definições de função.

Outra diferença importante entre macros e funções é que você deve definir macros ou trazê-las para o escopo _antes_ de chamá-las em um arquivo, em oposição às funções que você pode definir em qualquer lugar e chamar em qualquer lugar.
