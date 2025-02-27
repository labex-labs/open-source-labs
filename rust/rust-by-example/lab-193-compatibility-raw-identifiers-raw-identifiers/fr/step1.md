# Identifiants bruts

Rust, comme de nombreux langages de programmation, a le concept de "mots clés". Ces identifiants ont une signification pour le langage, et donc vous ne pouvez pas les utiliser dans des endroits comme les noms de variables, les noms de fonctions et d'autres endroits. Les identifiants bruts vous permettent d'utiliser des mots clés là où ils ne seraient normalement autorisés. Cela est particulièrement utile lorsque Rust introduit de nouveaux mots clés, et qu'une bibliothèque utilisant une édition plus ancienne de Rust a une variable ou une fonction avec le même nom qu'un mot clé introduit dans une édition plus récente.

Par exemple, considérez une boîte à outils `foo` compilée avec l'édition 2015 de Rust qui exporte une fonction nommée `try`. Ce mot clé est réservé pour une nouvelle fonctionnalité dans l'édition 2018, donc sans identifiants bruts, nous n'aurions pas de moyen de nommer la fonction.

```rust
extern crate foo;

fn main() {
    foo::try();
}
```

Vous obtiendrez cette erreur :

```plaintext
error: expected identifier, found keyword `try`
 --> src/main.rs:4:4
  |
4 | foo::try();
  |      ^^^ expected identifier, found keyword
```

Vous pouvez écrire cela avec un identifiant brut :

```rust
extern crate foo;

fn main() {
    foo::r#try();
}
```
