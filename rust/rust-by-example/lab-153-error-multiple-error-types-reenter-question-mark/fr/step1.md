# Autres utilisations de `?`

Remarquez dans l'exemple précédent que notre première réaction à l'appel de `parse` est de `map` l'erreur d'une erreur de bibliothèque en une erreur encadrée :

```rust
.and_then(|s| s.parse::<i32>())
 .map_err(|e| e.into())
```

Puisque c'est une opération simple et courante, il serait pratique de pouvoir l'omettre. Malheureusement, car `and_then` n'est pas suffisamment flexible, on ne peut pas. Cependant, on peut au lieu utiliser `?`.

`?` a été précédemment expliqué comme étant soit `unwrap` soit `return Err(err)`. C'est seulement en partie vrai. En réalité, cela signifie `unwrap` ou `return Err(From::from(err))`. Puisque `From::from` est une utilité de conversion entre différents types, cela signifie que si vous utilisez `?` où l'erreur est convertible en type de retour, elle sera automatiquement convertie.

Ici, on réécrit l'exemple précédent en utilisant `?`. En conséquence, le `map_err` disparaîtra lorsque `From::from` est implémenté pour notre type d'erreur :

```rust
use std::error;
use std::fmt;

// Changez l'alias en `Box<dyn error::Error>`.
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

// La même structure que précédemment mais plutôt que de chaîner tous les `Results`
// et les `Options` ensemble, on utilise `?` pour extraire immédiatement la valeur interne.
fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(EmptyVec)?;
    let parsed = first.parse::<i32>()?;
    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    print(double_first(numbers));
    print(double_first(empty));
    print(double_first(strings));
}
```

Cela est maintenant en fait assez propre. Comparé au `panic` d'origine, il est très similaire à remplacer les appels `unwrap` par `?` sauf que les types de retour sont `Result`. En conséquence, ils doivent être déstructurés au niveau supérieur.
