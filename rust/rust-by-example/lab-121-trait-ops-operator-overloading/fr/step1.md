# Surchargement d'opérateurs

En Rust, de nombreux opérateurs peuvent être surchargés via des traits. C'est-à-dire que certains opérateurs peuvent être utilisés pour accomplir différentes tâches en fonction de leurs arguments d'entrée. Cela est possible car les opérateurs sont du sucre syntaxique pour les appels de méthodes. Par exemple, l'opérateur `+` dans `a + b` appelle la méthode `add` (comme dans `a.add(b)`). Cette méthode `add` est partie du trait `Add`. Par conséquent, l'opérateur `+` peut être utilisé par tout implémentateur du trait `Add`.

Une liste des traits, tels que `Add`, qui surchargent les opérateurs peut être trouvée dans `core::ops`.

```rust
use std::ops;

struct Foo;
struct Bar;

#[derive(Debug)]
struct FooBar;

#[derive(Debug)]
struct BarFoo;

// Le trait `std::ops::Add` est utilisé pour spécifier la fonctionnalité de `+`.
// Ici, nous définissons `Add<Bar>` - le trait pour l'addition avec un opérande droit de type `Bar`.
// Le bloc suivant implémente l'opération : Foo + Bar = FooBar
impl ops::Add<Bar> for Foo {
    type Output = FooBar;

    fn add(self, _rhs: Bar) -> FooBar {
        println!("> Foo.add(Bar) a été appelé");

        FooBar
    }
}

// En inversant les types, nous finissons par implémenter une addition non commutative.
// Ici, nous définissons `Add<Foo>` - le trait pour l'addition avec un opérande droit de type `Foo`.
// Ce bloc implémente l'opération : Bar + Foo = BarFoo
impl ops::Add<Foo> for Bar {
    type Output = BarFoo;

    fn add(self, _rhs: Foo) -> BarFoo {
        println!("> Bar.add(Foo) a été appelé");

        BarFoo
    }
}

fn main() {
    println!("Foo + Bar = {:?}", Foo + Bar);
    println!("Bar + Foo = {:?}", Bar + Foo);
}
```
