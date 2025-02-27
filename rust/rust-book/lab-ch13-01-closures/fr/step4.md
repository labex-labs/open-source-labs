# Capturer des références ou transférer la propriété

Les closures peuvent capturer des valeurs de leur environnement de trois manières, qui correspondent directement aux trois manières dont une fonction peut prendre un paramètre : emprunter de manière immuable, emprunter de manière mutable et prendre la propriété. La closure décidera laquelle de ces méthodes utiliser en fonction de ce que le corps de la fonction fait avec les valeurs capturées.

Dans la Liste 13-4, nous définissons une closure qui capture une référence immuable au vecteur nommé `list` car elle a seulement besoin d'une référence immuable pour afficher la valeur.

Nom du fichier : `src/main.rs`

```rust
fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 let only_borrows = || println!("From closure: {:?}", list);

    println!("Before calling closure: {:?}", list);
  2 only_borrows();
    println!("After calling closure: {:?}", list);
}
```

Liste 13-4 : Définition et appel d'une closure qui capture une référence immuable

Cet exemple illustre également qu'une variable peut être liée à une définition de closure \[1\], et que nous pouvons plus tard appeler la closure en utilisant le nom de la variable et des parenthèses comme si le nom de la variable était le nom d'une fonction \[2\].

Parce que nous pouvons avoir plusieurs références immuables à `list` en même temps, `list` est toujours accessible dans le code avant la définition de la closure, après la définition de la closure mais avant l'appel de la closure, et après l'appel de la closure. Ce code se compile, s'exécute et imprime :

    Before defining closure: [1, 2, 3]
    Before calling closure: [1, 2, 3]
    From closure: [1, 2, 3]
    After calling closure: [1, 2, 3]

Ensuite, dans la Liste 13-5, nous modifions le corps de la closure pour qu'elle ajoute un élément au vecteur `list`. La closure capture maintenant une référence mutable.

Nom du fichier : `src/main.rs`

```rust
fn main() {
    let mut list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

    let mut borrows_mutably = || list.push(7);

    borrows_mutably();
    println!("After calling closure: {:?}", list);
}
```

Liste 13-5 : Définition et appel d'une closure qui capture une référence mutable

Ce code se compile, s'exécute et imprime :

```rust
Before defining closure: [1, 2, 3]
After calling closure: [1, 2, 3, 7]
```

Notez qu'il n'y a plus de `println!` entre la définition et l'appel de la closure `borrows_mutably` : lorsqu'on définit `borrows_mutably`, elle capture une référence mutable à `list`. Nous n'utilisons plus la closure après qu'elle a été appelée, donc le prêt mutable prend fin. Entre la définition de la closure et l'appel de la closure, un prêt immuable pour afficher n'est pas autorisé car aucun autre prêt n'est autorisé lorsqu'il y a un prêt mutable. Essayez d'ajouter un `println!` là pour voir quel message d'erreur vous obtenez!

Si vous voulez forcer la closure à prendre la propriété des valeurs qu'elle utilise dans l'environnement même si le corps de la closure n'a pas strictement besoin de la propriété, vous pouvez utiliser le mot clé `move` avant la liste de paramètres.

Cette technique est surtout utile lorsqu'on passe une closure à un nouveau thread pour transférer les données de sorte qu'elles soient possédées par le nouveau thread. Nous discuterons des threads et des raisons pour lesquelles vous voudriez les utiliser en détail au Chapitre 16 lorsque nous parlerons de concurrence, mais pour l'instant, examinons brièvement le lancement d'un nouveau thread en utilisant une closure qui nécessite le mot clé `move`. La Liste 13-6 montre la Liste 13-4 modifiée pour afficher le vecteur dans un nouveau thread plutôt que dans le thread principal.

Nom du fichier : `src/main.rs`

```rust
use std::thread;

fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 thread::spawn(move || {
      2 println!("From thread: {:?}", list)
    }).join().unwrap();
}
```

Liste 13-6 : Utilisation de `move` pour forcer la closure du thread à prendre la propriété de `list`

Nous lançons un nouveau thread, en donnant au thread une closure à exécuter en tant qu'argument. Le corps de la closure imprime la liste. Dans la Liste 13-4, la closure n'a capturé `list` qu'en utilisant une référence immuable car c'est le moindre accès à `list` nécessaire pour l'afficher. Dans cet exemple, même si le corps de la closure a toujours seulement besoin d'une référence immuable \[2\], nous devons spécifier que `list` doit être transféré dans la closure en plaçant le mot clé `move` \[1\] au début de la définition de la closure. Le nouveau thread pourrait finir avant que le reste du thread principal ne finisse, ou le thread principal pourrait finir en premier. Si le thread principal conserve la propriété de `list` mais finit avant le nouveau thread et libère `list`, la référence immuable dans le thread serait invalide. Par conséquent, le compilateur exige que `list` soit transféré dans la closure donnée au nouveau thread pour que la référence soit valide. Essayez de supprimer le mot clé `move` ou d'utiliser `list` dans le thread principal après la définition de la closure pour voir quels messages d'erreur du compilateur vous obtenez!
