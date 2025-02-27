# Constantes

Como las variables inmutables, las _constantes_ son valores que están vinculados a un nombre y no se les permite cambiar, pero hay algunas diferencias entre las constantes y las variables.

En primer lugar, no se te permite usar `mut` con constantes. Las constantes no solo son inmutables por defecto, sino que siempre lo son. Declaras constantes usando la palabra clave `const` en lugar de la palabra clave `let`, y el tipo del valor _debe_ ser anotado. Cubriremos tipos y anotaciones de tipos en "Tipos de datos", así que no te preocupes por los detalles por ahora. Simplemente sé que siempre debes anotar el tipo.

Las constantes se pueden declarar en cualquier ámbito, incluyendo el ámbito global, lo que las hace útiles para valores que muchas partes del código necesitan conocer.

La última diferencia es que las constantes solo pueden establecerse en una expresión constante, no en el resultado de un valor que solo se podría calcular en tiempo de ejecución.

Aquí hay un ejemplo de declaración de constante:

```rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```

El nombre de la constante es `THREE_HOURS_IN_SECONDS` y su valor se establece en el resultado de multiplicar 60 (el número de segundos en un minuto) por 60 (el número de minutos en una hora) por 3 (el número de horas que queremos contar en este programa). La convención de nombres de Rust para las constantes es usar todas las letras mayúsculas con guiones bajos entre las palabras. El compilador es capaz de evaluar un conjunto limitado de operaciones en tiempo de compilación, lo que nos permite elegir escribir este valor de una manera más fácil de entender y verificar, en lugar de establecer esta constante en el valor `10.800`. Consulte la sección de evaluación de constantes de la Referencia de Rust en *https://doc.rust-lang.org/reference/const_eval.html* para obtener más información sobre qué operaciones se pueden usar al declarar constantes.

Las constantes son válidas durante todo el tiempo que un programa se ejecuta, dentro del ámbito en el que se declararon. Esta propiedad hace que las constantes sean útiles para valores en el dominio de su aplicación que varias partes del programa pueden necesitar conocer, como el número máximo de puntos que cualquier jugador de un juego puede ganar, o la velocidad de la luz.

Denominar los valores codificados en el código que se usan en todo el programa como constantes es útil para transmitir el significado de ese valor a futuros mantenedores del código. También ayuda a tener solo un lugar en el código donde tendrías que cambiar si el valor codificado en el código necesitara actualizarse en el futuro.
