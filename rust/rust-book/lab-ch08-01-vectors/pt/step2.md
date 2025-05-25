# Criando um Novo Vetor

Para criar um novo vetor vazio, chamamos a função `Vec::new`, como mostrado na Listagem 8-1.

```rust
let v: Vec<i32> = Vec::new();
```

Listagem 8-1: Criando um novo vetor vazio para armazenar valores do tipo `i32`

Observe que adicionamos uma anotação de tipo aqui. Como não estamos inserindo nenhum valor neste vetor, o Rust não sabe que tipo de elementos pretendemos armazenar. Este é um ponto importante. Vetores são implementados usando genéricos; abordaremos como usar genéricos com seus próprios tipos no Capítulo 10. Por enquanto, saiba que o tipo `Vec<T>` fornecido pela biblioteca padrão pode conter qualquer tipo. Quando criamos um vetor para conter um tipo específico, podemos especificar o tipo dentro de colchetes angulares. Na Listagem 8-1, dissemos ao Rust que o `Vec<T>` em `v` conterá elementos do tipo `i32`.

Mais frequentemente, você criará um `Vec<T>` com valores iniciais e o Rust inferirá o tipo de valor que você deseja armazenar, então você raramente precisará fazer essa anotação de tipo. O Rust convenientemente fornece a macro `vec!`, que criará um novo vetor que contém os valores que você fornecer. A Listagem 8-2 cria um novo `Vec<i32>` que contém os valores `1`, `2` e `3`. O tipo inteiro é `i32` porque esse é o tipo inteiro padrão, como discutimos em "Tipos de Dados".

```rust
let v = vec![1, 2, 3];
```

Listagem 8-2: Criando um novo vetor contendo valores

Como fornecemos valores `i32` iniciais, o Rust pode inferir que o tipo de `v` é `Vec<i32>`, e a anotação de tipo não é necessária. Em seguida, veremos como modificar um vetor.
