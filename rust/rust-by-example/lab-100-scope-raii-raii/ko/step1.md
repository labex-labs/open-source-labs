# RAII (자원 획득은 초기화)

Rust 의 변수는 스택에 데이터를 저장하는 것 이상으로, 자원을 *소유*합니다. 예를 들어, `Box<T>`는 힙의 메모리를 소유합니다. Rust 는 RAII (Resource Acquisition Is Initialization, 자원 획득은 초기화) 를 적용하므로, 객체가 스코프를 벗어날 때마다 소멸자가 호출되고 소유된 자원이 해제됩니다.

이 동작은 _자원 누수_ 버그로부터 보호하므로, 더 이상 수동으로 메모리를 해제하거나 메모리 누수에 대해 걱정할 필요가 없습니다! 다음은 간단한 예시입니다:

```rust
// raii.rs
fn create_box() {
    // 힙에 정수를 할당합니다.
    let _box1 = Box::new(3i32);

    // `_box1` 은 여기서 파괴되고 메모리가 해제됩니다.
}

fn main() {
    // 힙에 정수를 할당합니다.
    let _box2 = Box::new(5i32);

    // 중첩된 스코프:
    {
        // 힙에 정수를 할당합니다.
        let _box3 = Box::new(4i32);

        // `_box3` 은 여기서 파괴되고 메모리가 해제됩니다.
    }

    // 재미로 많은 박스를 생성합니다.
    // 수동으로 메모리를 해제할 필요가 없습니다!
    for _ in 0u32..1_000 {
        create_box();
    }

    // `_box2` 는 여기서 파괴되고 메모리가 해제됩니다.
}
```

물론, `valgrind`를 사용하여 메모리 오류를 다시 확인할 수 있습니다:

```shell
$ rustc raii.rs && valgrind ./raii
==26873== Memcheck, a memory error detector
==26873== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==26873== Using Valgrind-3.9.0 and LibVEX; rerun with -h for copyright info
==26873== Command: ./raii
==26873==
==26873==
==26873== HEAP SUMMARY:
==26873==     in use at exit: 0 bytes in 0 blocks
==26873==   total heap usage: 1,013 allocs, 1,013 frees, 8,696 bytes allocated
==26873==
==26873== All heap blocks were freed -- no leaks are possible
==26873==
==26873== For counts of detected and suppressed errors, rerun with: -v
==26873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 2 from 2)
```

여기에는 누수가 없습니다!

## 소멸자

Rust 에서 소멸자의 개념은 \[`Drop`\] 트레이트를 통해 제공됩니다. 소멸자는 자원이 스코프를 벗어날 때 호출됩니다. 이 트레이트는 모든 타입에 대해 구현할 필요는 없으며, 자체 소멸자 로직이 필요한 경우에만 타입을 위해 구현합니다.

아래 예제를 실행하여 \[`Drop`\] 트레이트가 어떻게 작동하는지 확인하십시오. `main` 함수의 변수가 스코프를 벗어날 때 사용자 정의 소멸자가 호출됩니다.

```rust
struct ToDrop;

impl Drop for ToDrop {
    fn drop(&mut self) {
        println!("ToDrop is being dropped");
    }
}

fn main() {
    let x = ToDrop;
    println!("Made a ToDrop!");
}
```
