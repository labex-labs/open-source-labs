# Uso del patrón newtype para seguridad y abstracción de tipos

> Nota: Esta sección asume que has leído la sección anterior "Uso del patrón newtype para implementar rasgos externos".

El patrón newtype también es útil para tareas más allá de las que hemos discutido hasta ahora, incluyendo la aplicación de una restricción estática para evitar confusiones entre valores y la indicación de las unidades de un valor. Viste un ejemplo de uso de newtypes para indicar unidades en la Lista 19-15: recuerda que las estructuras `Millímetros` y `Metros` envolvían valores de `u32` en un newtype. Si escribimos una función con un parámetro de tipo `Millímetros`, no podremos compilar un programa que accidentalmente intente llamar a esa función con un valor de tipo `Metros` o un `u32` simple.

También podemos usar el patrón newtype para abstraer algunos detalles de implementación de un tipo: el nuevo tipo puede exponer una API pública que es diferente de la API del tipo interno privado.

Los newtypes también pueden ocultar la implementación interna. Por ejemplo, podríamos proporcionar un tipo `People` para envolver un `HashMap<i32, String>` que almacena el ID de una persona asociado con su nombre. El código que usa `People` solo interactuaría con la API pública que proporcionamos, como un método para agregar una cadena de nombre a la colección `People`; ese código no necesitaría saber que asignamos un ID de `i32` a los nombres internamente. El patrón newtype es una forma ligera de lograr la encapsulación para ocultar detalles de implementación, que discutimos en "Encapsulación que oculta detalles de implementación".
