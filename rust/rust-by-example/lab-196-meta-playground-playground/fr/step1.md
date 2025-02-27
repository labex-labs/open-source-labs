# Playground

Le [Rust Playground](https://play.rust-lang.org/) est un moyen d'expérimenter avec du code Rust via une interface web.

## Utilisation avec `mdbook`

Dans `mdbook`, vous pouvez rendre les exemples de code exécutables et modifiables.

```rust
fn main() {
    println!("Hello World!");
}
```

Cela permet au lecteur de lancer l'échantillon de code, mais également de le modifier et d'ajuster. Le point clé ici est d'ajouter le mot `editable` à votre bloc de code séparé par une virgule.

````markdown
```rust
//...place your code here
```
````

De plus, vous pouvez ajouter `ignore` si vous voulez que `mdbook` saute votre code lors de la construction et des tests.

````markdown
```rust
//...place your code here
```
````

## Utilisation avec les documents

Vous avez peut-être remarqué dans certains des documents officiels Rust un bouton qui dit "Exécuter", qui ouvre l'échantillon de code dans un nouvel onglet dans le Rust Playground. Cette fonctionnalité est activée si vous utilisez l'attribut #\[doc\] appelé `html_playground_url`.
