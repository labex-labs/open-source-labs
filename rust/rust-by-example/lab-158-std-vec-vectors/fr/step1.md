# Vectors

Les vecteurs sont des tableaux redimensionnables. Comme les slices, leur taille n'est pas connue à la compilation, mais ils peuvent croître ou rétrécir à tout moment. Un vecteur est représenté par 3 paramètres :

- pointeur vers les données
- longueur
- capacité

La capacité indique combien de mémoire est réservée pour le vecteur. Le vecteur peut croître tant que la longueur est inférieure à la capacité. Lorsque ce seuil doit être dépassé, le vecteur est réalloué avec une capacité plus grande.

```rust
fn main() {
    // Les itérateurs peuvent être collectés dans des vecteurs
    let collected_iterator: Vec<i32> = (0..10).collect();
    println!("Collected (0..10) into: {:?}", collected_iterator);

    // Le macro `vec!` peut être utilisé pour initialiser un vecteur
    let mut xs = vec![1i32, 2, 3];
    println!("Initial vector: {:?}", xs);

    // Insérer un nouvel élément à la fin du vecteur
    println!("Push 4 into the vector");
    xs.push(4);
    println!("Vector: {:?}", xs);

    // Erreur! Les vecteurs immuables ne peuvent pas croître
    collected_iterator.push(0);
    // FIXME ^ Comment out this line

    // La méthode `len` renvoie le nombre d'éléments actuellement stockés dans un vecteur
    println!("Vector length: {}", xs.len());

    // L'indexation est faite en utilisant les crochets (l'indexation commence à 0)
    println!("Second element: {}", xs[1]);

    // `pop` supprime le dernier élément du vecteur et le renvoie
    println!("Pop last element: {:?}", xs.pop());

    // L'indexation en dehors des limites provoque une panique
    println!("Fourth element: {}", xs[3]);
    // FIXME ^ Comment out this line

    // Les `Vector`s peuvent être facilement itérés
    println!("Contents of xs:");
    for x in xs.iter() {
        println!("> {}", x);
    }

    // Un `Vector` peut également être itéré tandis que le compte d'itération
    // est énuméré dans une variable séparée (`i`)
    for (i, x) in xs.iter().enumerate() {
        println!("In position {} we have value {}", i, x);
    }

    // Grâce à `iter_mut`, les vecteurs mutables peuvent également être itérés
    // de manière à permettre la modification de chaque valeur
    for x in xs.iter_mut() {
        *x *= 3;
    }
    println!("Updated vector: {:?}", xs);
}
```

Plus de méthodes `Vec` peuvent être trouvées dans le module `std::vec`
