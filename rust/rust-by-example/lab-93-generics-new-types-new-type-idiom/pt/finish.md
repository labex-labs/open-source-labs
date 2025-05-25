# Idioma de Novo Tipo

O idiom `newtype` garante em tempo de compilação que o tipo de valor correto é fornecido a um programa.

Por exemplo, uma função de verificação de idade que verifica a idade em anos, _deve_ receber um valor do tipo `Years`.

```rust
struct Years(i64);

struct Days(i64);

impl Years {
    pub fn to_days(&self) -> Days {
        Days(self.0 * 365)
    }
}


impl Days {
    /// trunca anos parciais
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

Descomente a última instrução `println` para observar que o tipo fornecido deve ser `Years`.

Para obter o valor do `newtype` como o tipo base, pode usar a sintaxe de tupla ou desestruturação, como segue:

```rust
struct Years(i64);

fn main() {
    let years = Years(42);
    let years_as_primitive_1: i64 = years.0; // Tupla
    let Years(years_as_primitive_2) = years; // Desestruturação
}
```
