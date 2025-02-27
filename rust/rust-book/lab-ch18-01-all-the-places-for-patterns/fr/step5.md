# for Loops

Dans une boucle `for`, la valeur qui suit directement le mot-clé `for` est un motif. Par exemple, dans `for x in y`, le `x` est le motif. Le listing 18-3 montre comment utiliser un motif dans une boucle `for` pour _déstructurer_, c'est-à-dire séparer, un tuple en tant que partie de la boucle `for`.

Nom de fichier : `src/main.rs`

```rust
let v = vec!['a', 'b', 'c'];

for (index, value) in v.iter().enumerate() {
    println!("{value} is at index {index}");
}
```

Listing 18-3: Using a pattern in a `for` loop to destructure a tuple

Le code du listing 18-3 imprimera ce qui suit :

    a is at index 0
    b is at index 1
    c is at index 2

Nous adaptons un itérateur en utilisant la méthode `enumerate` de sorte qu'il produit une valeur et l'index de cette valeur, placés dans un tuple. La première valeur produite est le tuple `(0, 'a')`. Lorsque cette valeur est comparée au motif `(index, value)`, `index` sera `0` et `value` sera `'a'`, affichant la première ligne de la sortie.
