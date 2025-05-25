# _Lifetimes_ Genéricos em Funções

Vamos escrever uma função que retorna a maior de duas _string slices_. Esta função receberá duas _string slices_ e retornará uma única _string slice_. Depois de implementarmos a função `longest`, o código na Listagem 10-19 deve imprimir `The longest string is abcd`.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {result}");
}
```

Listagem 10-19: Uma função `main` que chama a função `longest` para encontrar a maior de duas _string slices_

Observe que queremos que a função receba _string slices_, que são referências, em vez de _strings_, porque não queremos que a função `longest` assuma a propriedade de seus parâmetros. Consulte "String Slices como Parâmetros" para mais discussão sobre por que os parâmetros que usamos na Listagem 10-19 são os que queremos.

Se tentarmos implementar a função `longest` como mostrado na Listagem 10-20, ela não compilará.

Nome do arquivo: `src/main.rs`

```rust
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Listagem 10-20: Uma implementação da função `longest` que retorna a maior de duas _string slices_, mas ainda não compila

Em vez disso, obtemos o seguinte erro que fala sobre _lifetimes_:

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:9:33
  |
9 | fn longest(x: &str, y: &str) -> &str {
  |               ----     ----     ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but the signature does not say whether it is borrowed from `x` or `y`
help: consider introducing a named lifetime parameter
  |
9 | fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
  |           ++++     ++          ++          ++
```

O texto de ajuda revela que o tipo de retorno precisa de um parâmetro de _lifetime_ genérico, porque o Rust não pode dizer se a referência que está sendo retornada se refere a `x` ou `y`. Na verdade, nós também não sabemos, porque o bloco `if` no corpo desta função retorna uma referência a `x` e o bloco `else` retorna uma referência a `y`!

Quando estamos definindo esta função, não sabemos os valores concretos que serão passados para esta função, então não sabemos se o caso `if` ou o caso `else` serão executados. Também não sabemos os _lifetimes_ concretos das referências que serão passadas, então não podemos olhar para os escopos como fizemos nas Listagens 10-17 e 10-18 para determinar se a referência que retornamos sempre será válida. O _borrow checker_ também não pode determinar isso, porque não sabe como os _lifetimes_ de `x` e `y` se relacionam com o _lifetime_ do valor de retorno. Para corrigir este erro, adicionaremos parâmetros de _lifetime_ genéricos que definem a relação entre as referências para que o _borrow checker_ possa realizar sua análise.
