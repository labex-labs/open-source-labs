# Ensamblado en línea

Rust ofrece soporte para el ensamblado en línea a través de la macro `asm!`. Esto se puede utilizar para incrustar código de ensamblado escrito a mano en la salida de ensamblado generada por el compilador. En general, esto no debería ser necesario, pero puede ser útil cuando se requiere un rendimiento o un control de tiempos determinados que no se pueden lograr de otra manera. El acceso a primitivas de hardware de bajo nivel, por ejemplo, en el código del kernel, también puede requerir esta funcionalidad.

> **Nota**: los ejemplos aquí se dan en ensamblado x86/x86-64, pero también se admiten otras arquitecturas.

Actualmente, el ensamblado en línea está soportado en las siguientes arquitecturas:

- x86 y x86-64
- ARM
- AArch64
- RISC-V

## Uso básico

Comencemos con el ejemplo más simple posible:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

unsafe {
    asm!("nop");
}
# }
```

Esto insertará una instrucción NOP (no operación) en el ensamblado generado por el compilador. Tenga en cuenta que todas las invocaciones a `asm!` deben estar dentro de un bloque `unsafe`, ya que podrían insertar instrucciones arbitrarias y romper varias invariantes. Las instrucciones a insertar se listan en el primer argumento de la macro `asm!` como una literal de cadena.

## Entradas y salidas

Ahora, insertar una instrucción que no hace nada es bastante aburrido. Hagamos algo que realmente actúe sobre los datos:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let x: u64;
unsafe {
    asm!("mov {}, 5", out(reg) x);
}
assert_eq!(x, 5);
# }
```

Esto escribirá el valor `5` en la variable `u64` `x`. Puede ver que la literal de cadena que usamos para especificar las instrucciones es en realidad una cadena de plantilla. Está gobernada por las mismas reglas que las cadenas de formato de Rust. Los argumentos que se insertan en la plantilla, sin embargo, se ven un poco diferentes de lo que puede estar acostumbrado. Primero, debemos especificar si la variable es una entrada o una salida del ensamblado en línea. En este caso es una salida. La declaramos escribiendo `out`. También debemos especificar en qué tipo de registro espera el ensamblado la variable. En este caso, la ponemos en un registro general arbitrario especificando `reg`. El compilador elegirá un registro adecuado para insertar en la plantilla y leerá la variable de allí después de que se complete la ejecución del ensamblado en línea.

Veamos otro ejemplo que también utiliza una entrada:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let i: u64 = 3;
let o: u64;
unsafe {
    asm!(
        "mov {0}, {1}",
        "add {0}, 5",
        out(reg) o,
        in(reg) i,
    );
}
assert_eq!(o, 8);
# }
```

Esto sumará `5` a la entrada en la variable `i` y escribirá el resultado en la variable `o`. La forma particular en que este ensamblado lo hace es primero copiar el valor de `i` a la salida y luego sumar `5` a él.

El ejemplo muestra algunas cosas:

Primero, podemos ver que `asm!` permite múltiples argumentos de cadena de plantilla; cada uno se trata como una línea separada de código de ensamblado, como si todos estuvieran unidos con saltos de línea entre ellos. Esto facilita el formato del código de ensamblado.

Segundo, podemos ver que las entradas se declaran escribiendo `in` en lugar de `out`.

Tercero, podemos ver que podemos especificar un número de argumento o nombre como en cualquier cadena de formato. Para las plantillas de ensamblado en línea, esto es particularmente útil ya que los argumentos a menudo se usan más de una vez. Para ensamblado en línea más complejo, generalmente se recomienda usar esta facilidad, ya que mejora la legibilidad y permite reordenar las instrucciones sin cambiar el orden de los argumentos.

Podemos refinar aún más el ejemplo anterior para evitar la instrucción `mov`:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut x: u64 = 3;
unsafe {
    asm!("add {0}, 5", inout(reg) x);
}
assert_eq!(x, 8);
# }
```

Podemos ver que `inout` se utiliza para especificar un argumento que es tanto entrada como salida. Esto es diferente de especificar una entrada y una salida por separado en que se garantiza que se asignen ambos al mismo registro.

