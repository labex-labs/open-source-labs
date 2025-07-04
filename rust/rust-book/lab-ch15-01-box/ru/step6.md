# Использование Box`<T>` для получения рекурсивного типа с известным размером

Поскольку Rust не может определить, сколько места нужно выделить для рекурсивно определенных типов, компилятор выдаёт ошибку с полезным советом:

    help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List`
    representable
      |
    2 |     Cons(i32, Box<List>),
      |               ++++    +

В этом совете _индиректность_ означает, что вместо прямого хранения значения мы должны изменить структуру данных для хранения значения косвенно, сохраняя указатель на значение.

Поскольку `Box<T>` - это указатель, Rust всегда знает, сколько места нужно для `Box<T>`: размер указателя не зависит от количества данных, на которые он ссылается. Это означает, что мы можем поместить `Box<T>` внутри варианта `Cons` вместо другого значения `List` напрямую. `Box<T>` будет ссылаться на следующее значение `List`, которое будет храниться в куче, а не внутри варианта `Cons`. Концептуально мы по-прежнему имеем список, созданный из списков, содержащих другие списки, но данная реализация теперь более похожа на размещение элементов рядом с каждым другом, а не внутри друг друга.

Мы можем изменить определение перечисления `List` в Листинге 15-2 и использование `List` в Листинге 15-3 на код из Листинга 15-5, который скомпилируется.

Имя файла: `src/main.rs`

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(
        1,
        Box::new(Cons(
            2,
            Box::new(Cons(
                3,
                Box::new(Nil)
            ))
        ))
    );
}
```

Листинг 15-5: Определение `List`, использующее `Box<T>`, чтобы иметь известный размер

Вариант `Cons` требует размер `i32` плюс место для хранения данных указателя коробки. Вариант `Nil` не хранит никаких значений, поэтому он требует меньше места, чем вариант `Cons`. Теперь мы знаем, что любое значение `List` займет размер `i32` плюс размер данных указателя коробки. Используя коробку, мы разбили бесконечную рекурсивную цепочку, поэтому компилятор может определить размер, необходимый для хранения значения `List`. На рисунке 15-2 показано, как выглядит вариант `Cons` теперь.

Рисунок 15-2: `List`, не имеющий бесконечного размера, потому что `Cons` содержит `Box`

Коробки обеспечивают только индиректность и выделение памяти в куче; у них нет других особых возможностей, таких как те, которые мы увидим с другими типами умных указателей. Они также не несут издержек в производительности, связанных с этими особыми возможностями, поэтому они могут быть полезны в случаях, таких как список cons, где индиректность - это единственная особенность, которую мы требуем. Мы рассмотрим больше случаев использования коробок в главе 17.

Тип `Box<T>` является умным указателем, потому что он реализует трейт `Deref`, который позволяет обрабатывать значения `Box<T>` как ссылки. Когда значение `Box<T>` выходит из области видимости, данные в куче, на которые указывает коробка, также освобождаются из-за реализации трейта `Drop`. Эти два трейта будут еще более важны для функциональности, предоставляемой другими типами умных указателей, которые мы обсудим в остальной части этой главы. Давайте более подробно рассмотрим эти два трейта.
