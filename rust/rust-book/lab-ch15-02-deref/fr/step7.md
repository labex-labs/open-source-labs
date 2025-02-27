# How Deref Coercion Interacts with Mutability

De la même manière que vous utilisez le trait `Deref` pour surcharger l'opérateur `*` sur les références immuables, vous pouvez utiliser le trait `DerefMut` pour surcharger l'opérateur `*` sur les références mutables.

Rust effectue une deref coercion lorsqu'il trouve des types et des implémentations de traits dans trois cas :

- De `&T` à `&U` lorsque `T: Deref<Target=U>`
- De `&mut T` à `&mut U` lorsque `T: DerefMut<Target=U>`
- De `&mut T` à `&U` lorsque `T: Deref<Target=U>`

Les deux premiers cas sont identiques, sauf que le second implémente la mutabilité. Le premier cas stipule que si vous avez une `&T`, et que `T` implémente `Deref` vers un certain type `U`, vous pouvez obtenir une `&U` de manière transparente. Le second cas stipule que la même deref coercion se produit pour les références mutables.

Le troisième cas est plus compliqué : Rust coercera également une référence mutable en une référence immutable. Mais l'inverse n'est _pas_ possible : les références immuables ne seront jamais coercées en références mutables. En raison des règles d'emprunt, si vous avez une référence mutable, cette référence mutable doit être la seule référence à cette donnée (sinon, le programme ne compilerait pas). Convertir une référence mutable en une référence immutable ne brisera jamais les règles d'emprunt. Convertir une référence immutable en une référence mutable nécessiterait que la référence immutable initiale soit la seule référence immutable à cette donnée, mais les règles d'emprunt ne garantissent pas cela. Par conséquent, Rust ne peut pas supposer que la conversion d'une référence immutable en une référence mutable est possible.