También es posible especificar variables diferentes para las partes de entrada y salida de un operando `inout`:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let x: u64 = 3;
let y: u64;
unsafe {
    asm!("add {0}, 5", inout(reg) x => y);
}
assert_eq!(y, 8);
# }
```

## Operandos de salida tardía

El compilador de Rust es conservador en la asignación de operandos. Se asume que una `out` se puede escribir en cualquier momento y, por lo tanto, no puede compartir su ubicación con ningún otro argumento. Sin embargo, para garantizar un rendimiento óptimo, es importante utilizar la menor cantidad posible de registros, para que no sea necesario guardarlos y recargarlos alrededor del bloque de ensamblado en línea. Para lograr esto, Rust proporciona un especificador `lateout`. Esto se puede utilizar en cualquier salida que se escriba solo después de que se hayan consumido todas las entradas. También hay una variante `inlateout` de este especificador.

Aquí hay un ejemplo donde `inlateout` _no puede_ usarse en modo `release` o otros casos optimizados:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a: u64 = 4;
let b: u64 = 4;
let c: u64 = 4;
unsafe {
    asm!(
        "add {0}, {1}",
        "add {0}, {2}",
        inout(reg) a,
        in(reg) b,
        in(reg) c,
    );
}
assert_eq!(a, 12);
# }
```

Lo anterior podría funcionar bien en casos no optimizados (`Debug` mode), pero si desea un rendimiento optimizado (`release` mode o otros casos optimizados), no podría funcionar.

Eso se debe a que en casos optimizados, el compilador puede asignar el mismo registro para las entradas `b` y `c` ya que sabe que tienen el mismo valor. Sin embargo, debe asignar un registro separado para `a` ya que utiliza `inout` y no `inlateout`. Si se usara `inlateout`, entonces `a` y `c` podrían ser asignados al mismo registro, en cuyo caso la primera instrucción para sobrescribir el valor de `c` haría que el código de ensamblado produjera un resultado incorrecto.

Sin embargo, el siguiente ejemplo puede usar `inlateout` ya que la salida solo se modifica después de que se hayan leído todos los registros de entrada:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a: u64 = 4;
let b: u64 = 4;
unsafe {
    asm!("add {0}, {1}", inlateout(reg) a, in(reg) b);
}
assert_eq!(a, 8);
# }
```

Como puede ver, este fragmento de ensamblado todavía funcionará correctamente si `a` y `b` se asignan al mismo registro.

## Operandos de registro explícitos

Algunas instrucciones requieren que los operandos estén en un registro específico. Por lo tanto, el ensamblado en línea de Rust proporciona algunos especificadores de restricción más específicos. Si bien `reg` generalmente está disponible en cualquier arquitectura, los registros explícitos son altamente específicos de la arquitectura. Por ejemplo, para x86, los registros generales `eax`, `ebx`, `ecx`, `edx`, `ebp`, `esi` y `edi`, entre otros, se pueden referir por su nombre.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let cmd = 0xd1;
unsafe {
    asm!("out 0x64, eax", in("eax") cmd);
}
# }
```

En este ejemplo, llamamos a la instrucción `out` para enviar el contenido de la variable `cmd` al puerto `0x64`. Dado que la instrucción `out` solo acepta `eax` (y sus subregistros) como operando, tuvimos que usar el especificador de restricción `eax`.

> **Nota**: a diferencia de otros tipos de operandos, los operandos de registro explícitos no se pueden usar en la cadena de plantilla: no se puede usar `{}` y se debe escribir el nombre del registro directamente en su lugar. Además, deben aparecer al final de la lista de operandos después de todos los demás tipos de operandos.

Considere este ejemplo que utiliza la instrucción `mul` de x86:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

