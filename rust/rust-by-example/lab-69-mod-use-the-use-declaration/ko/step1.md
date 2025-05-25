# `use` 선언

`use` 선언은 전체 경로를 새로운 이름으로 바인딩하여 쉽게 접근할 수 있도록 사용할 수 있습니다. 일반적으로 다음과 같이 사용됩니다.

```rust
use crate::deeply::nested::{
    my_first_function,
    my_second_function,
    AndATraitType
};

fn main() {
    my_first_function();
}
```

`as` 키워드를 사용하여 가져온 항목을 다른 이름으로 바인딩할 수 있습니다.

```rust
// `deeply::nested::function` 경로를 `other_function` 으로 바인딩합니다.
use deeply::nested::function as other_function;

fn function() {
    println!("called `function()`");
}

mod deeply {
    pub mod nested {
        pub fn function() {
            println!("called `deeply::nested::function()`");
        }
    }
}

fn main() {
    // `deeply::nested::function` 에 쉽게 접근할 수 있습니다.
    other_function();

    println!("Entering block");
    {
        // 이것은 `use deeply::nested::function as function`과 동일합니다.
        // 이 `function()` 은 외부의 `function()` 을 가립니다.
        use crate::deeply::nested::function;

        // `use` 바인딩은 지역 범위를 갖습니다. 이 경우 `function()` 의 가림은 이 블록 내에서만 적용됩니다.
        function();

        println!("Leaving block");
    }

    function();
}
```
