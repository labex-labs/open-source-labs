# Funções

Ignorando \[elision\], as assinaturas de funções com _lifetimes_ têm algumas restrições:

- qualquer referência _deve_ ter um _lifetime_ anotado.
- qualquer referência que está sendo retornada _deve_ ter o mesmo _lifetime_ de uma entrada ou ser `static`.

Adicionalmente, note que retornar referências sem entrada é proibido se isso resultar em retornar referências a dados inválidos. O exemplo a seguir mostra algumas formas válidas de funções com _lifetimes_:

```rust
// Uma referência de entrada com lifetime `'a` que deve viver
// pelo menos tanto tempo quanto a função.
fn print_one<'a>(x: &'a i32) {
    println!("`print_one`: x is {}", x);
}

// Referências mutáveis também são possíveis com lifetimes.
fn add_one<'a>(x: &'a mut i32) {
    *x += 1;
}

// Múltiplos elementos com diferentes lifetimes. Neste caso, seria
// aceitável que ambos tivessem o mesmo lifetime `'a`, mas
// em casos mais complexos, diferentes lifetimes podem ser necessários.
fn print_multi<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("`print_multi`: x is {}, y is {}", x, y);
}

// Retornar referências que foram passadas como entrada é aceitável.
// No entanto, o lifetime correto deve ser retornado.
fn pass_x<'a, 'b>(x: &'a i32, _: &'b i32) -> &'a i32 { x }

//fn invalid_output<'a>() -> &'a String { &String::from("foo") }
// O acima é inválido: `'a` deve viver mais tempo que a função.
// Aqui, `&String::from("foo")` criaria uma `String`, seguido por uma
// referência. Então os dados são descartados ao sair do escopo, deixando
// uma referência a dados inválidos para serem retornados.

fn main() {
    let x = 7;
    let y = 9;

    print_one(&x);
    print_multi(&x, &y);

    let z = pass_x(&x, &y);
    print_one(z);

    let mut t = 3;
    add_one(&mut t);
    print_one(&t);
}
```
