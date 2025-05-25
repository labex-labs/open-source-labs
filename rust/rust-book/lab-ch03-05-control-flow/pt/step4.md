# Usando `if` em uma Declaração `let`

Como `if` é uma expressão, podemos usá-la no lado direito de uma declaração `let` para atribuir o resultado a uma variável, como em Listing 3-2.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };

    println!("The value of number is: {number}");
}
```

Listing 3-2: Atribuindo o resultado de uma expressão `if` a uma variável

A variável `number` será vinculada a um valor com base no resultado da expressão `if`. Execute este código para ver o que acontece:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/branches`
The value of number is: 5
```

Lembre-se que blocos de código são avaliados com base na última expressão neles, e números por si só também são expressões. Neste caso, o valor de toda a expressão `if` depende de qual bloco de código é executado. Isso significa que os valores que têm o potencial de serem resultados de cada braço (arm) do `if` devem ser do mesmo tipo; em Listing 3-2, os resultados tanto do braço `if` quanto do braço `else` eram inteiros `i32`. Se os tipos não corresponderem, como no exemplo a seguir, obteremos um erro:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let condition = true;

    let number = if condition { 5 } else { "six" };

    println!("The value of number is: {number}");
}
```

Quando tentamos compilar este código, obteremos um erro. Os braços `if` e `else` têm tipos de valor incompatíveis, e Rust indica exatamente onde encontrar o problema no programa:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
error[E0308]: `if` and `else` have incompatible types
 --> src/main.rs:4:44
  |
4 |     let number = if condition { 5 } else { "six" };
  |                                 -          ^^^^^ expected integer, found
`&str`
  |                                 |
  |                                 expected because of this
```

A expressão no bloco `if` é avaliada como um inteiro, e a expressão no bloco `else` é avaliada como uma string. Isso não funcionará porque as variáveis devem ter um único tipo, e Rust precisa saber em tempo de compilação qual é o tipo da variável `number`, definitivamente. Saber o tipo de `number` permite que o compilador verifique se o tipo é válido em todos os lugares onde usamos `number`. Rust não seria capaz de fazer isso se o tipo de `number` fosse determinado apenas em tempo de execução; o compilador seria mais complexo e faria menos garantias sobre o código se tivesse que acompanhar múltiplos tipos hipotéticos para qualquer variável.
