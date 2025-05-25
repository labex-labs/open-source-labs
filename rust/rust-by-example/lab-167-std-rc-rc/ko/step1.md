# `Rc`

여러 개의 소유권이 필요할 때 `Rc`(참조 카운팅) 를 사용할 수 있습니다. `Rc`는 값이 감싸인 `Rc`의 소유자 수를 의미하는 참조 횟수를 추적합니다.

`Rc`의 참조 카운트는 `Rc`가 복제될 때마다 1 씩 증가하고, 복제된 `Rc` 중 하나가 범위를 벗어날 때마다 1 씩 감소합니다. `Rc`의 참조 카운트가 0 이 되면 (즉, 남은 소유자가 없으면) `Rc`와 값 모두 삭제됩니다.

`Rc`를 복제하는 것은 깊은 복사를 수행하지 않습니다. 복제는 감싸인 값에 대한 또 다른 포인터를 생성하고 카운트를 증가시킵니다.

```rust
use std::rc::Rc;

fn main() {
    let rc_examples = "Rc examples".to_string();
    {
        println!("--- rc_a 가 생성됨 ---");

        let rc_a: Rc<String> = Rc::new(rc_examples);
        println!("rc_a 의 참조 카운트: {}", Rc::strong_count(&rc_a));

        {
            println!("--- rc_a 가 rc_b 로 복제됨 ---");

            let rc_b: Rc<String> = Rc::clone(&rc_a);
            println!("rc_b 의 참조 카운트: {}", Rc::strong_count(&rc_b));
            println!("rc_a 의 참조 카운트: {}", Rc::strong_count(&rc_a));

            // 내부 값이 같으면 두 `Rc` 는 같습니다.
            println!("rc_a 와 rc_b 는 같음: {}", rc_a.eq(&rc_b));

            // 값의 메서드를 직접 사용할 수 있습니다.
            println!("rc_a 내부 값의 길이: {}", rc_a.len());
            println!("rc_b 의 값: {}", rc_b);

            println!("--- rc_b 가 범위를 벗어남 ---");
        }

        println!("rc_a 의 참조 카운트: {}", Rc::strong_count(&rc_a));

        println!("--- rc_a 가 범위를 벗어남 ---");
    }

    // 오류! `rc_examples` 는 이미 `rc_a` 에 이동되었습니다.
    // `rc_a` 가 삭제될 때 `rc_examples` 도 함께 삭제됩니다.
    // println!("rc_examples: {}", rc_examples);
    // TODO ^ 이 줄을 주석 해제해 보세요
}
```
