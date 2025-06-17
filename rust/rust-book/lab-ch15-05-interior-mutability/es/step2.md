# Aplicando las Reglas de Préstamo en Tiempo de Ejecución con RefCell`<T>`

A diferencia de `Rc<T>`, el tipo `RefCell<T>` representa la propiedad exclusiva de los datos que contiene. Entonces, ¿en qué se diferencia `RefCell<T>` de un tipo como `Box<T>`? Recuerda las reglas de préstamo que aprendiste en el Capítulo 4:

- En cualquier momento dado, puedes tener _ya sea_ una referencia mutable o cualquier número de referencias inmutables (pero no ambas).
- Las referencias deben siempre ser válidas.

Con las referencias y `Box<T>`, las invariantes de las reglas de préstamo se aplican en tiempo de compilación. Con `RefCell<T>`, estas invariantes se aplican _en tiempo de ejecución_. Con las referencias, si violas estas reglas, obtendrás un error del compilador. Con `RefCell<T>`, si violas estas reglas, tu programa se bloqueará y saldrá.

Las ventajas de comprobar las reglas de préstamo en tiempo de compilación son que los errores se detectarán más temprano en el proceso de desarrollo y no hay impacto en el rendimiento en tiempo de ejecución porque todo el análisis se completa previamente. Por esas razones, comprobar las reglas de préstamo en tiempo de compilación es la mejor opción en la mayoría de los casos, que es por qué es el predeterminado de Rust.

La ventaja de comprobar las reglas de préstamo en tiempo de ejecución en lugar de eso es que entonces se permiten ciertos escenarios seguros de memoria, donde hubieran sido prohibidos por las comprobaciones en tiempo de compilación. El análisis estático, como el compilador de Rust, es inherentemente conservador. Algunas propiedades del código son imposibles de detectar al analizar el código: el ejemplo más famoso es el Problema de la Parada, que está fuera del alcance de este libro pero es un tema interesante para investigar.

Debido a que algunos análisis son imposibles, si el compilador de Rust no puede estar seguro de que el código cumple con las reglas de propiedad, puede rechazar un programa correcto; de esta manera, es conservador. Si Rust aceptara un programa incorrecto, los usuarios no podrían confiar en las garantías que Rust ofrece. Sin embargo, si Rust rechaza un programa correcto, el programador se verá inconvenciado, pero no puede ocurrir nada catastrófico. El tipo `RefCell<T>` es útil cuando estás seguro de que tu código sigue las reglas de préstamo pero el compilador no es capaz de entender y garantizarlo.

Similar a `Rc<T>`, `RefCell<T>` solo se debe utilizar en escenarios de un solo subproceso y te dará un error en tiempo de compilación si intentas usarlo en un contexto de varios subprocesos. Hablaremos sobre cómo obtener la funcionalidad de `RefCell<T>` en un programa de varios subprocesos en el Capítulo 16.

A continuación, se resume las razones para elegir `Box<T>`, `Rc<T>` o `RefCell<T>`:

- `Rc<T>` permite múltiples propietarios de los mismos datos; `Box<T>` y `RefCell<T>` tienen un solo propietario.
- `Box<T>` permite préstamos inmutables o mutables comprobados en tiempo de compilación; `Rc<T>` solo permite préstamos inmutables comprobados en tiempo de compilación; `RefCell<T>` permite préstamos inmutables o mutables comprobados en tiempo de ejecución.
- Debido a que `RefCell<T>` permite préstamos mutables comprobados en tiempo de ejecución, puedes mutar el valor dentro de `RefCell<T>` incluso cuando `RefCell<T>` es inmutable.

Mutar el valor dentro de un valor inmutable es el _patrón de mutabilidad interior_. Veamos una situación en la que la mutabilidad interior es útil y examinemos cómo es posible.
