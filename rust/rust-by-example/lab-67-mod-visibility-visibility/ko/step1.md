# 가시성

모듈 내 항목은 기본적으로 비공개 (private) 가시성을 가지지만, `pub` 수정자를 사용하여 이를 재정의할 수 있습니다. 모듈 외부에서 접근할 수 있는 것은 해당 모듈의 공개 항목 (public items) 뿐입니다.

```rust
// `my_mod` 라는 이름의 모듈
mod my_mod {
    // 모듈 내 항목은 기본적으로 비공개 가시성을 가집니다.
    fn private_function() {
        println!("called `my_mod::private_function()`");
    }

    // `pub` 수정자를 사용하여 기본 가시성을 재정의합니다.
    pub fn function() {
        println!("called `my_mod::function()`");
    }

    // 항목은 같은 모듈 내 다른 항목에 접근할 수 있습니다.
    // 비공개 항목이라도 마찬가지입니다.
    pub fn indirect_access() {
        print!("called `my_mod::indirect_access()`, that\n> ");
        private_function();
    }

    // 모듈은 중첩될 수도 있습니다.
    pub mod nested {
        pub fn function() {
            println!("called `my_mod::nested::function()`");
        }

        #[allow(dead_code)]
        fn private_function() {
            println!("called `my_mod::nested::private_function()`");
        }

        // `pub(in path)` 구문을 사용하여 선언된 함수는 지정된 경로 내에서만 표시됩니다. `path` 는 부모 또는 조상 모듈이어야 합니다.
        pub(in crate::my_mod) fn public_function_in_my_mod() {
            print!("called `my_mod::nested::public_function_in_my_mod()`, that\n> ");
            public_function_in_nested();
        }

        // `pub(self)` 구문을 사용하여 선언된 함수는 현재 모듈 내에서만 표시됩니다.
        // 이는 비공개로 남겨두는 것과 같습니다.
        pub(self) fn public_function_in_nested() {
            println!("called `my_mod::nested::public_function_in_nested()`");
        }

        // `pub(super)` 구문을 사용하여 선언된 함수는 부모 모듈 내에서만 표시됩니다.
        pub(super) fn public_function_in_super_mod() {
            println!("called `my_mod::nested::public_function_in_super_mod()`");
        }
    }

    pub fn call_public_function_in_my_mod() {
        print!("called `my_mod::call_public_function_in_my_mod()`, that\n> ");
        nested::public_function_in_my_mod();
        print!("> ");
        nested::public_function_in_super_mod();
    }

    // `pub(crate)` 는 함수가 현재 크레이트 내에서만 표시되도록 합니다.
    pub(crate) fn public_function_in_crate() {
        println!("called `my_mod::public_function_in_crate()`");
    }

    // 중첩된 모듈도 가시성 규칙을 따릅니다.
    mod private_nested {
        #[allow(dead_code)]
        pub fn function() {
            println!("called `my_mod::private_nested::function()`");
        }

        // 비공개 부모 항목은 더 큰 범위 내에서 표시되도록 선언되어도 자식 항목의 가시성을 여전히 제한합니다.
        #[allow(dead_code)]
        pub(crate) fn restricted_function() {
            println!("called `my_mod::private_nested::restricted_function()`");
        }
    }
}

fn function() {
    println!("called `function()`");
}

fn main() {
    // 모듈은 동일한 이름을 가진 항목 간의 모호성을 해결하는 데 도움이 됩니다.
    function();
    my_mod::function();

    // 중첩된 모듈 내의 공개 항목을 포함하여 공개 항목은 부모 모듈 외부에서도 접근할 수 있습니다.
    my_mod::indirect_access();
    my_mod::nested::function();
    my_mod::call_public_function_in_my_mod();

    // pub(crate) 항목은 같은 크레이트 내 어디에서나 호출할 수 있습니다.
    my_mod::public_function_in_crate();

    // pub(in path) 항목은 지정된 모듈 내에서만 호출할 수 있습니다.
    // 오류! 함수 `public_function_in_my_mod` 는 비공개입니다.
    //my_mod::nested::public_function_in_my_mod();
    // TODO ^ 이 줄을 주석 해제해 보세요

    // 모듈의 비공개 항목은 직접 접근할 수 없습니다.
    // 오류! `private_function` 은 비공개입니다.
    //my_mod::private_function();
    // TODO ^ 이 줄을 주석 해제해 보세요

    // 오류! `private_function` 은 비공개입니다.
    //my_mod::nested::private_function();
    // TODO ^ 이 줄을 주석 해제해 보세요

    // 오류! `private_nested` 는 비공개 모듈입니다.
    //my_mod::private_nested::function();
    // TODO ^ 이 줄을 주석 해제해 보세요

    // 오류! `private_nested` 는 비공개 모듈입니다.
    //my_mod::private_nested::restricted_function();
    // TODO ^ 이 줄을 주석 해제해 보세요
}
```
