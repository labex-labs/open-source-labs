# Calcul de la taille d'un type non récursif

Rappelez l'énumération `Message` que nous avons définie dans le Listing 6-2 lorsque nous avons discuté des définitions d'énumération au Chapitre 6 :

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

Pour déterminer combien d'espace allouer pour une valeur de type `Message`, Rust examine chacun des variants pour voir lequel des variants nécessite le plus d'espace. Rust constate que `Message::Quit` n'a pas besoin d'espace, `Message::Move` a besoin d'un espace suffisant pour stocker deux valeurs de type `i32`, etc. Puisque seul un variant sera utilisé, l'espace maximum dont une valeur de type `Message` aura besoin est l'espace qu'elle occuperait pour stocker le plus grand de ses variants.

Comparez cela à ce qui se passe lorsque Rust essaie de déterminer combien d'espace un type récursif comme l'énumération `List` dans le Listing 15-2 nécessite. Le compilateur commence par examiner la variante `Cons`, qui contient une valeur de type `i32` et une valeur de type `List`. Par conséquent, `Cons` a besoin d'une quantité d'espace égale à la taille d'un `i32` plus la taille d'un `List`. Pour déterminer combien de mémoire le type `List` nécessite, le compilateur examine les variants, en commençant par la variante `Cons`. La variante `Cons` contient une valeur de type `i32` et une valeur de type `List`, et ce processus continue indéfiniment, comme le montre la Figure 15-1.

Figure 15-1 : Une `List` infinie composée de variants `Cons` infinis
