# Caso de prueba: map-reduce

Rust hace muy fácil paralelizar el procesamiento de datos, sin muchos de los dolores de cabeza tradicionalmente asociados con este intento.

La biblioteca estándar proporciona excelentes primitivas de subprocesamiento listas para usar. Estas, combinadas con el concepto de Propiedad y las reglas de aliasación de Rust, evitan automáticamente las carreras de datos.

Las reglas de aliasación (una referencia escribible exclusiva XOR muchas referencias lectoras) te impiden automáticamente manipular el estado visible para otros subprocesos. (Donde se necesite sincronización, hay primitivas de sincronización como `Mutex`es o `Channel`s.)

En este ejemplo, calcularemos la suma de todos los dígitos en un bloque de números. Lo haremos dividiendo trozos del bloque en diferentes subprocesos. Cada subproceso sumará su pequeño bloque de dígitos, y luego sumaremos las sumas intermedias producidas por cada subproceso.

Tenga en cuenta que, aunque estamos pasando referencias a través de los límites de los subprocesos, Rust entiende que solo estamos pasando referencias de solo lectura, y que por lo tanto no pueden ocurrir errores de seguridad ni carreras de datos. También porque las referencias que estamos pasando tienen vidas `'static`, Rust entiende que nuestros datos no se destruirán mientras estos subprocesos sigan ejecutándose. (Cuando necesite compartir datos no `static` entre subprocesos, puede usar un puntero inteligente como `Arc` para mantener los datos activos y evitar vidas no `static`.)

```rust
use std::thread;

// Este es el subproceso `main`
fn main() {

    // Estos son nuestros datos a procesar.
    // Calcularemos la suma de todos los dígitos a través de un algoritmo map-reduce en subprocesos.
    // Cada trozo separado por espacios será manejado en un subproceso diferente.
    //
    // TODO: vea qué pasa con la salida si inserta espacios!
    let data = "86967897737416471853297327050364959
11861322575564723963297542624962850
70856234701860851907960690014725639
38397966707106094172783238747669219
52380795257888236525459303330302837
58495327135744041048897885734297812
69920216438980873548808413720956532
16278424637452589860345374828574668";

    // Crea un vector para almacenar los subprocesos hijos que generaremos.
    let mut children = vec![];

    /*************************************************************************
     * Fase "Map"
     *
     * Divide nuestros datos en segmentos y aplica el procesamiento inicial
     ************************************************************************/

    // Divide nuestros datos en segmentos para un cálculo individual
    // cada trozo será una referencia (&str) al dato real
    let chunked_data = data.split_whitespace();

    // Itera sobre los segmentos de datos.
    //.enumerate() agrega el índice actual del bucle a lo que sea que se itere
    // la tupla resultante "(índice, elemento)" se "desestructura" inmediatamente
    // en dos variables, "i" y "data_segment" con una
    // "asignación de desestructuración"
    for (i, data_segment) in chunked_data.enumerate() {
        println!("data segment {} is \"{}\"", i, data_segment);

        // Procesa cada segmento de datos en un subproceso separado
        //
        // spawn() devuelve un controlador al nuevo subproceso,
        // que DEBEMOS mantener para acceder al valor devuelto
        //
        //'move || -> u32' es la sintaxis para un cierre que:
        // * no toma argumentos ('||')
        // * toma la propiedad de sus variables capturadas ('move') y
        // * devuelve un entero sin signo de 32 bits ('-> u32')
        //
        // Rust es lo suficientemente inteligente para inferir el '-> u32' a partir de
        // el propio cierre, así que podríamos haber omitido eso.
        //
        // TODO: intente quitar el'move' y vea qué pasa
        children.push(thread::spawn(move || -> u32 {
            // Calcula la suma intermedia de este segmento:
            let result = data_segment
                       // itera sobre los caracteres de nuestro segmento..
                     .chars()
                       //.. convierte los caracteres de texto en su valor numérico..
                     .map(|c| c.to_digit(10).expect("debería ser un dígito"))
                       //.. y suma el iterador resultante de números
                     .sum();

            // println! bloquea la salida estándar, así que no hay intercalación de texto
            println!("processed segment {}, result={}", i, result);

            // "return" no es necesario, porque Rust es un "lenguaje de expresiones", el
            // último expresión evaluada en cada bloque es automáticamente su valor.
            result

        }));
    }


    /*************************************************************************
     * Fase "Reduce"
     *
     * Recopila nuestros resultados intermedios y los combina en un resultado final
     ************************************************************************/

    // Combina los resultados intermedios de cada subproceso en una sola suma final.
    //
    // usamos el "turbofish" ::<> para proporcionar un indicador de tipo a sum()
    //
    // TODO: intente sin el turbofish, en lugar de
    // especificar explícitamente el tipo de final_result
    let final_result = children.into_iter().map(|c| c.join().unwrap()).sum::<u32>();

    println!("Final sum result: {}", final_result);
}

```

## Tareas

No es inteligente hacer que el número de subprocesos dependa de los datos ingresados por el usuario. ¿Qué pasa si el usuario decide insertar muchos espacios? ¿Realmente queremos generar 2.000 subprocesos? Modifique el programa para que los datos siempre se dividan en un número limitado de trozos, definido por una constante estática al principio del programa.
