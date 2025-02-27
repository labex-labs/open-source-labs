# Poderes adicionales de Rust inseguro

Para cambiar a Rust inseguro, utiliza la palabra clave `unsafe` y luego comienza un nuevo bloque que contiene el código inseguro. Puedes realizar cinco acciones en Rust inseguro que no puedes realizar en Rust seguro, que llamamos _poderes adicionales de Rust inseguro_. Esos poderes adicionales incluyen la capacidad de:

1.  Dereferenciar un puntero crudo
2.  Llamar a una función o método inseguro
3.  Acceder o modificar una variable estática mutable
4.  Implementar un trato inseguro
5.  Acceder a los campos de las `union`

Es importante entender que `unsafe` no desactiva el verificador de préstamos ni deshabilita ninguna de las otras comprobaciones de seguridad de Rust: si utilizas una referencia en código inseguro, todavía se comprobará. La palabra clave `unsafe` solo te da acceso a estas cinco características que luego no se verifican por el compilador para la seguridad de la memoria. Todavía obtendrás cierto grado de seguridad dentro de un bloque inseguro.

Además, `unsafe` no significa que el código dentro del bloque sea necesariamente peligroso o que definitivamente tendrá problemas de seguridad de memoria: la intención es que, como programador, asegures que el código dentro de un bloque `unsafe` acceda a la memoria de manera válida.

Las personas son falibles y se producirán errores, pero al requerir que estas cinco operaciones inseguras estén dentro de bloques anotados con `unsafe`, sabrás que cualquier error relacionado con la seguridad de la memoria debe estar dentro de un bloque `unsafe`. Mantén los bloques `unsafe` pequeños; te agradecerás más tarde cuando investigues errores de memoria.

Para aislar el código inseguro lo máximo posible, es mejor encerrar ese código dentro de una abstracción segura y proporcionar una API segura, que discutiremos más adelante en el capítulo cuando examinemos funciones y métodos inseguros. Parte de la biblioteca estándar se implementa como abstracciones seguras sobre código inseguro que ha sido revisado. Envolver el código inseguro en una abstracción segura evita que el uso de `unsafe` se filtre a todos los lugares donde tú o tus usuarios puedan querer utilizar la funcionalidad implementada con código inseguro, porque utilizar una abstracción segura es segura.

Veamos cada uno de los cinco poderes adicionales de Rust inseguro por separado. También veremos algunas abstracciones que proporcionan una interfaz segura para el código inseguro.
