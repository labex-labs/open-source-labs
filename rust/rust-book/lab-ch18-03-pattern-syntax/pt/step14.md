# Uma Variável Não Utilizada Começando Seu Nome com \_

Se você criar uma variável, mas não usá-la em nenhum lugar, o Rust geralmente emitirá um aviso porque uma variável não utilizada pode ser um bug. No entanto, às vezes é útil poder criar uma variável que você não usará ainda, como quando você está prototipando ou apenas começando um projeto. Nessa situação, você pode dizer ao Rust para não avisá-lo sobre a variável não utilizada, começando o nome da variável com um sublinhado. Na Listagem 18-20, criamos duas variáveis não utilizadas, mas quando compilamos este código, devemos receber apenas um aviso sobre uma delas.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let _x = 5;
    let y = 10;
}
```

Listagem 18-20: Começando o nome de uma variável com um sublinhado para evitar receber avisos de variável não utilizada

Aqui, recebemos um aviso sobre não usar a variável `y`, mas não recebemos um aviso sobre não usar `_x`.

Observe que há uma diferença sutil entre usar apenas `_` e usar um nome que começa com um sublinhado. A sintaxe `_x` ainda vincula o valor à variável, enquanto `_` não vincula de forma alguma. Para mostrar um caso em que essa distinção importa, a Listagem 18-21 nos fornecerá um erro.

Nome do arquivo: `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_s) = s {
    println!("found a string");
}

println!("{:?}", s);
```

Listagem 18-21: Uma variável não utilizada começando com um sublinhado ainda vincula o valor, o que pode assumir a propriedade do valor.

Receberemos um erro porque o valor `s` ainda será movido para `_s`, o que nos impede de usar `s` novamente. No entanto, usar o sublinhado por si só nunca se vincula ao valor. A Listagem 18-22 compilará sem nenhum erro porque `s` não é movido para `_`.

Nome do arquivo: `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_) = s {
    println!("found a string");
}

println!("{:?}", s);
```

Listagem 18-22: Usar um sublinhado não vincula o valor.

Este código funciona perfeitamente porque nunca vinculamos `s` a nada; ele não é movido.
