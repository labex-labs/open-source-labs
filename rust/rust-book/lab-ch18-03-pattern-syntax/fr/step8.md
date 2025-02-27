# Déconstruction d'enums

Nous avons déjà déconstruit des enums dans ce livre (par exemple, dans la Liste 6-5), mais nous n'avons pas encore explicitement discuté que le motif pour déconstruire un enum correspond à la manière dont les données stockées dans l'enum sont définies. Par exemple, dans la Liste 18-15, nous utilisons l'enum `Message` de la Liste 6-2 et écrivons une expression `match` avec des motifs qui déconstruiront chaque valeur interne.

Nom de fichier : `src/main.rs`

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
  1 let msg = Message::ChangeColor(0, 160, 255);

    match msg {
      2 Message::Quit => {
            println!(
                "The Quit variant has no data to destructure."
            );
        }
      3 Message::Move { x, y } => {
            println!(
                "Move in the x dir {x}, in the y dir {y}"
            );
        }
      4 Message::Write(text) => {
            println!("Text message: {text}");
        }
      5 Message::ChangeColor(r, g, b) => println!(
            "Change color to red {r}, green {g}, and blue {b}"
        ),
    }
}
```

Liste 18-15 : Déconstruction des variantes d'enum qui contiennent différents types de valeurs

Ce code imprimera `Change color to red 0, green 160, and blue 255`. Essayez de modifier la valeur de `msg` \[1\] pour voir le code des autres bras s'exécuter.

Pour les variantes d'enum sans données, comme `Message::Quit` \[2\], nous ne pouvons pas déconstruire la valeur plus loin. Nous ne pouvons que correspondre à la valeur littérale `Message::Quit`, et aucun variable n'est dans ce motif.

Pour les variantes d'enum ressemblant à des structs, telles que `Message::Move` \[3\], nous pouvons utiliser un motif similaire à celui que nous spécifions pour correspondre à des structs. Après le nom de la variante, nous plaçons des accolades et ensuite listons les champs avec des variables pour que nous séparions les parties à utiliser dans le code de ce bras. Ici, nous utilisons la forme abrégée comme nous l'avons fait dans la Liste 18-13.

Pour les variantes d'enum ressemblant à des tuples, comme `Message::Write` qui contient un tuple avec un élément \[4\] et `Message::ChangeColor` qui contient un tuple avec trois éléments \[5\], le motif est similaire à celui que nous spécifions pour correspondre à des tuples. Le nombre de variables dans le motif doit correspondre au nombre d'éléments dans la variante que nous sommes en train de correspondre.
