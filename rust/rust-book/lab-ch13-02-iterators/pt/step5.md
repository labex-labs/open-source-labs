# Usando _Closures_ que Capturam seu Ambiente

Muitos adaptadores de iterador recebem _closures_ como argumentos, e comumente os _closures_ que especificaremos como argumentos para adaptadores de iterador serão _closures_ que capturam seu ambiente.

Para este exemplo, usaremos o método `filter`, que recebe um _closure_. O _closure_ recebe um item do iterador e retorna um `bool`. Se o _closure_ retornar `true`, o valor será incluído na iteração produzida por `filter`. Se o _closure_ retornar `false`, o valor não será incluído.

Na Listagem 13-16, usamos `filter` com um _closure_ que captura a variável `shoe_size` de seu ambiente para iterar sobre uma coleção de instâncias da _struct_ `Shoe`. Ele retornará apenas sapatos que são do tamanho especificado.

Nome do arquivo: `src/lib.rs`

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

Listagem 13-16: Usando o método `filter` com um _closure_ que captura `shoe_size`

A função `shoes_in_size` assume a propriedade de um vetor de sapatos e um tamanho de sapato como parâmetros. Ela retorna um vetor contendo apenas sapatos do tamanho especificado.

No corpo de `shoes_in_size`, chamamos `into_iter` para criar um iterador que assume a propriedade do vetor. Em seguida, chamamos `filter` para adaptar esse iterador em um novo iterador que contém apenas elementos para os quais o _closure_ retorna `true`.

O _closure_ captura o parâmetro `shoe_size` do ambiente e compara o valor com o tamanho de cada sapato, mantendo apenas sapatos do tamanho especificado. Finalmente, chamar `collect` reúne os valores retornados pelo iterador adaptado em um vetor que é retornado pela função.

O teste mostra que, quando chamamos `shoes_in_size`, recebemos de volta apenas sapatos que têm o mesmo tamanho que o valor que especificamos.
