# Pensando em Termos de _Lifetimes_

A maneira como você precisa especificar os parâmetros de _lifetime_ depende do que sua função está fazendo. Por exemplo, se mudássemos a implementação da função `longest` para sempre retornar o primeiro parâmetro em vez do _string slice_ mais longo, não precisaríamos especificar um _lifetime_ no parâmetro `y`. O código a seguir compilará:

Nome do arquivo: `src/main.rs`

```rust
fn longest<'a>(x: &'a str, y: &str) -> &'a str {
    x
}
```

Especificamos um parâmetro de _lifetime_ `'a` para o parâmetro `x` e o tipo de retorno, mas não para o parâmetro `y`, porque o _lifetime_ de `y` não tem nenhuma relação com o _lifetime_ de `x` ou o valor de retorno.

Ao retornar uma referência de uma função, o parâmetro de _lifetime_ para o tipo de retorno precisa corresponder ao parâmetro de _lifetime_ para um dos parâmetros. Se a referência retornada _não_ se referir a um dos parâmetros, ela deve se referir a um valor criado dentro desta função. No entanto, esta seria uma referência pendente porque o valor sairá do escopo no final da função. Considere esta tentativa de implementação da função `longest` que não compilará:

Nome do arquivo: `src/main.rs`

```rust
fn longest<'a>(x: &str, y: &str) -> &'a str {
    let result = String::from("really long string");
    result.as_str()
}
```

Aqui, embora tenhamos especificado um parâmetro de _lifetime_ `'a` para o tipo de retorno, esta implementação não compilará porque o _lifetime_ do valor de retorno não está relacionado ao _lifetime_ dos parâmetros. Aqui está a mensagem de erro que recebemos:

```bash
error[E0515]: cannot return reference to local variable `result`
  --> src/main.rs:11:5
   |
11 |     result.as_str()
   |     ^^^^^^^^^^^^^^^ returns a reference to data owned by the
current function
```

O problema é que `result` sai do escopo e é limpo no final da função `longest`. Também estamos tentando retornar uma referência a `result` da função. Não há como especificar parâmetros de _lifetime_ que mudariam a referência pendente, e o Rust não nos permitirá criar uma referência pendente. Neste caso, a melhor solução seria retornar um tipo de dado _owned_ em vez de uma referência, para que a função de chamada seja então responsável por limpar o valor.

Em última análise, a sintaxe de _lifetime_ é sobre conectar os _lifetimes_ de vários parâmetros e valores de retorno de funções. Uma vez que eles estão conectados, o Rust tem informações suficientes para permitir operações seguras de memória e proibir operações que criariam ponteiros pendentes ou violariam a segurança da memória.
