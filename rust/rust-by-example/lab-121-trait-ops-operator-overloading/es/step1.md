# Sobrecarga de operadores

En Rust, muchos de los operadores se pueden sobrecargar a través de traits. Es decir, algunos operadores se pueden utilizar para realizar diferentes tareas según sus argumentos de entrada. Esto es posible porque los operadores son azúcar sintáctico para las llamadas de método. Por ejemplo, el operador `+` en `a + b` llama al método `add` (como en `a.add(b)`). Este método `add` es parte del trait `Add`. Por lo tanto, el operador `+` puede ser utilizado por cualquier implementador del trait `Add`.

Se puede encontrar una lista de los traits, como `Add`, que sobrecargan operadores en `core::ops`.

```rust
use std::ops;

struct Foo;
struct Bar;

#[derive(Debug)]
struct FooBar;

#[derive(Debug)]
struct BarFoo;

// El trait `std::ops::Add` se utiliza para especificar la funcionalidad de `+`.
// Aquí, hacemos `Add<Bar>` - el trait para la adición con un lado derecho de tipo `Bar`.
// El siguiente bloque implementa la operación: Foo + Bar = FooBar
impl ops::Add<Bar> for Foo {
    type Output = FooBar;

    fn add(self, _rhs: Bar) -> FooBar {
        println!("> Foo.add(Bar) fue llamado");

        FooBar
    }
}

// Al invertir los tipos, terminamos implementando una adición no conmutativa.
// Aquí, hacemos `Add<Foo>` - el trait para la adición con un lado derecho de tipo `Foo`.
// Este bloque implementa la operación: Bar + Foo = BarFoo
impl ops::Add<Foo> for Bar {
    type Output = BarFoo;

    fn add(self, _rhs: Foo) -> BarFoo {
        println!("> Bar.add(Foo) fue llamado");

        BarFoo
    }
}

fn main() {
    println!("Foo + Bar = {:?}", Foo + Bar);
    println!("Bar + Foo = {:?}", Bar + Foo);
}
```
