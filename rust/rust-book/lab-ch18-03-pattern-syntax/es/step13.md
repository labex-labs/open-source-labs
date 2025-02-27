# Partes de un valor con un \_ anidado

También podemos usar `_` dentro de otro patrón para ignorar solo parte de un valor. Por ejemplo, cuando queremos probar solo parte de un valor pero no tenemos uso de las otras partes en el código correspondiente que queremos ejecutar. La Lista 18-18 muestra el código responsable de administrar el valor de una configuración. Los requisitos comerciales son que no se debe permitir que el usuario sobrescriba una personalización existente de una configuración, pero puede anular la configuración y asignarle un valor si actualmente está sin valor.

Nombre de archivo: `src/main.rs`

```rust
let mut setting_value = Some(5);
let new_setting_value = Some(10);

match (setting_value, new_setting_value) {
    (Some(_), Some(_)) => {
        println!("No se puede sobrescribir un valor personalizado existente");
    }
    _ => {
        setting_value = new_setting_value;
    }
}

println!("configuración es {:?}", setting_value);
```

Lista 18-18: Usando un guion bajo dentro de patrones que coinciden con variantes `Some` cuando no necesitamos usar el valor dentro de `Some`

Este código imprimirá `No se puede sobrescribir un valor personalizado existente` y luego `configuración es Some(5)`. En el primer brazo de coincidencia, no necesitamos coincidir con ni usar los valores dentro de ninguna variante `Some`, pero sí necesitamos probar el caso en el que `setting_value` y `new_setting_value` son la variante `Some`. En ese caso, imprimimos la razón por la que no se cambia `setting_value`, y no se cambia.

En todos los demás casos (si `setting_value` o `new_setting_value` es `None`) expresados por el patrón `_` en el segundo brazo, queremos permitir que `new_setting_value` se convierta en `setting_value`.

También podemos usar guiones bajos en múltiples lugares dentro de un patrón para ignorar valores particulares. La Lista 18-19 muestra un ejemplo de ignorar el segundo y cuarto valores en una tupla de cinco elementos.

Nombre de archivo: `src/main.rs`

```rust
let numbers = (2, 4, 8, 16, 32);

match numbers {
    (first, _, third, _, fifth) => {
        println!("Algunos números: {first}, {third}, {fifth}");
    }
}
```

Lista 18-19: Ignorar múltiples partes de una tupla

Este código imprimirá `Algunos números: 2, 8, 32`, y los valores `4` y `16` serán ignorados.
