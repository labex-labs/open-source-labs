# Recoverable Errors with Result

La plupart des erreurs ne sont pas assez graves pour nécessiter l'arrêt total du programme. Parfois, lorsqu'une fonction échoue, c'est pour une raison que vous pouvez facilement interpréter et répondre. Par exemple, si vous essayez d'ouvrir un fichier et que cette opération échoue parce que le fichier n'existe pas, vous pouvez vouloir créer le fichier au lieu de terminer le processus.

Rappelez-vous de "Handling Potential Failure with Result" que l'énumération `Result` est définie comme ayant deux variantes, `Ok` et `Err`, comme suit :

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

Les paramètres de type génériques `T` et `E` : nous en parlerons en détail au chapitre 10. Ce dont vous devez vous souvenir pour l'instant, c'est que `T` représente le type de la valeur qui sera renvoyée dans un cas de réussite dans la variante `Ok`, et `E` représente le type de l'erreur qui sera renvoyée dans un cas d'échec dans la variante `Err`. Étant donné que `Result` a ces paramètres de type génériques, nous pouvons utiliser le type `Result` et les fonctions définies dessus dans de nombreuses situations différentes où la valeur de réussite et la valeur d'erreur que nous voulons renvoyer peuvent différer.

Appelons une fonction qui renvoie une valeur `Result` parce que la fonction peut échouer. Dans la liste 9-3, nous essayons d'ouvrir un fichier.

Nom du fichier : `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");
}
```

Liste 9-3 : Ouvrir un fichier

Le type de retour de `File::open` est un `Result<T, E>`. Le paramètre de type générique `T` a été remplacé dans l'implémentation de `File::open` par le type de la valeur de réussite, `std::fs::File`, qui est un pointeur de fichier. Le type de `E` utilisé dans la valeur d'erreur est `std::io::Error`. Ce type de retour signifie que l'appel à `File::open` peut réussir et renvoyer un pointeur de fichier que nous pouvons lire ou écrire. L'appel de fonction peut également échouer : par exemple, le fichier peut ne pas exister, ou nous n'ayons pas les autorisations pour accéder au fichier. La fonction `File::open` doit avoir un moyen de nous dire si elle a réussi ou échoué et en même temps nous donner soit le pointeur de fichier soit des informations d'erreur. C'est exactement ce que l'énumération `Result` transporte.

Dans le cas où `File::open` réussit, la valeur dans la variable `greeting_file_result` sera une instance de `Ok` qui contient un pointeur de fichier. Dans le cas où cela échoue, la valeur dans `greeting_file_result` sera une instance de `Err` qui contient plus d'informations sur le type d'erreur qui s'est produite.

Nous devons ajouter au code de la liste 9-3 pour prendre des actions différentes selon la valeur renvoyée par `File::open`. La liste 9-4 montre une façon de gérer le `Result` en utilisant un outil de base, l'expression `match` que nous avons discutée au chapitre 6.

Nom du fichier : `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => {
            panic!("Problem opening the file: {:?}", error);
        }
    };
}
```

Liste 9-4 : Utilisation d'une expression `match` pour gérer les variantes `Result` qui pourraient être renvoyées

Notez que, comme l'énumération `Option`, l'énumération `Result` et ses variantes ont été importées dans la portée par le préambule, donc nous n'avons pas besoin de spécifier `Result::` avant les variantes `Ok` et `Err` dans les branches `match`.

Lorsque le résultat est `Ok`, ce code renverra la valeur interne `file` de la variante `Ok`, et nous assignons ensuite cette valeur de pointeur de fichier à la variable `greeting_file`. Après le `match`, nous pouvons utiliser le pointeur de fichier pour lire ou écrire.

L'autre branche du `match` gère le cas où nous obtenons une valeur `Err` à partir de `File::open`. Dans cet exemple, nous avons choisi d'appeler la macro `panic!`. Si aucun fichier nommé _hello.txt_ n'est présent dans notre répertoire actuel et que nous exécutons ce code, nous verrons la sortie suivante de la macro `panic!` :

    thread'main' panicked at 'Problem opening the file: Os { code:
     2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:8:23

Comme d'habitude, cette sortie nous dit exactement ce qui s'est mal passé.
