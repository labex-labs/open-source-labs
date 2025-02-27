# Matching on Different Errors

Le code de la liste 9-4 provoquera une panique (`panic!`) peu importe pourquoi `File::open` a échoué. Cependant, nous souhaitons prendre des actions différentes pour différentes raisons d'échec. Si `File::open` a échoué parce que le fichier n'existe pas, nous voulons créer le fichier et renvoyer le pointeur vers le nouveau fichier. Si `File::open` a échoué pour toute autre raison - par exemple, parce que nous n'avons pas les autorisations pour ouvrir le fichier - nous souhaitons que le code provoque toujours une panique (`panic!`) de la même manière qu'il l'a fait dans la liste 9-4. Pour cela, nous ajoutons une expression `match` interne, comme montré dans la liste 9-5.

Nom du fichier : `src/main.rs`

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => {
                match File::create("hello.txt") {
                    Ok(fc) => fc,
                    Err(e) => panic!(
                        "Problem creating the file: {:?}",
                        e
                    ),
                }
            }
            other_error => {
                panic!(
                    "Problem opening the file: {:?}",
                    other_error
                );
            }
        },
    };
}
```

Liste 9-5 : Gérer différents types d'erreurs de manière différente

Le type de la valeur renvoyée par `File::open` à l'intérieur de la variante `Err` est `io::Error`, qui est une structure fournie par la bibliothèque standard. Cette structure a une méthode `kind` que nous pouvons appeler pour obtenir une valeur `io::ErrorKind`. L'énumération `io::ErrorKind` est fournie par la bibliothèque standard et a des variantes représentant les différents types d'erreurs qui peuvent résulter d'une opération `io`. La variante que nous voulons utiliser est `ErrorKind::NotFound`, qui indique que le fichier que nous essayons d'ouvrir n'existe pas encore. Ainsi, nous effectuons un `match` sur `greeting_file_result`, mais nous avons également un `match` interne sur `error.kind()`.

La condition que nous voulons vérifier dans le `match` interne est de savoir si la valeur renvoyée par `error.kind()` est la variante `NotFound` de l'énumération `ErrorKind`. Si c'est le cas, nous essayons de créer le fichier avec `File::create`. Cependant, puisque `File::create` peut également échouer, nous avons besoin d'un deuxième bras dans l'expression `match` interne. Lorsque le fichier ne peut pas être créé, un message d'erreur différent est affiché. Le deuxième bras du `match` externe reste le même, de sorte que le programme provoque une panique pour toute erreur autre que l'erreur de fichier manquant.
