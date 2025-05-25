# @ Bindings

O operador _at_ `@` nos permite criar uma variável que contém um valor ao mesmo tempo em que testamos esse valor para uma correspondência de padrão. Na Listagem 18-29, queremos testar se um campo `id` de `Message::Hello` está dentro do intervalo `3..=7`. Também queremos vincular o valor à variável `id_variable` para que possamos usá-lo no código associado ao braço. Poderíamos nomear essa variável `id`, a mesma do campo, mas para este exemplo usaremos um nome diferente.

Nome do arquivo: `src/main.rs`

```rust
enum Message {
    Hello { id: i32 },
}

let msg = Message::Hello { id: 5 };

match msg {
    Message::Hello {
        id: id_variable @ 3..=7,
    } => println!("Found an id in range: {id_variable}"),
    Message::Hello { id: 10..=12 } => {
        println!("Found an id in another range")
    }
    Message::Hello { id } => println!("Some other id: {id}"),
}
```

Listagem 18-29: Usando `@` para vincular a um valor em um padrão enquanto também o testa

Este exemplo imprimirá `Found an id in range: 5`. Ao especificar `id_variable @` antes do intervalo `3..=7`, estamos capturando qualquer valor que corresponda ao intervalo, ao mesmo tempo em que testamos se o valor corresponde ao padrão do intervalo.

No segundo braço, onde temos apenas um intervalo especificado no padrão, o código associado ao braço não tem uma variável que contenha o valor real do campo `id`. O valor do campo `id` poderia ter sido 10, 11 ou 12, mas o código que acompanha esse padrão não sabe qual é. O código do padrão não é capaz de usar o valor do campo `id` porque não salvamos o valor `id` em uma variável.

No último braço, onde especificamos uma variável sem um intervalo, temos o valor disponível para usar no código do braço em uma variável chamada `id`. A razão é que usamos a sintaxe abreviada do campo da struct. Mas não aplicamos nenhum teste ao valor no campo `id` neste braço, como fizemos com os dois primeiros braços: qualquer valor corresponderia a este padrão.

Usar `@` nos permite testar um valor e salvá-lo em uma variável dentro de um padrão.
