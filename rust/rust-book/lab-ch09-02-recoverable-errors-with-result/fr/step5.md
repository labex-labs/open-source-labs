# Propagating Errors

Lorsque l'implémentation d'une fonction appelle une opération qui peut échouer, au lieu de gérer l'erreur dans la fonction elle-même, vous pouvez renvoyer l'erreur au code appelant afin qu'il puisse décider de ce qu'il faut faire. Cela s'appelle _propager_ l'erreur et donne plus de contrôle au code appelant, où il peut y avoir plus d'informations ou de logique qui dictent la manière dont l'erreur devrait être gérée que ce que vous avez disponible dans le contexte de votre code.

Par exemple, la liste 9-6 montre une fonction qui lit un nom d'utilisateur à partir d'un fichier. Si le fichier n'existe pas ou ne peut pas être lu, cette fonction renverra ces erreurs au code qui a appelé la fonction.

Nom du fichier : `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

1 fn read_username_from_file() -> Result<String, io::Error> {
  2 let username_file_result = File::open("hello.txt");

  3 let mut username_file = match username_file_result {
      4 Ok(file) => file,
      5 Err(e) => return Err(e),
    };

  6 let mut username = String::new();

  7 match username_file.read_to_string(&mut username) {
      8 Ok(_) => Ok(username),
      9 Err(e) => Err(e),
    }
}
```

Liste 9-6 : Une fonction qui renvoie des erreurs au code appelant en utilisant `match`

Cette fonction peut être écrite d'une manière beaucoup plus courte, mais nous allons commencer par la faire de manière manuelle pour explorer la gestion des erreurs ; à la fin, nous montrerons la manière plus courte. Regardons d'abord le type de retour de la fonction : `Result<String, io::Error>` \[1\]. Cela signifie que la fonction renvoie une valeur du type `Result<T, E>`, où le paramètre de type générique `T` a été remplacé par le type concret `String` et le type générique `E` a été remplacé par le type concret `io::Error`.

Si cette fonction réussit sans problème, le code qui appelle cette fonction recevra une valeur `Ok` qui contient une `String` - le `username` que cette fonction a lu à partir du fichier \[8\]. Si cette fonction rencontre des problèmes, le code appelant recevra une valeur `Err` qui contient une instance de `io::Error` qui contient plus d'informations sur les problèmes rencontrés. Nous avons choisi `io::Error` comme type de retour de cette fonction parce que c'est exactement le type de la valeur d'erreur renvoyée par les deux opérations que nous appelons dans le corps de cette fonction qui peuvent échouer : la fonction `File::open` \[2\] et la méthode `read_to_string` \[7\].

Le corps de la fonction commence par appeler la fonction `File::open` \[2\]. Ensuite, nous gérons la valeur `Result` avec un `match` similaire au `match` de la liste 9-4. Si `File::open` réussit, le pointeur de fichier dans la variable de modèle `file` \[4\] devient la valeur dans la variable mutable `username_file` \[3\] et la fonction continue. Dans le cas `Err`, au lieu d'appeler `panic!`, nous utilisons le mot clé `return` pour sortir de la fonction immédiatement et renvoyer la valeur d'erreur de `File::open`, maintenant dans la variable de modèle `e`, au code appelant comme valeur d'erreur de cette fonction \[5\].

Donc, si nous avons un pointeur de fichier dans `username_file`, la fonction crée ensuite une nouvelle `String` dans la variable `username` \[6\] et appelle la méthode `read_to_string` sur le pointeur de fichier dans `username_file` pour lire le contenu du fichier dans `username` \[7\]. La méthode `read_to_string` renvoie également un `Result` car elle peut échouer, même si `File::open` a réussi. Nous avons donc besoin d'un autre `match` pour gérer ce `Result` : si `read_to_string` réussit, alors notre fonction a réussi et nous renvoyons le nom d'utilisateur du fichier qui se trouve maintenant dans `username` encapsulé dans un `Ok`. Si `read_to_string` échoue, nous renvoyons la valeur d'erreur de la même manière que nous avons renvoyé la valeur d'erreur dans le `match` qui a géré la valeur de retour de `File::open`. Cependant, nous n'avons pas besoin de dire explicitement `return`, car c'est la dernière expression de la fonction \[9\].

Le code qui appelle ce code devra ensuite gérer la réception d'une valeur `Ok` qui contient un nom d'utilisateur ou d'une valeur `Err` qui contient un `io::Error`. C'est au code appelant de décider de ce qu'il faut faire avec ces valeurs. Si le code appelant reçoit une valeur `Err`, il pourrait appeler `panic!` et faire planter le programme, utiliser un nom d'utilisateur par défaut ou chercher le nom d'utilisateur à partir d'un autre emplacement que le fichier, par exemple. Nous n'avons pas assez d'informations sur ce que le code appelant essaye réellement de faire, donc nous propagons toutes les informations de réussite ou d'erreur vers le haut pour qu'il les gère de manière appropriée.

Ce modèle de propagation d'erreurs est si courant en Rust que Rust fournit l'opérateur point d'interrogation `?` pour le simplifier.
