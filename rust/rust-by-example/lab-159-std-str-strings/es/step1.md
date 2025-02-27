# Cadenas

En Rust, hay dos tipos de cadenas: `String` y `&str`.

Una `String` se almacena como un vector de bytes (`Vec<u8>`), pero está garantizada para siempre ser una secuencia UTF-8 válida. `String` se asigna en el montón, es crecible y no está terminada en nulo.

`&str` es una porción (`&[u8]`) que siempre apunta a una secuencia UTF-8 válida y se puede utilizar para ver dentro de una `String`, al igual que `&[T]` es una vista dentro de `Vec<T>`.

```rust
fn main() {
    // (todas las anotaciones de tipo son superfluas)
    // Una referencia a una cadena asignada en memoria de solo lectura
    let pangram: &'static str = "the quick brown fox jumps over the lazy dog";
    println!("Pangram: {}", pangram);

    // Itera sobre las palabras en orden inverso, no se asigna una nueva cadena
    println!("Palabras en orden inverso");
    for word in pangram.split_whitespace().rev() {
        println!("> {}", word);
    }

    // Copia los caracteres en un vector, los ordena y elimina los duplicados
    let mut chars: Vec<char> = pangram.chars().collect();
    chars.sort();
    chars.dedup();

    // Crea una `String` vacía y crecible
    let mut string = String::new();
    for c in chars {
        // Inserta un carácter al final de la cadena
        string.push(c);
        // Inserta una cadena al final de la cadena
        string.push_str(", ");
    }

    // La cadena recortada es una porción de la cadena original, por lo tanto no se realiza
    // una nueva asignación
    let chars_to_trim: &[char] = &[' ', ','];
    let trimmed_str: &str = string.trim_matches(chars_to_trim);
    println!("Caracteres utilizados: {}", trimmed_str);

    // Asigna memoria en el montón para una cadena
    let alice = String::from("I like dogs");
    // Asigna nueva memoria y almacena la cadena modificada allí
    let bob: String = alice.replace("dog", "cat");

    println!("Alice dice: {}", alice);
    println!("Bob dice: {}", bob);
}
```

Se pueden encontrar más métodos de `str`/`String` en los módulos `std::str` y `std::string`

## Literales y escapes

Hay múltiples maneras de escribir literales de cadena con caracteres especiales en ellos. Todos resultan en un `&str` similar, por lo que es mejor utilizar la forma que sea más conveniente de escribir. Del mismo modo, hay múltiples maneras de escribir literales de cadena de bytes, que todos resultan en `&[u8; N]`.

Generalmente, los caracteres especiales se escapan con un carácter barra invertida: `\`. De esta manera, se puede agregar cualquier carácter a su cadena, incluso aquellos no imprimibles y aquellos que no sabe cómo escribir. Si desea una barra invertida literal, escápela con otra: `\\`

Los delimitadores de literales de cadena o carácter que aparecen dentro de un literal deben ser escapados: `"\""`, `'\''`.

```rust
fn main() {
    // Puede utilizar escapes para escribir bytes por sus valores hexadecimales...
    let byte_escape = "I'm writing \x52\x75\x73\x74!";
    println!("¿Qué estás haciendo\x3F (\\x3F significa?) {}", byte_escape);

    //...o puntos de código Unicode.
    let unicode_codepoint = "\u{211D}";
    let character_name = "\"DOUBLE-STRUCK CAPITAL R\"";

    println!("El carácter Unicode {} (U+211D) se llama {}",
                unicode_codepoint, character_name );


    let long_string = "String literals
                        can span multiple lines.
                        The linebreak and indentation here ->\
                        <- can be escaped too!";
    println!("{}", long_string);
}
```

A veces, simplemente hay demasiados caracteres que deben ser escapados o es simplemente mucho más conveniente escribir una cadena tal cual. Aquí es donde entran en juego los literales de cadena sin procesar.

```rust
fn main() {
    let raw_str = r"Escapes don't work here: \x3F \u{211D}";
    println!("{}", raw_str);

    // Si necesita comillas en una cadena sin procesar, agregue un par de #s
    let quotes = r#"And then I said: "There is no escape!""#;
    println!("{}", quotes);

    // Si necesita "# en su cadena, simplemente use más #s en el delimitador.
    // Puede usar hasta 65535 #s.
    let longer_delimiter = r###"A string with "# in it. And even "##!"###;
    println!("{}", longer_delimiter);
}
```

¿Quieres una cadena que no sea UTF-8? (Recuerde, `str` y `String` deben ser UTF-8 válidos). O quizás quieres una matriz de bytes que sea mayormente texto? ¡Las cadenas de bytes a la rescate!

```rust
use std::str;

fn main() {
    // Tenga en cuenta que esto no es realmente un `&str`
    let bytestring: &[u8; 21] = b"this is a byte string";

    // Las matrices de bytes no tienen el trato `Display`, por lo que imprimirlas está un poco limitado
    println!("Una cadena de bytes: {:?}", bytestring);

    // Las cadenas de bytes pueden tener escapes de bytes...
    let escaped = b"\x52\x75\x73\x74 as bytes";
    //...pero no escapes Unicode
    // let escaped = b"\u{211D} is not allowed";
    println!("Algunos bytes escapados: {:?}", escaped);


    // Las cadenas de bytes sin procesar funcionan igual que las cadenas sin procesar
    let raw_bytestring = br"\u{211D} is not escaped here";
    println!("{:?}", raw_bytestring);

    // Convertir una matriz de bytes a `str` puede fallar
    if let Ok(my_str) = str::from_utf8(raw_bytestring) {
        println!("Y lo mismo que texto: '{}'", my_str);
    }

    let _quotes = br#"You can also use "fancier" formatting, \
                    like with normal raw strings"#;

    // Las cadenas de bytes no tienen que ser UTF-8
    let shift_jis = b"\x82\xe6\x82\xa8\x82\xb1\x82\xbb"; // "ようこそ" en SHIFT-JIS

    // Pero entonces no siempre se pueden convertir a `str`
    match str::from_utf8(shift_jis) {
        Ok(my_str) => println!("Conversión exitosa: '{}'", my_str),
        Err(e) => println!("Conversión fallida: {:?}", e),
    };
}
```

Para conversiones entre codificaciones de caracteres, consulte la caja de codificación.

Una lista más detallada de las maneras de escribir literales de cadena y caracteres de escape se da en el capítulo 'Tokens' de la Referencia de Rust.
