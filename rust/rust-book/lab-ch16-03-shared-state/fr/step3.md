# L'API de Mutex`<T>`{=html}

Pour illustrer comment utiliser un mutex, commençons par l'utiliser dans un contexte mono-fil, comme montré dans la liste 16-12.

Nom de fichier : `src/main.rs`

```rust
use std::sync::Mutex;

fn main() {
  1 let m = Mutex::new(5);

    {
      2 let mut num = m.lock().unwrap();
      3 *num = 6;
  4 }

  5 println!("m = {:?}", m);
}
```

Liste 16-12 : Exploration de l'API de `Mutex<T>` dans un contexte mono-fil pour plus de simplicité

Comme pour de nombreux types, nous créons un `Mutex<T>` en utilisant la fonction associée `new` \[1\]. Pour accéder aux données à l'intérieur du mutex, nous utilisons la méthode `lock` pour acquérir le verrou \[2\]. Cet appel bloquera le fil actuel, de sorte qu'il ne pourra pas effectuer de travail tant que ce n'est pas à notre tour d'avoir le verrou.

L'appel à `lock` échouerait si un autre fil détenant le verrou était interrompu. Dans ce cas, personne ne pourrait jamais obtenir le verrou, donc nous avons choisi d'utiliser `unwrap` et de faire planter ce fil si nous sommes dans cette situation.

Une fois que nous avons acquis le verrou, nous pouvons traiter la valeur de retour, appelée `num` dans ce cas, comme une référence mutable aux données à l'intérieur. Le système de types garantit que nous acquérons un verrou avant d'utiliser la valeur dans `m`. Le type de `m` est `Mutex<i32>`, pas `i32`, donc nous _devons_ appeler `lock` pour être en mesure d'utiliser la valeur `i32`. Nous ne pouvons pas oublier ; le système de types ne nous permettra pas d'accéder à l'`i32` interne autrement.

Comme vous le soupçonnez peut-être, `Mutex<T>` est un pointeur intelligent. Plus précisément, l'appel à `lock` _renvoie_ un pointeur intelligent appelé `MutexGuard`, encapsulé dans un `LockResult` que nous avons traité avec l'appel à `unwrap`. Le pointeur intelligent `MutexGuard` implémente `Deref` pour pointer vers nos données internes ; le pointeur intelligent a également une implémentation de `Drop` qui libère automatiquement le verrou lorsque le `MutexGuard` sort de portée, ce qui se produit à la fin de la portée interne \[4\]. En conséquence, nous ne courons pas le risque d'oublier de libérer le verrou et de bloquer l'utilisation du mutex par d'autres threads car la libération du verrou se produit automatiquement.

Après avoir libéré le verrou, nous pouvons afficher la valeur du mutex et constater que nous avons été en mesure de changer l'`i32` interne en `6` \[5\].
