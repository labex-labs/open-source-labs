# El Tipo Carácter

El tipo `char` de Rust es el tipo alfabético más primitivo del lenguaje. Aquí hay algunos ejemplos de declaración de valores `char`:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let c = 'z';
    let z: char = 'ℤ'; // con anotación de tipo explícita
    let heart_eyed_cat = '😻';
}
```

Tenga en cuenta que especificamos los literales `char` con comillas simples, en contraste con los literales de cadena, que usan comillas dobles. El tipo `char` de Rust tiene un tamaño de cuatro bytes y representa un Valor Escalar Unicode, lo que significa que puede representar mucho más que solo ASCII. Letras con acento; caracteres chinos, japoneses y coreanos; emoji; y espacios de ancho cero son todos valores `char` válidos en Rust. Los Valores Escalares Unicode van desde `U+0000` hasta `U+D7FF` y `U+E000` hasta `U+10FFFF` inclusive. Sin embargo, un "carácter" no es realmente un concepto en Unicode, por lo que su intuición humana sobre lo que es un "carácter" puede no coincidir con lo que es un `char` en Rust. Discutiremos este tema en detalle en "Almacenar texto codificado en UTF-8 con cadenas".
