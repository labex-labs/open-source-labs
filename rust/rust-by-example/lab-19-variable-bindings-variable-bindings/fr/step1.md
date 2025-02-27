# Liaisons de variables

Rust offre une sécurité de type grâce à la typage statique. Les liaisons de variables peuvent être annotées au moment de leur déclaration. Cependant, dans la plupart des cas, le compilateur sera capable d'inférer le type de la variable à partir du contexte, réduisant considérablement la charge d'annotation.

Des valeurs (comme des littéraux) peuvent être liées à des variables, en utilisant la liaison `let`.

```rust
fn main() {
    let an_integer = 1u32;
    let a_boolean = true;
    let unit = ();

    // copie `an_integer` dans `copied_integer`
    let copied_integer = an_integer;

    println!("Un entier : {:?}", copied_integer);
    println!("Un booléen : {:?}", a_boolean);
    println!("Rencontons la valeur unit : {:?}", unit);

    // Le compilateur avertit des liaisons de variables non utilisées ; ces avertissements peuvent
    // être silencieux en préfixant le nom de variable par un tiret bas
    let _unused_variable = 3u32;

    let noisy_unused_variable = 2u32;
    // FIXME ^ Préfixer avec un tiret bas pour supprimer l'avertissement
    // Notez que les avertissements peuvent ne pas être affichés dans un navigateur
}
```
