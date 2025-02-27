# Boucles conditionnelles avec `while`

Un programme a souvent besoin d'évaluer une condition à l'intérieur d'une boucle. Tant que la condition est `vraie`, la boucle s'exécute. Lorsque la condition cesse d'être `vraie`, le programme appelle `break`, ce qui arrête la boucle. Il est possible de mettre en œuvre un comportement de ce type en utilisant une combinaison de `loop`, `if`, `else` et `break` ; vous pouvez essayer cela maintenant dans un programme, si vous le souhaitez. Cependant, ce modèle est si courant que Rust a une construction de langage intégrée pour cela, appelée boucle `while`. Dans la liste 3-3, nous utilisons `while` pour faire boucler le programme trois fois, en décomptant à chaque fois, puis, après la boucle, afficher un message et sortir.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let mut number = 3;

    while number!= 0 {
        println!("{number}!");

        number -= 1;
    }

    println!("DÉCOLAGE!!!");
}
```

Liste 3-3 : Utilisation d'une boucle `while` pour exécuter du code tant qu'une condition est évaluée comme `vraie`

Cette construction élimine beaucoup d'imbrications qui seraient nécessaires si vous utilisiez `loop`, `if`, `else` et `break`, et elle est plus claire. Tant qu'une condition est évaluée comme `vraie`, le code s'exécute ; sinon, il sort de la boucle.
