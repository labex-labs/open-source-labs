# `super`와 `self`

`super`와 `self` 키워드는 항목에 접근할 때 모호성을 제거하고 경로의 불필요한 하드코딩을 방지하기 위해 경로에 사용될 수 있습니다.

```rust
fn function() {
    println!("called `function()`");
}

mod cool {
    pub fn function() {
        println!("called `cool::function()`");
    }
}

mod my {
    fn function() {
        println!("called `my::function()`");
    }

    mod cool {
        pub fn function() {
            println!("called `my::cool::function()`");
        }
    }

    pub fn indirect_call() {
        // 이 범위에서 `function` 이라는 이름의 모든 함수에 접근해 봅시다!
        print!("called `my::indirect_call()`, that\n> ");

        // `self` 키워드는 현재 모듈 범위 (이 경우 `my`) 를 가리킵니다.
        // `self::function()` 을 호출하는 것과 `function()` 을 직접 호출하는 것은 동일한 결과를 제공합니다. 둘 다 같은 함수를 참조하기 때문입니다.
        self::function();
        function();

        // `self` 를 사용하여 `my` 내의 다른 모듈에 접근할 수도 있습니다.
        self::cool::function();

        // `super` 키워드는 상위 범위 ( `my` 모듈 외부) 를 가리킵니다.
        super::function();

        // 이것은 *크레이트* 범위의 `cool::function` 에 바인딩됩니다.
        // 이 경우 크레이트 범위는 가장 바깥쪽 범위입니다.
        {
            use crate::cool::function as root_function;
            root_function();
        }
    }
}

fn main() {
    my::indirect_call();
}
```
