# Ассоциированные типы

Использование "ассоциированных типов" повышает общую читаемость кода, перемещая внутренние типы локально в трейт в качестве _типов вывода_. Синтаксис определения `trait` выглядит следующим образом:

```rust
// `A` и `B` определяются в трейте с использованием ключевого слова `type`.
// (Примечание: `type` в этом контексте отличается от `type`, когда оно используется для
// алиасов).
trait Contains {
    type A;
    type B;

    // Обновленный синтаксис для обращения к этим новым типам в общем виде.
    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
}
```

Обратите внимание, что функция, использующая `trait` `Contains`, больше не требует явного указания `A` или `B`:

```rust
// Без использования ассоциированных типов
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {... }

// Используя ассоциированные типы
fn difference<C: Contains>(container: &C) -> i32 {... }
```

Перепишем пример из предыдущего раздела с использованием ассоциированных типов:

```rust
struct Container(i32, i32);

// Трейт, который проверяет, хранятся ли 2 элемента внутри контейнера.
// Также извлекает первое или последнее значение.
trait Contains {
    // Определите общие типы здесь, которые методы смогут использовать.
    type A;
    type B;

    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
    fn first(&self) -> i32;
    fn last(&self) -> i32;
}

impl Contains for Container {
    // Укажите, какие типы `A` и `B`. Если тип `input`
    // равен `Container(i32, i32)`, то типы `output` определяются
    // как `i32` и `i32`.
    type A = i32;
    type B = i32;

    // `&Self::A` и `&Self::B` также допустимы здесь.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }
    // Возьмите первое число.
    fn first(&self) -> i32 { self.0 }

    // Возьмите последнее число.
    fn last(&self) -> i32 { self.1 }
}

fn difference<C: Contains>(container: &C) -> i32 {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

    let container = Container(number_1, number_2);

    println!("Содержит ли контейнер {} и {}: {}",
        &number_1, &number_2,
        container.contains(&number_1, &number_2));
    println!("Первое число: {}", container.first());
    println!("Последнее число: {}", container.last());

    println!("Разница составляет: {}", difference(&container));
}
```