fn mul(a: u64, b: u64) -> u128 {
    let lo: u64;
    let hi: u64;

    unsafe {
        asm!(
            // La instrucción mul de x86 toma rax como entrada implícita y escribe
            // el resultado de la multiplicación de 128 bits en rax:rdx.
            "mul {}",
            in(reg) a,
            inlateout("rax") b => lo,
            lateout("rdx") hi
        );
    }

    ((hi as u128) << 64) + lo as u128
}
# }
```

Este utiliza la instrucción `mul` para multiplicar dos entradas de 64 bits con un resultado de 128 bits. El único operando explícito es un registro, que llenamos a partir de la variable `a`. El segundo operando es implícito y debe ser el registro `rax`, que llenamos a partir de la variable `b`. Los 64 bits inferiores del resultado se almacenan en `rax` a partir de los cuales llenamos la variable `lo`. Los 64 bits superiores se almacenan en `rdx` a partir de los cuales llenamos la variable `hi`.

## Registros afectados

En muchos casos, el ensamblado en línea modificará el estado que no se necesita como salida. Por lo general, esto es porque tenemos que usar un registro temporal en el ensamblado o porque las instrucciones modifican el estado que no necesitamos examinar más. Este estado generalmente se conoce como "afectado". Debemos informar al compilador de esto ya que puede necesitar guardar y restaurar este estado alrededor del bloque de ensamblado en línea.

```rust
use std::arch::asm;

# #[cfg(target_arch = "x86_64")]
fn main() {
    // tres entradas de cuatro bytes cada una
    let mut name_buf = [0_u8; 12];
    // La cadena se almacena como ascii en ebx, edx, ecx en ese orden
    // Debido a que ebx está reservado, el ensamblado debe preservar el valor de él.
    // Entonces lo empujamos y lo sacamos alrededor del ensamblado principal.
    // El modo 64 bits en procesadores de 64 bits no permite empujar/sacar
    // registros de 32 bits (como ebx), entonces tenemos que usar el registro rbx extendido en su lugar.

    unsafe {
        asm!(
            "push rbx",
            "cpuid",
            "mov [rdi], ebx",
            "mov [rdi + 4], edx",
            "mov [rdi + 8], ecx",
            "pop rbx",
            // Usamos un puntero a un array para almacenar los valores para simplificar
            // el código de Rust a costa de un par más de instrucciones de ensamblado
            // Esto es más explícito sobre cómo funciona el ensamblado, en cambio
            // a salidas de registro explícitas como `out("ecx") val`
            // El *puntero en sí mismo* solo es una entrada aunque se escribe detrás
            in("rdi") name_buf.as_mut_ptr(),
            // selecciona cpuid 0, también especifica eax como afectado
            inout("eax") 0 => _,
            // cpuid también afecta estos registros
            out("ecx") _,
            out("edx") _,
        );
    }

    let name = core::str::from_utf8(&name_buf).unwrap();
    println!("CPU Manufacturer ID: {}", name);
}

# #[cfg(not(target_arch = "x86_64"))]
# fn main() {}
```

En el ejemplo anterior, usamos la instrucción `cpuid` para leer el ID del fabricante del CPU. Esta instrucción escribe en `eax` con el argumento `cpuid` máximo admitido y en `ebx`, `edx` y `ecx` con el ID del fabricante del CPU como bytes ASCII en ese orden.

Aunque `eax` nunca se lee, todavía debemos informar al compilador de que el registro ha sido modificado para que el compilador pueda guardar cualquier valor que estaba en estos registros antes del ensamblado. Esto se hace declarándolo como una salida pero con `_` en lugar de un nombre de variable, lo que indica que el valor de salida se debe descartar.

Este código también se circunviene la limitación de que `ebx` es un registro reservado por LLVM. Eso significa que LLVM asume que tiene control total sobre el registro y que debe restaurarse a su estado original antes de salir del bloque de ensamblado, por lo que no se puede usar como entrada o salida **excepto** si el compilador lo utiliza para cumplir una clase de registro general (por ejemplo, `in(reg)`). Esto hace que los operandos `reg` sean peligrosos cuando se usan registros reservados ya que podríamos dañar sin saberlo nuestras entradas o salidas porque comparten el mismo registro.

Para evitar esto, usamos `rdi` para almacenar el puntero al array de salida, guardamos `ebx` a través de `push`, leemos de `ebx` dentro del bloque de ensamblado al array y luego restauramos `ebx` a su estado original a través de `pop`. El `push` y el `pop` usan la versión de 64 bits completa de `rbx` del registro para asegurarse de que todo el registro se guarde. En objetivos de 32 bits, el código usaría `ebx` en el `push`/`pop` en lugar de eso.

Esto también se puede usar con una clase de registro general para obtener un registro temporal para su uso dentro del código de ensamblado:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

// Multiplica x por 6 usando desplazamientos y sumas
let mut x: u64 = 4;
unsafe {
    asm!(
        "mov {tmp}, {x}",
        "shl {tmp}, 1",
        "shl {x}, 2",
        "add {x}, {tmp}",
        x = inout(reg) x,
        tmp = out(reg) _,
    );
}
assert_eq!(x, 4 * 6);
# }
```

