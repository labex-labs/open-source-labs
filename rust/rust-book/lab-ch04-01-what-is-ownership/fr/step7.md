# Variables et données interagissant avec la méthode `clone`

Si nous _voulons_ réellement copier en profondeur les données du tas du `String`, et non seulement les données de la pile, nous pouvons utiliser une méthode commune appelée `clone`. Nous aborderons la syntaxe des méthodes au chapitre 5, mais comme les méthodes sont une caractéristique commune de nombreux langages de programmation, vous avez probablement déjà rencontré ce concept.

Voici un exemple d'utilisation de la méthode `clone` :

```rust
let s1 = String::from("hello");
let s2 = s1.clone();

println!("s1 = {s1}, s2 = {s2}");
```

Cela fonctionne parfaitement et produit explicitement le comportement montré dans la figure 4-3, où les données du tas _sont_ effectivement copiées.

Lorsque vous voyez un appel à `clone`, vous savez qu'un code arbitraire est exécuté et que ce code peut être coûteux. C'est un indicateur visuel que quelque chose de différent se passe.
