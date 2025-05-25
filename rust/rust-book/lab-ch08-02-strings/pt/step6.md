# Concatenação com o operador + ou a macro format!

Frequentemente, você vai querer combinar duas strings existentes. Uma maneira de fazer isso é usar o operador `+`, como mostrado na Listagem 8-18.

```rust
let s1 = String::from("Hello, ");
let s2 = String::from("world!");
let s3 = s1 + &s2; // note s1 has been moved here and can no longer be used
```

Listagem 8-18: Usando o operador `+` para combinar dois valores `String` em um novo valor `String`

A string `s3` conterá `Hello, world!`. A razão pela qual `s1` não é mais válido após a adição, e a razão pela qual usamos uma referência a `s2`, tem a ver com a assinatura do método que é chamado quando usamos o operador `+`. O operador `+` usa o método `add`, cuja assinatura se parece com isto:

```rust
fn add(self, s: &str) -> String {
```

Na biblioteca padrão, você verá `add` definido usando genéricos e tipos associados. Aqui, substituímos tipos concretos, que é o que acontece quando chamamos este método com valores `String`. Discutiremos genéricos no Capítulo 10. Esta assinatura nos dá as pistas que precisamos para entender as partes complicadas do operador `+`.

Primeiro, `s2` tem um `&`, significando que estamos adicionando uma _referência_ da segunda string à primeira string. Isso ocorre por causa do parâmetro `s` na função `add`: só podemos adicionar um `&str` a uma `String`; não podemos adicionar dois valores `String` juntos. Mas espere---o tipo de `&s2` é `&String`, não `&str`, como especificado no segundo parâmetro para `add`. Então, por que a Listagem 8-18 compila?

A razão pela qual podemos usar `&s2` na chamada para `add` é que o compilador pode _coagir_ o argumento `&String` em um `&str`. Quando chamamos o método `add`, Rust usa uma _coerção deref_, que aqui transforma `&s2` em `&s2[..]`. Discutiremos a coerção deref com mais profundidade no Capítulo 15. Como `add` não assume a propriedade do parâmetro `s`, `s2` ainda será uma `String` válida após esta operação.

Segundo, podemos ver na assinatura que `add` assume a propriedade de `self` porque `self` _não_ tem um `&`. Isso significa que `s1` na Listagem 8-18 será movido para a chamada `add` e não será mais válido depois disso. Então, embora `let s3 = s1 + &s2;` pareça que vai copiar ambas as strings e criar uma nova, esta instrução na verdade assume a propriedade de `s1`, anexa uma cópia do conteúdo de `s2` e então retorna a propriedade do resultado. Em outras palavras, parece que está fazendo muitas cópias, mas não está; a implementação é mais eficiente do que copiar.

Se precisarmos concatenar múltiplas strings, o comportamento do operador `+` se torna complicado:

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = s1 + "-" + &s2 + "-" + &s3;
```

Neste ponto, `s` será `tic-tac-toe`. Com todos os caracteres `+` e `"`, é difícil ver o que está acontecendo. Para combinar strings de maneiras mais complicadas, podemos, em vez disso, usar a macro `format!`:

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = format!("{s1}-{s2}-{s3}");
```

Este código também define `s` como `tic-tac-toe`. A macro `format!` funciona como `println!`, mas em vez de imprimir a saída na tela, ela retorna uma `String` com o conteúdo. A versão do código usando `format!` é muito mais fácil de ler, e o código gerado pela macro `format!` usa referências para que esta chamada não assuma a propriedade de nenhum de seus parâmetros.
