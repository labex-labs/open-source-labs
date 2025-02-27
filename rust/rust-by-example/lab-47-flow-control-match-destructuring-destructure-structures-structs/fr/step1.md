# structs

De même, un `struct` peut être déstructuré comme suit :

```rust
fn main() {
    struct Foo {
        x: (u32, u32),
        y: u32,
    }

    // Essayez de modifier les valeurs dans le struct pour voir ce qui se passe
    let foo = Foo { x: (1, 2), y: 3 };

    match foo {
        Foo { x: (1, b), y } => println!("Le premier de x est 1, b = {},  y = {} ", b, y),

        // vous pouvez déstructurer des structs et renommer les variables,
        // l'ordre n'est pas important
        Foo { y: 2, x: i } => println!("y est 2, i = {:?}", i),

        // et vous pouvez également ignorer certaines variables :
        Foo { y,.. } => println!("y = {}, on n'a pas besoin de x", y),
        // cela générera une erreur : le motif ne mentionne pas le champ `x`
        //Foo { y } => println!("y = {}", y),
    }

    let faa = Foo { x: (1, 2), y: 3 };

    // Vous n'avez pas besoin d'un bloc match pour déstructurer des structs :
    let Foo { x : x0, y: y0 } = faa;
    println!("En dehors : x0 = {x0:?}, y0 = {y0}");
}
```
