# Operatorüberladung

In Rust können viele Operatoren über die Verwendung von Traits überladen werden. Das heißt, einige Operatoren können verwendet werden, um unterschiedliche Aufgaben basierend auf ihren Eingabeargumenten zu erledigen. Dies ist möglich, da Operatoren syntaktischer Zucker für Methodenaufrufe sind. Beispielsweise ruft der `+`-Operator in `a + b` die `add`-Methode auf (wie in `a.add(b)`). Diese `add`-Methode ist Teil des `Add`-Traits. Folglich kann der `+`-Operator von jedem Implementierer des `Add`-Traits verwendet werden.

Eine Liste der Traits, wie `Add`, die Operatoren überladen, kann in `core::ops` gefunden werden.

```rust
use std::ops;

struct Foo;
struct Bar;

#[derive(Debug)]
struct FooBar;

#[derive(Debug)]
struct BarFoo;

// Das `std::ops::Add`-Trait wird verwendet, um die Funktionalität von `+` anzugeben.
// Hier definieren wir `Add<Bar>` - das Trait für die Addition mit einem rechten Operanden vom Typ `Bar`.
// Der folgende Block implementiert die Operation: Foo + Bar = FooBar
impl ops::Add<Bar> for Foo {
    type Output = FooBar;

    fn add(self, _rhs: Bar) -> FooBar {
        println!("> Foo.add(Bar) wurde aufgerufen");

        FooBar
    }
}

// Indem wir die Typen umkehren, implementieren wir eine nicht-kommutative Addition.
// Hier definieren wir `Add<Foo>` - das Trait für die Addition mit einem rechten Operanden vom Typ `Foo`.
// Dieser Block implementiert die Operation: Bar + Foo = BarFoo
impl ops::Add<Foo> for Bar {
    type Output = BarFoo;

    fn add(self, _rhs: Foo) -> BarFoo {
        println!("> Bar.add(Foo) wurde aufgerufen");

        BarFoo
    }
}

fn main() {
    println!("Foo + Bar = {:?}", Foo + Bar);
    println!("Bar + Foo = {:?}", Bar + Foo);
}
```
