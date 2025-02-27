# Usando Clausuras que Capturan su Entorno

Muchos adaptadores de iterador toman clausuras como argumentos, y comúnmente las clausuras que especificaremos como argumentos a los adaptadores de iterador serán clausuras que capturan su entorno.

Para este ejemplo, usaremos el método `filter` que toma una clausura. La clausura recibe un elemento del iterador y devuelve un `bool`. Si la clausura devuelve `true`, el valor se incluirá en la iteración producida por `filter`. Si la clausura devuelve `false`, el valor no se incluirá.

En la Lista 13-16, usamos `filter` con una clausura que captura la variable `shoe_size` de su entorno para iterar sobre una colección de instancias del struct `Shoe`. Devolverá solo los zapatos del tamaño especificado.

Nombre de archivo: `src/lib.rs`

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

Lista 13-16: Usando el método `filter` con una clausura que captura `shoe_size`

La función `shoes_in_size` toma posesión de un vector de zapatos y un tamaño de zapato como parámetros. Devuelve un vector que contiene solo zapatos del tamaño especificado.

En el cuerpo de `shoes_in_size`, llamamos a `into_iter` para crear un iterador que tome posesión del vector. Luego llamamos a `filter` para adaptar ese iterador en un nuevo iterador que solo contiene elementos para los cuales la clausura devuelve `true`.

La clausura captura el parámetro `shoe_size` del entorno y compara el valor con el tamaño de cada zapato, manteniendo solo los zapatos del tamaño especificado. Finalmente, llamar a `collect` agrupa los valores devueltos por el iterador adaptado en un vector que es devuelto por la función.

La prueba muestra que cuando llamamos a `shoes_in_size`, obtenemos solo los zapatos que tienen el mismo tamaño que el valor que especificamos.
