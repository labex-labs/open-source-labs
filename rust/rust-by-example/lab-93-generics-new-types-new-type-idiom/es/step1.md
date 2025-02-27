# Idioma de Nuevo Tipo

El idioma `newtype` ofrece garantías en tiempo de compilación de que se suministra el tipo correcto de valor a un programa.

Por ejemplo, una función de verificación de edad que comprueba la edad en años, _debe_ recibir un valor del tipo `Years`.

```rust
struct Years(i64);

struct Days(i64);

impl Years {
    pub fn to_days(&self) -> Days {
        Days(self.0 * 365)
    }
}


impl Days {
    /// truncates partial years
    pub fn to_years(&self) -> Years {
        Years(self.0 / 365)
    }
}

fn old_enough(age: &Years) -> bool {
    age.0 >= 18
}

fn main() {
    let age = Years(5);
    let age_days = age.to_days();
    println!("Old enough {}", old_enough(&age));
    println!("Old enough {}", old_enough(&age_days.to_years()));
    // println!("Old enough {}", old_enough(&age_days));
}
```

Descomente la última declaración de impresión para observar que el tipo suministrado debe ser `Years`.

Para obtener el valor del `newtype` como el tipo base, puede utilizar la sintaxis de tuplas o de desestructuración de la siguiente manera:

```rust
struct Years(i64);

fn main() {
    let years = Years(42);
    let years_as_primitive_1: i64 = years.0; // Tuple
    let Years(years_as_primitive_2) = years; // Destructuring
}
```
