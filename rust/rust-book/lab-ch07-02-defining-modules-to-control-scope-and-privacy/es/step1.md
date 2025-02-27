# Definiendo Módulos para Controlar el Alcance y la Privacidad

En esta sección, hablaremos sobre los módulos y otras partes del sistema de módulos, concretamente las _rutas_, que te permiten nombrar los elementos; la palabra clave `use` que trae una ruta al ámbito; y la palabra clave `pub` para hacer que los elementos sean públicos. También discutiremos la palabra clave `as`, los paquetes externos y el operador glob.

Los _módulos_ nos permiten organizar el código dentro de un crat para que sea legible y fácil de reutilizar. Los módulos también nos permiten controlar la _privacidad_ de los elementos, ya que el código dentro de un módulo es privado por defecto. Los elementos privados son detalles de implementación internos no disponibles para el uso externo. Podemos elegir hacer públicos los módulos y los elementos que los componen, lo que los expone para que el código externo los pueda usar y depender de ellos.

Como ejemplo, escribamos un crat de biblioteca que proporcione la funcionalidad de un restaurante. Definiremos las firmas de las funciones pero las dejaremos con el cuerpo vacío para centrar la atención en la organización del código en lugar de en la implementación de un restaurante.

En la industria del restaurante, algunas partes de un restaurante se denominan _parte de sala_ y otras _parte de cocina_. La parte de sala es donde se encuentran los clientes; esto incluye donde los camareros asignan mesas a los clientes, los meseros toman pedidos y cobran, y los barman preparan bebidas. La parte de cocina es donde los chefs y los cocineros trabajan en la cocina, los lavaplatos limpian y los gerentes realizan tareas administrativas.

Para estructurar nuestro crat de esta manera, podemos organizar sus funciones en módulos anidados. Crea una nueva biblioteca llamada `restaurant` ejecutando `cargo new restaurant --lib`. Luego, ingresa el código de la Lista 7-1 en `src/lib.rs` para definir algunos módulos y firmas de funciones; este código es la sección de la parte de sala.

Nombre del archivo: `src/lib.rs`

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}

        fn seat_at_table() {}
    }

    mod serving {
        fn take_order() {}

        fn serve_order() {}

        fn take_payment() {}
    }
}
```

Lista 7-1: Un módulo `front_of_house` que contiene otros módulos que a su vez contienen funciones

Definimos un módulo con la palabra clave `mod` seguida del nombre del módulo (en este caso, `front_of_house`). El cuerpo del módulo luego va dentro de llaves. Dentro de los módulos, podemos colocar otros módulos, como en este caso con los módulos `hosting` y `serving`. Los módulos también pueden contener definiciones para otros elementos, como structs, enums, constantes, traits y, como en la Lista 7-1, funciones.

Al usar módulos, podemos agrupar definiciones relacionadas y nombrar por qué están relacionadas. Los programadores que usan este código pueden navegar por el código basado en los grupos en lugar de tener que leer todas las definiciones, lo que hace que sea más fácil encontrar las definiciones que les son relevantes. Los programadores que agregan nueva funcionalidad a este código sabrán dónde colocar el código para mantener el programa organizado.

Antes, mencionamos que `src/main.rs` y `src/lib.rs` se llaman raíces del crat. La razón de su nombre es que el contenido de cualquiera de estos dos archivos forma un módulo llamado `crate` en la raíz de la estructura de módulos del crat, conocida como el _árbol de módulos_.

La Lista 7-2 muestra el árbol de módulos para la estructura de la Lista 7-1.

```bash
crate
└── front_of_house
├── hosting
│ ├── add_to_waitlist
│ └── seat_at_table
└── serving
├── take_order
├── serve_order
└── take_payment
```

Lista 7-2: El árbol de módulos para el código de la Lista 7-1

Este árbol muestra cómo algunos de los módulos se anidan dentro de otros módulos; por ejemplo, `hosting` se anida dentro de `front_of_house`. El árbol también muestra que algunos módulos son _hermanos_, lo que significa que están definidos en el mismo módulo; `hosting` y `serving` son hermanos definidos dentro de `front_of_house`. Si el módulo A está contenido dentro del módulo B, decimos que el módulo A es el _hijo_ del módulo B y que el módulo B es el _padre_ del módulo A. Observe que todo el árbol de módulos está enraizado bajo el módulo implícito llamado `crate`.

El árbol de módulos puede recordarte el árbol de directorios del sistema de archivos de tu computadora; esta es una comparación muy adecuada. Al igual que las carpetas en un sistema de archivos, se usan los módulos para organizar tu código. Y al igual que los archivos en una carpeta, necesitamos una forma de encontrar nuestros módulos.
