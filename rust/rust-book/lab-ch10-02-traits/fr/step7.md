# Spécification de Plusieurs Contraintes de Trait avec la Syntaxe +

Nous pouvons également spécifier plusieurs contraintes de trait. Disons que nous voulions que `notify` utilise la mise en forme d'affichage ainsi que `summarize` sur `item` : nous spécifions dans la définition de `notify` que `item` doit implémenter à la fois `Display` et `Summary`. Nous pouvons le faire en utilisant la syntaxe `+` :

```rust
pub fn notify(item: &(impl Summary + Display)) {
```

La syntaxe `+` est également valide avec les contraintes de trait sur les types génériques :

```rust
pub fn notify<T: Summary + Display>(item: &T) {
```

Avec les deux contraintes de trait spécifiées, le corps de `notify` peut appeler `summarize` et utiliser `{}` pour formater `item`.
