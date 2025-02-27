# Appending to a String with push_str and push

Nous pouvons faire croître une `String` en utilisant la méthode `push_str` pour ajouter une tranche de chaîne de caractères, comme montré dans la Liste 8-15.

```rust
let mut s = String::from("foo");
s.push_str("bar");
```

Liste 8-15: Ajout d'une tranche de chaîne de caractères à une `String` en utilisant la méthode `push_str`

Après ces deux lignes, `s` contiendra `foobar`. La méthode `push_str` prend une tranche de chaîne de caractères car nous ne voulons pas nécessairement prendre la propriété du paramètre. Par exemple, dans le code de la Liste 8-16, nous voulons être en mesure d'utiliser `s2` après avoir ajouté son contenu à `s1`.

```rust
let mut s1 = String::from("foo");
let s2 = "bar";
s1.push_str(s2);
println!("s2 is {s2}");
```

Liste 8-16: Utilisation d'une tranche de chaîne de caractères après avoir ajouté son contenu à une `String`

Si la méthode `push_str` prenait la propriété de `s2`, nous ne serions pas en mesure d'afficher sa valeur sur la dernière ligne. Cependant, ce code fonctionne comme prévu!

La méthode `push` prend un seul caractère en tant que paramètre et l'ajoute à la `String`. La Liste 8-17 ajoute la lettre _l_ à une `String` en utilisant la méthode `push`.

```rust
let mut s = String::from("lo");
s.push('l');
```

Liste 8-17: Ajout d'un caractère à une valeur `String` en utilisant `push`

En conséquence, `s` contiendra `lol`.
