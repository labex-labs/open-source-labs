# Criando uma Nova String

Muitas das mesmas operações disponíveis com `Vec<T>` também estão disponíveis com `String`, porque `String` é realmente implementado como um wrapper em torno de um vetor de bytes com algumas garantias, restrições e capacidades extras. Um exemplo de uma função que funciona da mesma forma com `Vec<T>` e `String` é a função `new` para criar uma instância, mostrada na Listagem 8-11.

```rust
let mut s = String::new();
```

Listagem 8-11: Criando uma nova `String` vazia

Esta linha cria uma nova string vazia chamada `s`, na qual podemos então carregar dados. Frequentemente, teremos alguns dados iniciais com os quais queremos começar a string. Para isso, usamos o método `to_string`, que está disponível em qualquer tipo que implemente o trait `Display`, como os literais de string fazem. A Listagem 8-12 mostra dois exemplos.

```rust
let data = "initial contents";

let s = data.to_string();

// the method also works on a literal directly:
let s = "initial contents".to_string();
```

Listagem 8-12: Usando o método `to_string` para criar uma `String` a partir de um literal de string

Este código cria uma string contendo `initial contents`.

Também podemos usar a função `String::from` para criar uma `String` a partir de um literal de string. O código na Listagem 8-13 é equivalente ao código na Listagem 8-12 que usa `to_string`.

```rust
let s = String::from("initial contents");
```

Listagem 8-13: Usando a função `String::from` para criar uma `String` a partir de um literal de string

Como as strings são usadas para tantas coisas, podemos usar muitas APIs genéricas diferentes para strings, fornecendo-nos muitas opções. Algumas delas podem parecer redundantes, mas todas têm seu lugar! Neste caso, `String::from` e `to_string` fazem a mesma coisa, então qual você escolhe é uma questão de estilo e legibilidade.

Lembre-se que as strings são codificadas em UTF-8, então podemos incluir quaisquer dados devidamente codificados nelas, como mostrado na Listagem 8-14.

```rust
let hello = String::from("السلام عليكم");
let hello = String::from("Dobrý den");
let hello = String::from("Hello");
let hello = String::from("שָׁלוֹם");
let hello = String::from("नमस्ते");
let hello = String::from("こんにちは");
let hello = String::from("안녕하세요");
let hello = String::from("你好");
let hello = String::from("Olá");
let hello = String::from("Здравствуйте");
let hello = String::from("Hola");
```

Listagem 8-14: Armazenando saudações em diferentes idiomas em strings

Todos estes são valores `String` válidos.
