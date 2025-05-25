# Parâmetros de Função

Parâmetros de função também podem ser padrões. O código na Listagem 18-6, que declara uma função chamada `foo` que recebe um parâmetro chamado `x` do tipo `i32`, deve agora parecer familiar.

```rust
fn foo(x: i32) {
    // code goes here
}
```

Listagem 18-6: Uma assinatura de função usando padrões nos parâmetros

A parte `x` é um padrão! Como fizemos com `let`, poderíamos corresponder uma tupla nos argumentos de uma função ao padrão. A Listagem 18-7 divide os valores em uma tupla ao passá-la para uma função.

Nome do arquivo: `src/main.rs`

```rust
fn print_coordinates(&(x, y): &(i32, i32)) {
    println!("Current location: ({x}, {y})");
}

fn main() {
    let point = (3, 5);
    print_coordinates(&point);
}
```

Listagem 18-7: Uma função com parâmetros que desestruturam uma tupla

Este código imprime `Current location: (3, 5)`. Os valores `&(3, 5)` correspondem ao padrão `&(x, y)`, então `x` é o valor `3` e `y` é o valor `5`.

Também podemos usar padrões em listas de parâmetros de closure da mesma forma que nas listas de parâmetros de função, porque closures são semelhantes a funções, como discutido no Capítulo 13.

Neste ponto, você viu várias maneiras de usar padrões, mas os padrões não funcionam da mesma forma em todos os lugares onde podemos usá-los. Em alguns lugares, os padrões devem ser irrefutáveis; em outras circunstâncias, eles podem ser refutáveis. Discutiremos esses dois conceitos a seguir.
