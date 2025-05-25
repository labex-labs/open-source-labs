# Outras utilizações de `?`

Observe no exemplo anterior que nossa reação imediata ao chamar `parse` é `mapear` o erro de um erro de biblioteca para um erro empacotado (boxed error):

```rust
.and_then(|s| s.parse::<i32>())
    .map_err(|e| e.into())
```

Como esta é uma operação simples e comum, seria conveniente se pudesse ser omitida. Infelizmente, porque `and_then` não é suficientemente flexível, não pode. No entanto, podemos usar `?` em vez disso.

`?` foi previamente explicado como `unwrap` ou `return Err(err)`. Isso é apenas parcialmente verdade. Na verdade, significa `unwrap` ou `return Err(From::from(err))`. Como `From::from` é uma utilidade de conversão entre diferentes tipos, isso significa que se você usar `?` onde o erro é conversível para o tipo de retorno, ele converterá automaticamente.

Aqui, reescrevemos o exemplo anterior usando `?`. Como resultado, o `map_err` desaparecerá quando `From::from` for implementado para o nosso tipo de erro:

```rust
use std::error;
use std::fmt;

// Change the alias to `Box<dyn error::Error>`.
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

// The same structure as before but rather than chain all `Results`
// and `Options` along, we `?` to get the inner value out immediately.
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

Isto é, na verdade, bastante limpo agora. Comparado com o `panic` original, é muito semelhante a substituir as chamadas `unwrap` por `?`, exceto que os tipos de retorno são `Result`. Como resultado, eles devem ser desestruturados no nível superior.
