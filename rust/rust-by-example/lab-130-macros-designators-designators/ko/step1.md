# 디자인자 (Designators)

매크로의 인수는 달러 기호 `$`로 시작하고, *디자인자 (designator)*로 타입 어노테이션 (type annotated) 됩니다.

```rust
macro_rules! create_function {
    // 이 매크로는 `ident` 디자인자의 인수를 받아
    // `$func_name` 이라는 이름의 함수를 생성합니다.
    // `ident` 디자인자는 변수/함수 이름에 사용됩니다.
    ($func_name:ident) => {
        fn $func_name() {
            // `stringify!` 매크로는 `ident` 를 문자열로 변환합니다.
            println!("You called {:?}()",
                     stringify!($func_name));
        }
    };
}

// 위 매크로를 사용하여 `foo` 와 `bar` 라는 이름의 함수를 생성합니다.
create_function!(foo);
create_function!(bar);

macro_rules! print_result {
    // 이 매크로는 `expr` 타입의 표현식을 받아
    // 결과와 함께 문자열로 출력합니다.
    // `expr` 디자인자는 표현식에 사용됩니다.
    ($expression:expr) => {
        // `stringify!` 는 표현식을 *있는 그대로* 문자열로 변환합니다.
        println!("{:?} = {:?}",
                 stringify!($expression),
                 $expression);
    };
}

fn main() {
    foo();
    bar();

    print_result!(1u32 + 1);

    // 블록도 표현식이라는 것을 기억하세요!
    print_result!({
        let x = 1u32;

        x * x + 2 * x - 1
    });
}
```

다음은 사용 가능한 디자인자 (designator) 중 일부입니다.

- `block`
- `expr`는 표현식에 사용됩니다.
- `ident`는 변수/함수 이름에 사용됩니다.
- `item`
- `literal`은 리터럴 상수 (literal constants) 에 사용됩니다.
- `pat` (_패턴_)
- `path`
- `stmt` (_구문_)
- `tt` (_토큰 트리_)
- `ty` (_타입_)
- `vis` (_가시성 한정자_)

전체 목록은 \[Rust Reference]를 참조하십시오.
