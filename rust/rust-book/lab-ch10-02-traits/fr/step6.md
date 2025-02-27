# Syntaxe des Contraintes de Trait

La syntaxe `impl Trait` fonctionne pour les cas simples, mais est en fait un sucre syntaxique pour une forme plus longue connue sous le nom de _contrainte de trait_ ; elle ressemble à ceci :

```rust
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```

Cette forme plus longue est équivalente à l'exemple de la section précédente, mais est plus verbeuse. Nous plaçons les contraintes de trait avec la déclaration du paramètre de type générique après deux points et à l'intérieur de crochets.

La syntaxe `impl Trait` est pratique et permet d'avoir un code plus concis dans les cas simples, tandis que la syntaxe complète des contraintes de trait peut exprimer plus de complexité dans d'autres cas. Par exemple, nous pouvons avoir deux paramètres qui implémentent `Summary`. Le faire avec la syntaxe `impl Trait` ressemble à ceci :

```rust
pub fn notify(item1: &impl Summary, item2: &impl Summary) {
```

Utiliser `impl Trait` est approprié si nous voulons que cette fonction permette à `item1` et `item2` d'avoir des types différents (pourvu que les deux types implémentent `Summary`). Si nous voulons forcer les deux paramètres à avoir le même type, cependant, nous devons utiliser une contrainte de trait, comme ceci :

```rust
pub fn notify<T: Summary>(item1: &T, item2: &T) {
```

Le type générique `T` spécifié comme type des paramètres `item1` et `item2` contraint la fonction de sorte que le type concret de la valeur passée en argument pour `item1` et `item2` doit être le même.
