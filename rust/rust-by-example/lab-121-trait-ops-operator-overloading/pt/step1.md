# Sobrecarga de Operadores

Em Rust, muitos dos operadores podem ser sobrecarregados via traits. Ou seja, alguns operadores podem ser usados para realizar diferentes tarefas com base em seus argumentos de entrada. Isso é possível porque os operadores são açúcar sintático (syntactic sugar) para chamadas de métodos. Por exemplo, o operador `+` em `a + b` chama o método `add` (como em `a.add(b)`). Este método `add` faz parte da trait `Add`. Portanto, o operador `+` pode ser usado por qualquer implementador da trait `Add`.

Uma lista das traits, como `Add`, que sobrecarregam operadores pode ser encontrada em `core::ops`.

```rust
use std::ops;

struct Foo;
struct Bar;

#[derive(Debug)]
struct FooBar;

#[derive(Debug)]
struct BarFoo;

// A trait `std::ops::Add` é usada para especificar a funcionalidade de `+`.
// Aqui, fazemos `Add<Bar>` - a trait para adição com um RHS do tipo `Bar`.
// O bloco a seguir implementa a operação: Foo + Bar = FooBar
impl ops::Add<Bar> for Foo {
    type Output = FooBar;

    fn add(self, _rhs: Bar) -> FooBar {
        println!("> Foo.add(Bar) was called");

        FooBar
    }
}

// Ao inverter os tipos, acabamos implementando uma adição não comutativa.
// Aqui, fazemos `Add<Foo>` - a trait para adição com um RHS do tipo `Foo`.
// Este bloco implementa a operação: Bar + Foo = BarFoo
impl ops::Add<Foo> for Bar {
    type Output = BarFoo;

    fn add(self, _rhs: Foo) -> BarFoo {
        println!("> Bar.add(Foo) was called");

        BarFoo
    }
}

fn main() {
    println!("Foo + Bar = {:?}", Foo + Bar);
    println!("Bar + Foo = {:?}", Bar + Foo);
}
```
