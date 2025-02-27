# Herencia como sistema de tipos y como compartir código

La _herencia_ es un mecanismo mediante el cual un objeto puede heredar elementos de la definición de otro objeto, obteniendo así los datos y el comportamiento del objeto padre sin tener que definirlos nuevamente.

Si un lenguaje debe tener herencia para ser orientado a objetos, entonces Rust no es ese tipo de lenguaje. No hay forma de definir un struct que herede los campos y las implementaciones de métodos del struct padre sin utilizar una macro.

Sin embargo, si estás acostumbrado a tener herencia en tu herramienta de programación, puedes utilizar otras soluciones en Rust, dependiendo de la razón por la que optaste por la herencia en primer lugar.

Elegirías herencia por dos razones principales. Una es para la reutilización de código: puedes implementar un comportamiento particular para un tipo, y la herencia te permite reutilizar esa implementación para un tipo diferente. Puedes hacer esto de manera limitada en el código de Rust utilizando implementaciones predeterminadas de métodos de trato, que viste en la Lista 10-14 cuando agregamos una implementación predeterminada del método `summarize` en el trato `Summary`. Cualquier tipo que implemente el trato `Summary` tendría el método `summarize` disponible sin necesidad de más código. Esto es similar a una clase padre que tiene una implementación de un método y una clase hija heredada que también tiene la implementación del método. También podemos anular la implementación predeterminada del método `summarize` cuando implementamos el trato `Summary`, lo que es similar a una clase hija anulando la implementación de un método heredado de una clase padre.

La otra razón para utilizar herencia está relacionada con el sistema de tipos: para permitir que un tipo hijo se utilice en los mismos lugares que el tipo padre. Esto también se llama _polimorfismo_, que significa que puedes sustituir múltiples objetos entre sí en tiempo de ejecución si comparten ciertas características.

> **Polimorfismo**
>
> Para muchas personas, el polimorfismo es sinónimo de herencia. Pero en realidad es un concepto más general que se refiere al código que puede trabajar con datos de múltiples tipos. Para la herencia, esos tipos son generalmente subclases.
>
> Rust en cambio utiliza genéricos para abstraerse sobre diferentes tipos posibles y límites de trato para imponer restricciones sobre lo que esos tipos deben proporcionar. Esto a veces se llama _polimorfismo paramétrico acotado_.

La herencia ha caído en desgracia recientemente como solución de diseño de programación en muchos lenguajes de programación porque a menudo corre el riesgo de compartir más código del necesario. Las subclases no siempre deben compartir todas las características de su clase padre, pero lo harán con la herencia. Esto puede hacer que el diseño de un programa sea menos flexible. También introduce la posibilidad de llamar a métodos en subclases que no tienen sentido o que causan errores porque los métodos no se aplican a la subclase. Además, algunos lenguajes solo permitirán herencia simple (es decir, una subclase solo puede heredar de una clase), lo que restringe aún más la flexibilidad del diseño de un programa.

Por estas razones, Rust adopta el enfoque diferente de utilizar objetos de trato en lugar de herencia. Veamos cómo los objetos de trato permiten el polimorfismo en Rust.
