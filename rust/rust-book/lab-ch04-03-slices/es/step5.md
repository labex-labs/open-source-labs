# Otras Rebanadas

Como puedes imaginar, las rebanadas de cadena son específicas de las cadenas. Pero también hay un tipo de rebanada más general. Considera este array:

```rust
let a = [1, 2, 3, 4, 5];
```

Al igual que podríamos querer referirnos a una parte de una cadena, también podríamos querer referirnos a una parte de un array. Lo haríamos de la siguiente manera:

```rust
let a = [1, 2, 3, 4, 5];

let slice = &a[1..3];

assert_eq!(slice, &[2, 3]);
```

Esta rebanada tiene el tipo `&[i32]`. Funciona de la misma manera que las rebanadas de cadena, almacenando una referencia al primer elemento y una longitud. Usarás este tipo de rebanada para todo tipo de otras colecciones. Discutiremos estas colecciones en detalle cuando hablemos de vectores en el Capítulo 8.
