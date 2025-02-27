# Tratar Punteros Inteligentes como Referencias Normales con Deref

Implementar el trato `Deref` te permite personalizar el comportamiento del operador de _dereferencia_ `*` (no confundir con el operador de multiplicación o glob). Al implementar `Deref` de manera que un puntero inteligente se pueda tratar como una referencia normal, puedes escribir código que opere sobre referencias y usar ese código con punteros inteligentes también.

Veamos primero cómo funciona el operador de dereferencia con referencias normales. Luego intentaremos definir un tipo personalizado que se comporte como `Box<T>` y veremos por qué el operador de dereferencia no funciona como una referencia en nuestro nuevo tipo definido. Exploraremos cómo implementar el trato `Deref` hace posible que los punteros inteligentes funcionen de manera similar a las referencias. Luego veremos la característica de _coerción de deref_ de Rust y cómo nos permite trabajar con referencias o punteros inteligentes.

> Nota: Hay una gran diferencia entre el tipo `MyBox<T>` que construiremos y el real `Box<T>`: nuestra versión no almacenará sus datos en el montón. Este ejemplo se centra en `Deref`, por lo que donde se almacenan realmente los datos es menos importante que el comportamiento parecido a un puntero.
