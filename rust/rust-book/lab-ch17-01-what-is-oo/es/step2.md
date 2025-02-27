# Los objetos contienen datos y comportamiento

El libro _Diseño de Patrones: Elementos de Software Orientado a Objetos Reutilizable_ de Erich Gamma, Richard Helm, Ralph Johnson y John Vlissides (Addison-Wesley, 1994), conocido popularmente como el libro de _Los Cuatro Grandes_, es un catálogo de patrones de diseño orientados a objetos. Lo define de la siguiente manera:

Los programas orientados a objetos están compuestos por objetos. Un _objeto_ agrupa tanto datos como los procedimientos que operan sobre esos datos. Los procedimientos se denominan generalmente _métodos_ o _operaciones_.

Con esta definición, Rust es orientado a objetos: los structs y los enums tienen datos, y los bloques `impl` proporcionan métodos para los structs y los enums. Aunque los structs y los enums con métodos no se _llaman_ objetos, proporcionan la misma funcionalidad, de acuerdo con la definición de objetos de Los Cuatro Grandes.
