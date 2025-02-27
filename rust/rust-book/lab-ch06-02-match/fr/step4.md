# Les correspondances sont exhaustives

Il y a un autre aspect de `match` que nous devons discuter : les modèles des branches doivent couvrir toutes les possibilités. Considérez cette version de notre fonction `plus_one`, qui contient un bogue et ne compilera pas :

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        Some(i) => Some(i + 1),
    }
}
```

Nous n'avons pas traité le cas `None`, donc ce code entraînera un bogue. Heureusement, c'est un bogue que Rust sait détecter. Si nous essayons de compiler ce code, nous obtiendrons cette erreur :

```bash
error[E0004]: non-exhaustive patterns: `None` not covered
 --> src/main.rs:3:15
  |
3 |         match x {
  |               ^ pattern `None` not covered
  |
  note: `Option<i32>` defined here
      = note: the matched value is of type `Option<i32>`
help: ensure that all possible cases are being handled by adding
a match arm with a wildcard pattern or an explicit pattern as
shown
    |
4   ~             Some(i) => Some(i + 1),
5   ~             None => todo!(),
    |
```

Rust sait que nous n'avons pas couvert toutes les possibilités et même lequel des modèles nous avons oublié! Les correspondances en Rust sont _exhaustives_ : nous devons épuiser toutes les dernières possibilités pour que le code soit valide. En particulier dans le cas de `Option<T>`, lorsque Rust nous empêche d'oublier de traiter explicitement le cas `None`, il nous protège d'assumer qu'il existe une valeur alors que nous pourrions avoir `null`, rendant ainsi impossible la fameuse erreur coûteuse évoquée précédemment.
