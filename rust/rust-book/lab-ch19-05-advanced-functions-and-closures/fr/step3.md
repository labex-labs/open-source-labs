# Retourner des closures

Les closures sont représentées par des traits, ce qui signifie que vous ne pouvez pas retourner directement des closures. Dans la plupart des cas où vous voudriez retourner un trait, vous pouvez au lieu de cela utiliser le type concret qui implémente le trait comme valeur de retour de la fonction. Cependant, vous ne pouvez pas faire cela avec les closures car elles n'ont pas de type concret qui soit retournable ; vous n'êtes pas autorisé à utiliser le pointeur de fonction `fn` comme type de retour, par exemple.

Le code suivant essaie de retourner directement une closure, mais il ne compilera pas :

```rust
fn returns_closure() -> dyn Fn(i32) -> i32 {
    |x| x + 1
}
```

L'erreur du compilateur est la suivante :

```bash
error[E0746]: return type cannot have an unboxed trait object
 --> src/lib.rs:1:25
  |
1 | fn returns_closure() -> dyn Fn(i32) -> i32 {
  |                         ^^^^^^^^^^^^^^^^^^ doesn't have a size known at
compile-time
  |
  = note: for information on `impl Trait`, see
<https://doc.rust-lang.org/book/ch10-02-traits.html#returning-types-that-
implement-traits>
help: use `impl Fn(i32) -> i32` as the return type, as all return paths are of
type `[closure@src/lib.rs:2:5: 2:14]`, which implements `Fn(i32) -> i32`
  |
1 | fn returns_closure() -> impl Fn(i32) -> i32 {
  |                         ~~~~~~~~~~~~~~~~~~~
```

L'erreur renvoie à nouveau au trait `Sized`! Rust ne sait pas combien d'espace il devra utiliser pour stocker la closure. Nous avons vu une solution à ce problème plus tôt. Nous pouvons utiliser un objet de trait :

```rust
fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
    Box::new(|x| x + 1)
}
```

Ce code compilera parfaitement. Pour en savoir plus sur les objets de trait, consultez "Utiliser des objets de trait qui autorisent des valeurs de différents types".

Ensuite, regardons les macros!
