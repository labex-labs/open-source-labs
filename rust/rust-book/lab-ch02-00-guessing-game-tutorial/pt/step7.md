# Imprimindo Valores com Placeholders println!

Além da chave de fechamento, há apenas mais uma linha para discutir no código até agora:

```rust
println!("You guessed: {guess}");
```

Esta linha imprime a string que agora contém a entrada do usuário. O conjunto de chaves `{}` é um placeholder (espaço reservado): pense em `{}` como pequenas pinças de caranguejo que seguram um valor no lugar. Ao imprimir o valor de uma variável, o nome da variável pode ir dentro das chaves. Ao imprimir o resultado da avaliação de uma expressão, coloque chaves vazias na string de formato e, em seguida, siga a string de formato com uma lista separada por vírgulas de expressões para imprimir em cada placeholder de chave vazio na mesma ordem. Imprimir uma variável e o resultado de uma expressão em uma chamada para `println!` ficaria assim:

```rust
let x = 5;
let y = 10;

println!("x = {x} and y + 2 = {}", y + 2);
```

Este código imprimiria `x = 5 and y = 12`.