## Operandos de símbolo y afectaciones ABI

Por defecto, `asm!` asume que cualquier registro no especificado como una salida tendrá su contenido preservado por el código de ensamblado. El argumento \[`clobber_abi`\] de `asm!` le dice al compilador que inserte automáticamente los operandos de afectación necesarios de acuerdo con la convención de llamada ABI dada: cualquier registro que no se preserva completamente en esa ABI se considerará afectado. Pueden proporcionarse múltiples argumentos `clobber_abi` y se insertarán todas las afectaciones de todas las ABIs especificadas.

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

extern "C" fn foo(arg: i32) -> i32 {
    println!("arg = {}", arg);
    arg * 2
}

fn call_foo(arg: i32) -> i32 {
    unsafe {
        let result;
        asm!(
            "call {}",
            // Puntero a la función a llamar
            in(reg) foo,
            // 1er argumento en rdi
            in("rdi") arg,
            // Valor de retorno en rax
            out("rax") result,
            // Marca todos los registros que no se preservan por la convención de llamada
            // "C" como afectados.
            clobber_abi("C"),
        );
        result
    }
}
# }
```

## Modificadores de plantilla de registro

En algunos casos, se necesita un control fino sobre la forma en que se formatea el nombre de un registro cuando se inserta en la cadena de plantilla. Esto es necesario cuando el lenguaje de ensamblado de una arquitectura tiene varios nombres para el mismo registro, cada uno generalmente siendo una "vista" sobre un subconjunto del registro (por ejemplo, los 32 bits inferiores de un registro de 64 bits).

Por defecto, el compilador siempre elegirá el nombre que se refiere al tamaño completo del registro (por ejemplo, `rax` en x86-64, `eax` en x86, etc.).

Este comportamiento predeterminado se puede anular usando modificadores en los operandos de cadena de plantilla, al igual que con las cadenas de formato:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut x: u16 = 0xab;

unsafe {
    asm!("mov {0:h}, {0:l}", inout(reg_abcd) x);
}

assert_eq!(x, 0xabab);
# }
```

En este ejemplo, usamos la clase de registro `reg_abcd` para restringir el asignador de registros a los 4 registros heredados de x86 (`ax`, `bx`, `cx`, `dx`) de los cuales los primeros dos bytes se pueden direccionar independientemente.

Supongamos que el asignador de registros ha elegido asignar `x` al registro `ax`. El modificador `h` emitirá el nombre del registro para el byte alto de ese registro y el modificador `l` emitirá el nombre del registro para el byte bajo. El código de ensamblado se expandirá entonces como `mov ah, al` que copia el byte bajo del valor al byte alto.

Si se usa un tipo de datos más pequeño (por ejemplo, `u16`) con un operando y se olvida usar modificadores de plantilla, el compilador emitirá una advertencia y sugerirá el modificador correcto para usar.

## Operandos de dirección de memoria

A veces, las instrucciones de ensamblado requieren operandos pasados a través de direcciones de memoria/localizaciones de memoria. Tienes que usar manualmente la sintaxis de dirección de memoria especificada por la arquitectura destino. Por ejemplo, en x86/x86_64 usando la sintaxis de ensamblado de Intel, debes envolver las entradas/salidas en `[]` para indicar que son operandos de memoria:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

