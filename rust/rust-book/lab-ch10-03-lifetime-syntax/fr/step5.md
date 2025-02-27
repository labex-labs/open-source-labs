# Lifetime Annotation Syntax

Les annotations de durée de vie ne changent pas la durée de vie de l'une quelconque des références. Au contraire, elles décrivent les relations entre les durées de vie de plusieurs références les unes par rapport aux autres sans affecter les durées de vie. Tout comme les fonctions peuvent accepter n'importe quel type lorsque la signature spécifie un paramètre de type générique, les fonctions peuvent accepter des références avec n'importe quelle durée de vie en spécifiant un paramètre de durée de vie générique.

Les annotations de durée de vie ont une syntaxe légèrement inhabituelle : les noms des paramètres de durée de vie doivent commencer par une apostrophe (`'`) et sont généralement tous en minuscules et très courts, comme les types génériques. La plupart des gens utilisent le nom `'a` pour la première annotation de durée de vie. Nous plaçons les annotations de paramètres de durée de vie après le `&` d'une référence, en utilisant un espace pour séparer l'annotation du type de la référence.

Voici quelques exemples : une référence à un `i32` sans paramètre de durée de vie, une référence à un `i32` qui a un paramètre de durée de vie nommé `'a`, et une référence mutable à un `i32` qui a également la durée de vie `'a`.

```rust
&i32        // une référence
&'a i32     // une référence avec une durée de vie explicite
&'a mut i32 // une référence mutable avec une durée de vie explicite
```

Une annotation de durée de vie prise seule n'a pas beaucoup de sens car les annotations sont destinées à dire à Rust comment les paramètres de durée de vie génériques de plusieurs références sont liés les uns aux autres. Examnons comment les annotations de durée de vie sont liées les unes aux autres dans le contexte de la fonction `longest`.
