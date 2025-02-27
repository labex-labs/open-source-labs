# Inference

Le moteur d'inférence de type est assez intelligent. Il fait plus que regarder le type de l'expression de valeur lors d'une initialisation. Il regarde également comment la variable est utilisée ensuite pour inférer son type. Voici un exemple avancé d'inférence de type :

```rust
fn main() {
    // En raison de l'annotation, le compilateur sait que `elem` a le type u8.
    let elem = 5u8;

    // Crée un vecteur vide (un tableau pouvant croître).
    let mut vec = Vec::new();
    // À ce stade, le compilateur ne connaît pas le type exact de `vec`, il
    // sait seulement qu'il s'agit d'un vecteur de quelque chose (`Vec<_>`).

    // Insère `elem` dans le vecteur.
    vec.push(elem);
    // Aha! Maintenant, le compilateur sait que `vec` est un vecteur de `u8` (`Vec<u8>`)
    // TODO ^ Essayez de commenter la ligne `vec.push(elem)`

    println!("{:?}", vec);
}
```

Aucune annotation de type de variables n'était nécessaire, le compilateur est content et le programmeur l'est aussi!