fn load_fpu_control_word(control: u16) {
    unsafe {
        asm!("fldcw [{}]", in(reg) &control, options(nostack));
    }
}
# }
```

## Etiquetas

Cualquier reutilización de una etiqueta con nombre, local o no, puede resultar en un error del ensamblador o del enlazador o puede causar otro comportamiento extraño. La reutilización de una etiqueta con nombre puede suceder de varias maneras, incluyendo:

- explícitamente: usando una etiqueta más de una vez en un bloque `asm!`, o varias veces en bloques diferentes.
- implícitamente a través de la inlining: el compilador está permitido instanciar múltiples copias de un bloque `asm!`, por ejemplo, cuando la función que lo contiene se inlina en varios lugares.
- implícitamente a través de LTO: LTO puede causar que el código de _otros crates_ se coloque en la misma unidad de código generado, y por lo tanto podría traer etiquetas arbitrarias.

Como consecuencia, solo se deben usar etiquetas numéricas \[etiquetas locales\] del ensamblador GNU dentro del código de ensamblado en línea. Definir símbolos en el código de ensamblado puede conducir a errores del ensamblador y/o del enlazador debido a definiciones de símbolo duplicadas.

Además, en x86 cuando se usa la sintaxis Intel predeterminada, debido a \[un error de LLVM\], no se deben usar etiquetas formadas exclusivamente por dígitos `0` y `1`, por ejemplo, `0`, `11` o `101010`, ya que pueden terminar siendo interpretadas como valores binarios. Usar `options(att_syntax)` evitará cualquier ambigüedad, pero eso afecta la sintaxis de todo el bloque `asm!`. (Véase [Opciones](#opciones), a continuación, para más información sobre `options`.)

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a = 0;
unsafe {
    asm!(
        "mov {0}, 10",
        "2:",
        "sub {0}, 1",
        "cmp {0}, 3",
        "jle 2f",
        "jmp 2b",
        "2:",
        "add {0}, 2",
        out(reg) a
    );
}
assert_eq!(a, 5);
# }
```

Esto decrementará el valor del registro `{0}` de 10 a 3, luego sumará 2 y lo almacenará en `a`.

Este ejemplo muestra algunas cosas:

- Primero, que el mismo número se puede usar como etiqueta varias veces en el mismo bloque de ensamblado en línea.
- Segundo, que cuando una etiqueta numérica se usa como referencia (como un operando de instrucción, por ejemplo), se deben agregar los sufijos "b" ("hacia atrás") o "f" ("hacia adelante") a la etiqueta numérica. Entonces se referirá a la etiqueta definida por este número más cercana en esta dirección.

## Opciones

Por defecto, un bloque de ensamblado en línea se trata de la misma manera que una llamada a una función FFI externa con una convención de llamada personalizada: puede leer/escribir en memoria, tener efectos secundarios observables, etc. Sin embargo, en muchos casos es deseable dar al compilador más información sobre lo que realmente está haciendo el código de ensamblado para que pueda optimizar mejor.

Tomemos nuestro ejemplo anterior de una instrucción `add`:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a: u64 = 4;
let b: u64 = 4;
unsafe {
    asm!(
        "add {0}, {1}",
        inlateout(reg) a, in(reg) b,
        options(pure, nomem, nostack),
    );
}
assert_eq!(a, 8);
# }
```

Las opciones se pueden proporcionar como un argumento final opcional a la macro `asm!`. Especificamos tres opciones aquí:

- `pure` significa que el código de ensamblado no tiene efectos secundarios observables y que su salida depende solo de sus entradas. Esto permite que el optimizador del compilador llame menos veces al ensamblado en línea o incluso lo elimine por completo.
- `nomem` significa que el código de ensamblado no lee ni escribe en memoria. Por defecto, el compilador asumirá que el ensamblado en línea puede leer o escribir cualquier dirección de memoria accesible para él (por ejemplo, a través de un puntero pasado como un operando, o un global).
- `nostack` significa que el código de ensamblado no empuja ningún dato en la pila. Esto permite que el compilador use optimizaciones como la zona roja de la pila en x86-64 para evitar ajustes del puntero de pila.

Esto permite que el compilador optimice mejor el código que usa `asm!`, por ejemplo, eliminando bloques de `asm!` puros cuyas salidas no se necesitan.

Vea la [referencia](https://doc.rust-lang.org/stable/reference/inline-assembly.html) para la lista completa de opciones disponibles y sus efectos.
