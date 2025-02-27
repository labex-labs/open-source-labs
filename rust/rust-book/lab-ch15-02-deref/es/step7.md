# Cómo la Coerción de Deref Interactúa con la Mutabilidad

De manera similar a cómo se utiliza el trato `Deref` para sobrescribir el operador `*` en referencias inmutables, se puede usar el trato `DerefMut` para sobrescribir el operador `*` en referencias mutables.

Rust realiza la coerción de Deref cuando encuentra tipos e implementaciones de tratos en tres casos:

- De `&T` a `&U` cuando `T: Deref<Target=U>`
- De `&mut T` a `&mut U` cuando `T: DerefMut<Target=U>`
- De `&mut T` a `&U` cuando `T: Deref<Target=U>`

Los primeros dos casos son iguales, excepto que el segundo implementa la mutabilidad. El primer caso establece que si tienes una `&T`, y `T` implementa `Deref` a algún tipo `U`, puedes obtener una `&U` de manera transparente. El segundo caso establece que la misma coerción de Deref ocurre para referencias mutables.

El tercer caso es más complicado: Rust también coercionará una referencia mutable a una inmutable. Pero lo contrario _no_ es posible: las referencias inmutables nunca se coercerán a referencias mutables. Debido a las reglas de préstamo, si tienes una referencia mutable, esa referencia mutable debe ser la única referencia a esos datos (de lo contrario, el programa no se compilaría). Convertir una referencia mutable en una referencia inmutable nunca romperá las reglas de préstamo. Convertir una referencia inmutable en una referencia mutable requeriría que la referencia inmutable inicial fuera la única referencia inmutable a esos datos, pero las reglas de préstamo no garantizan eso. Por lo tanto, Rust no puede hacer la suposición de que es posible convertir una referencia inmutable en una referencia mutable.
