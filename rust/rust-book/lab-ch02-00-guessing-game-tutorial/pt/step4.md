# Armazenando Valores com Variáveis

Em seguida, criaremos uma _variável_ para armazenar a entrada do usuário, assim:

```rust
let mut guess = String::new();
```

Agora o programa está ficando interessante! Há muita coisa acontecendo nesta pequena linha. Usamos a declaração `let` para criar a variável. Aqui está outro exemplo:

```rust
let apples = 5;
```

Esta linha cria uma nova variável chamada `apples` e a vincula ao valor 5. Em Rust, as variáveis são imutáveis por padrão, o que significa que, uma vez que damos um valor à variável, o valor não mudará. Discutiremos este conceito em detalhes em "Variáveis e Mutabilidade". Para tornar uma variável mutável, adicionamos `mut` antes do nome da variável:

```rust
let apples = 5; // immutable
let mut bananas = 5; // mutable
```

> Nota: A sintaxe `//` inicia um comentário que continua até o final da linha. Rust ignora tudo nos comentários. Discutiremos os comentários com mais detalhes no Capítulo 3.

Voltando ao programa do jogo de adivinhação, você agora sabe que `let mut guess` introduzirá uma variável mutável chamada `guess`. O sinal de igual (`=`) diz ao Rust que queremos vincular algo à variável agora. À direita do sinal de igual está o valor ao qual `guess` está vinculado, que é o resultado da chamada `String::new`, uma função que retorna uma nova instância de `String`. `String` é um tipo de string fornecido pela biblioteca padrão que é um pedaço de texto UTF-8 codificado e expansível.

A sintaxe `::` na linha `::new` indica que `new` é uma função associada do tipo `String`. Uma _função associada_ é uma função que é implementada em um tipo, neste caso `String`. Esta função `new` cria uma nova string vazia. Você encontrará uma função `new` em muitos tipos porque é um nome comum para uma função que cria um novo valor de algum tipo.

Em suma, a linha `let mut guess = String::new();` criou uma variável mutável que está atualmente vinculada a uma nova instância vazia de `String`. Ufa!
