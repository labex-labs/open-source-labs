# ¡Bytes, valores escalares y clusters de grafemas! ¡Oh, mi!

Otro punto sobre UTF-8 es que en realidad hay tres maneras relevantes de ver las cadenas desde el punto de vista de Rust: como bytes, valores escalares y clusters de grafemas (lo más cercano a lo que llamaríamos _letras_).

Si miramos la palabra hindi "नमस्ते" escrita en el alfabeto devanagari, se almacena como un vector de valores de `u8` que se ve así:

```rust
[224, 164, 168, 224, 164, 174, 224, 164, 184, 224, 165, 141, 224,
164, 164, 224, 165, 135]
```

Eso son 18 bytes y es cómo las computadoras almacenan ultimamente estos datos. Si los miramos como valores escalares Unicode, que es el tipo `char` de Rust, esos bytes se ven así:

```rust
['न', 'म', 'स', '्', 'त', 'े']
```

Hay seis valores de `char` aquí, pero el cuarto y el sexto no son letras: son diacríticos que no tienen sentido por sí solos. Finalmente, si los miramos como clusters de grafemas, obtendríamos lo que una persona llamaría las cuatro letras que forman la palabra hindi:

```rust
["न", "म", "स्", "ते"]
```

Rust proporciona diferentes maneras de interpretar los datos de cadena crudos que almacenan las computadoras para que cada programa pueda elegir la interpretación que necesita, sin importar el idioma humano del que se tratan los datos.

Una razón final por la cual Rust no nos permite indexar una `String` para obtener un carácter es que se espera que las operaciones de indexación siempre tomen un tiempo constante (O(1)). Pero no es posible garantizar ese rendimiento con una `String`, porque Rust tendría que recorrer el contenido desde el principio hasta el índice para determinar cuántos caracteres válidos había.
