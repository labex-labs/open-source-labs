# `Rc`

Когда требуется множественное владение, можно использовать `Rc` (счетчик ссылок). `Rc` отслеживает количество ссылок, то есть количество владельцев значения, обернутого в `Rc`.

Счетчик ссылок `Rc` увеличивается на 1 каждый раз, когда `Rc` клонируется, и уменьшается на 1 каждый раз, когда один клонированный `Rc` выходит из области видимости. Когда счетчик ссылок `Rc` становится равным нулю (что означает, что не осталось владельцев), и `Rc`, и значение удаляются.

Клонирование `Rc` никогда не выполняет глубокую копию. Клонирование создает только еще один указатель на обернутое значение и увеличивает счетчик.

```rust
use std::rc::Rc;

fn main() {
    let rc_examples = "Rc examples".to_string();
    {
        println!("--- rc_a is created ---");

        let rc_a: Rc<String> = Rc::new(rc_examples);
        println!("Reference Count of rc_a: {}", Rc::strong_count(&rc_a));

        {
            println!("--- rc_a is cloned to rc_b ---");

            let rc_b: Rc<String> = Rc::clone(&rc_a);
            println!("Reference Count of rc_b: {}", Rc::strong_count(&rc_b));
            println!("Reference Count of rc_a: {}", Rc::strong_count(&rc_a));

            // Два `Rc` равны, если их внутренние значения равны
            println!("rc_a and rc_b are equal: {}", rc_a.eq(&rc_b));

            // Мы можем напрямую использовать методы значения
            println!("Length of the value inside rc_a: {}", rc_a.len());
            println!("Value of rc_b: {}", rc_b);

            println!("--- rc_b is dropped out of scope ---");
        }

        println!("Reference Count of rc_a: {}", Rc::strong_count(&rc_a));

        println!("--- rc_a is dropped out of scope ---");
    }

    // Ошибка! `rc_examples` уже перемещено в `rc_a`
    // И когда `rc_a` удаляется, `rc_examples` удаляется вместе
    // println!("rc_examples: {}", rc_examples);
    // TODO ^ Попробуйте раскомментировать эту строку
}
```
