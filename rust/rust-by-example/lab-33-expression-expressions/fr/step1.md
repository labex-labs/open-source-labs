# Expressions

Un programme Rust est (en majeure partie) composé d'une série d'instructions :

```rust
fn main() {
    // instruction
    // instruction
    // instruction
}
```

Il existe plusieurs types d'instructions en Rust. Les deux plus courants sont la déclaration d'une liaison de variable et l'utilisation d'un `;` avec une expression :

```rust
fn main() {
    // liaison de variable
    let x = 5;

    // expression;
    x;
    x + 1;
    15;
}
```

Les blocs sont également des expressions, donc ils peuvent être utilisés comme valeurs dans des affectations. La dernière expression dans le bloc sera assignée à l'endroit de l'expression, tel qu'une variable locale. Cependant, si la dernière expression du bloc se termine par un point-virgule, la valeur de retour sera `()`.

```rust
fn main() {
    let x = 5u32;

    let y = {
        let x_squared = x * x;
        let x_cube = x_squared * x;

        // Cette expression sera assignée à `y`
        x_cube + x_squared + x
    };

    let z = {
        // Le point-virgule supprime cette expression et `()` est assigné à `z`
        2 * x;
    };

    println!("x est {:?}", x);
    println!("y est {:?}", y);
    println!("z est {:?}", z);
}
```
