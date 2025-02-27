# Идиома нового типа

Идиома `newtype` обеспечивает гарантии на этапе компиляции, что в программу подается правильный тип значения.

Например, функция проверки возраста, которая проверяет возраст в годах, _должна_ получать значение типа `Years`.

```rust
struct Years(i64);

struct Days(i64);

impl Years {
    pub fn to_days(&self) -> Days {
        Days(self.0 * 365)
    }
}


impl Days {
    /// Отбрасывает дробные годы
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

Разкомментируйте последнюю инструкцию вывода, чтобы убедиться, что подаваемый тип должен быть `Years`.

Для получения значения `newtype` в виде базового типа вы можете использовать синтаксис кортежей или деструктуризации, как показано ниже:

```rust
struct Years(i64);

fn main() {
    let years = Years(42);
    let years_as_primitive_1: i64 = years.0; // Кортеж
    let Years(years_as_primitive_2) = years; // Деструктуризация
}
```
