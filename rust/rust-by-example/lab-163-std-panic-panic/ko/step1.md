# `panic!`

`panic!` 매크로는 패닉을 발생시키고 스택 언와인딩을 시작하는 데 사용할 수 있습니다. 언와인딩 중에 런타임은 모든 객체의 소멸자를 호출하여 스레드가 소유한 모든 리소스를 해제합니다.

단일 스레드 프로그램을 다루고 있기 때문에 `panic!`는 프로그램이 패닉 메시지를 보고 종료되도록 합니다.

```rust
// 정수 나눗셈 (/) 의 재구현
fn division(dividend: i32, divisor: i32) -> i32 {
    if divisor == 0 {
        // 0 으로 나누기는 패닉을 발생시킵니다.
        panic!("division by zero");
    } else {
        dividend / divisor
    }
}

// `main` 작업
fn main() {
    // 힙 할당 정수
    let _x = Box::new(0i32);

    // 이 연산은 작업 실패를 유발합니다.
    division(3, 0);

    println!("이 지점에 도달하지 않습니다!");

    // 이 시점에서 `_x` 가 파괴되어야 합니다.
}
```

`panic!`이 메모리 누수를 일으키지 않는지 확인해 보겠습니다.

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Prevent REUSE from parsing the copyright statement in the sample code -->
```

```shell
$ rustc panic.rs && valgrind ./panic
==4401== Memcheck, a memory error detector
==4401== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==4401== Using Valgrind-3.10.0.SVN and LibVEX; rerun with -h for copyright info
==4401== Command: ./panic
==4401==
thread '<main>' panicked at 'division by zero', panic.rs:5
==4401==
==4401== HEAP SUMMARY:
==4401==     in use at exit: 0 bytes in 0 blocks
==4401==   total heap usage: 18 allocs, 18 frees, 1,648 bytes allocated
==4401==
==4401== All heap blocks were freed -- no leaks are possible
==4401==
==4401== For counts of detected and suppressed errors, rerun with: -v
==4401== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```
