# Verwenden von Closures, die ihre Umgebung erfassen

Viele Iterator-Adapter nehmen Closures als Argumente entgegen, und im Allgemeinen werden die Closures, die wir als Argumente für Iterator-Adapter angeben, Closures sein, die ihre Umgebung erfassen.

Für dieses Beispiel verwenden wir die `filter`-Methode, die ein Closure annimmt. Das Closure erhält ein Element aus dem Iterator und gibt einen `bool` zurück. Wenn das Closure `true` zurückgibt, wird der Wert in der von `filter` erzeugten Iteration enthalten. Wenn das Closure `false` zurückgibt, wird der Wert nicht enthalten sein.

In Listing 13-16 verwenden wir `filter` mit einem Closure, das die Variable `shoe_size` aus seiner Umgebung erfasst, um über eine Sammlung von `Shoe`-Struct-Instanzen zu iterieren. Es wird nur Schuhe zurückgeben, die die angegebene Größe haben.

Dateiname: `src/lib.rs`

```rust
#[derive(PartialEq, Debug)]
struct Shoe {
    size: u32,
    style: String,
}

fn shoes_in_size(shoes: Vec<Shoe>, shoe_size: u32) -> Vec<Shoe> {
    shoes.into_iter().filter(|s| s.size == shoe_size).collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn filters_by_size() {
        let shoes = vec![
            Shoe {
                size: 10,
                style: String::from("sneaker"),
            },
            Shoe {
                size: 13,
                style: String::from("sandal"),
            },
            Shoe {
                size: 10,
                style: String::from("boot"),
            },
        ];

        let in_my_size = shoes_in_size(shoes, 10);

        assert_eq!(
            in_my_size,
            vec![
                Shoe {
                    size: 10,
                    style: String::from("sneaker")
                },
                Shoe {
                    size: 10,
                    style: String::from("boot")
                },
            ]
        );
    }
}
```

Listing 13-16: Verwenden der `filter`-Methode mit einem Closure, das `shoe_size` erfasst

Die Funktion `shoes_in_size` übernimmt die Eigentumsgewalt über einen Vektor von Schuhen und eine Schuhgröße als Parameter. Sie gibt einen Vektor zurück, der nur Schuhe der angegebenen Größe enthält.

Im Körper von `shoes_in_size` rufen wir `into_iter` auf, um einen Iterator zu erstellen, der die Eigentumsgewalt über den Vektor übernimmt. Anschließend rufen wir `filter` auf, um diesen Iterator in einen neuen Iterator umzuwandeln, der nur Elemente enthält, für die das Closure `true` zurückgibt.

Das Closure erfasst den Parameter `shoe_size` aus der Umgebung und vergleicht den Wert mit der Größe jedes Schuhs, behält dabei nur Schuhe der angegebenen Größe bei. Schließlich ruft `collect` die von dem adaptierten Iterator zurückgegebenen Werte in einen Vektor zusammen, der von der Funktion zurückgegeben wird.

Der Test zeigt, dass wenn wir `shoes_in_size` aufrufen, wir nur Schuhe zurückbekommen, die die gleiche Größe wie den von uns angegebenen Wert haben.
