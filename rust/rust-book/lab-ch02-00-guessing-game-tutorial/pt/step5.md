# Recebendo a Entrada do Usuário

Lembre-se de que incluímos a funcionalidade de entrada/saída da biblioteca padrão com `use std::io;` na primeira linha do programa. Agora, chamaremos a função `stdin` do módulo `io`, o que nos permitirá lidar com a entrada do usuário:

```rust
io::stdin()
    .read_line(&mut guess)
```

Se não tivéssemos importado a biblioteca `io` com `use std::io;` no início do programa, ainda poderíamos usar a função escrevendo esta chamada de função como `std::io::stdin`. A função `stdin` retorna uma instância de `std::io::Stdin`, que é um tipo que representa um manipulador para a entrada padrão do seu terminal.

Em seguida, a linha `.read_line(&mut guess)` chama o método `read_line` no manipulador de entrada padrão para obter a entrada do usuário. Também estamos passando `&mut guess` como o argumento para `read_line` para dizer a ele em qual string armazenar a entrada do usuário. O trabalho completo de `read_line` é pegar o que o usuário digita na entrada padrão e anexá-lo a uma string (sem substituir seu conteúdo), então, portanto, passamos essa string como um argumento. O argumento da string precisa ser mutável para que o método possa alterar o conteúdo da string.

O `&` indica que este argumento é uma _referência_ (reference), que oferece uma maneira de permitir que várias partes do seu código acessem um pedaço de dados sem precisar copiar esses dados na memória várias vezes. Referências são um recurso complexo, e uma das principais vantagens do Rust é como é seguro e fácil usar referências. Você não precisa saber muitos desses detalhes para concluir este programa. Por enquanto, tudo o que você precisa saber é que, como as variáveis, as referências são imutáveis por padrão. Portanto, você precisa escrever `&mut guess` em vez de `&guess` para torná-lo mutável. (O Capítulo 4 explicará as referências com mais detalhes.)
