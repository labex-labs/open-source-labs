# while let Conditional Loops

De construction similaire à `if let`, la boucle conditionnelle `while let` permet à une boucle `while` de s'exécuter aussi longtemps qu'un motif continue de correspondre. Dans le listing 18-2, nous écrivons une boucle `while let` qui utilise un vecteur comme pile et imprime les valeurs du vecteur dans l'ordre inverse de celui dans lequel elles ont été empilées.

Nom de fichier : `src/main.rs`

```rust
let mut stack = Vec::new();

stack.push(1);
stack.push(2);
stack.push(3);

while let Some(top) = stack.pop() {
    println!("{top}");
}
```

Listing 18-2: Using a `while let` loop to print values for as long as `stack.pop()` returns `Some`

Cet exemple imprime `3`, puis `2`, puis `1`. La méthode `pop` retire le dernier élément du vecteur et renvoie `Some(value)`. Si le vecteur est vide, `pop` renvoie `None`. La boucle `while` continue d'exécuter le code dans son bloc aussi longtemps que `pop` renvoie `Some`. Lorsque `pop` renvoie `None`, la boucle s'arrête. Nous pouvons utiliser `while let` pour dépiler chaque élément de notre pile.
