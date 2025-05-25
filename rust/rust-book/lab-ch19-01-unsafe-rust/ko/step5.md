# Unsafe 코드를 통한 안전한 추상화 생성

함수에 unsafe 코드가 포함되어 있다고 해서 전체 함수를 unsafe 로 표시해야 하는 것은 아닙니다. 실제로 unsafe 코드를 안전한 함수로 래핑하는 것은 일반적인 추상화입니다. 예를 들어, unsafe 코드가 필요한 표준 라이브러리의 `split_at_mut` 함수를 살펴보겠습니다. 이를 구현하는 방법을 살펴보겠습니다. 이 안전한 메서드는 가변 슬라이스에 정의되어 있습니다. 하나의 슬라이스를 가져와 인수로 제공된 인덱스에서 슬라이스를 분할하여 두 개로 만듭니다. Listing 19-4 는 `split_at_mut`을 사용하는 방법을 보여줍니다.

```rust
let mut v = vec![1, 2, 3, 4, 5, 6];

let r = &mut v[..];

let (a, b) = r.split_at_mut(3);

assert_eq!(a, &mut [1, 2, 3]);
assert_eq!(b, &mut [4, 5, 6]);
```

Listing 19-4: 안전한 `split_at_mut` 함수 사용

안전한 Rust 만 사용하여 이 함수를 구현할 수 없습니다. 시도는 Listing 19-5 와 비슷할 수 있으며, 이는 컴파일되지 않습니다. 단순성을 위해 `split_at_mut`을 메서드가 아닌 함수로 구현하고 제네릭 타입 `T`가 아닌 `i32` 값의 슬라이스에 대해서만 구현합니다.

```rust
fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
    let len = values.len();

    assert!(mid <= len);

    (&mut values[..mid], &mut values[mid..])
}
```

Listing 19-5: 안전한 Rust 만 사용하여 `split_at_mut`을 구현하려는 시도

이 함수는 먼저 슬라이스의 총 길이를 가져옵니다. 그런 다음 매개변수로 제공된 인덱스가 슬라이스 내에 있는지, 즉 길이가 작거나 같은지 확인하여 어설션합니다. 어설션은 슬라이스를 분할할 길이보다 큰 인덱스를 전달하면 함수가 해당 인덱스를 사용하려고 시도하기 전에 패닉을 일으킨다는 것을 의미합니다.

그런 다음 튜플에서 두 개의 가변 슬라이스를 반환합니다. 하나는 원래 슬라이스의 시작 부분에서 `mid` 인덱스까지, 다른 하나는 `mid`에서 슬라이스의 끝까지입니다.

Listing 19-5 의 코드를 컴파일하려고 하면 오류가 발생합니다.

```bash
error[E0499]: cannot borrow `*values` as mutable more than once at a time
 --> src/main.rs:9:31
  |
2 |     values: &mut [i32],
  |             - let's call the lifetime of this reference `'1`
...
9 |     (&mut values[..mid], &mut values[mid..])
  |     --------------------------^^^^^^--------
  |     |     |                   |
  |     |     |                   second mutable borrow occurs here
  |     |     first mutable borrow occurs here
  |     returning this value requires that `*values` is borrowed for `'1`
```

Rust 의 borrow checker 는 슬라이스의 다른 부분을 빌리고 있다는 것을 이해할 수 없습니다. 동일한 슬라이스에서 두 번 빌리고 있다는 것만 알고 있습니다. 슬라이스의 다른 부분을 빌리는 것은 근본적으로 괜찮습니다. 두 슬라이스가 겹치지 않기 때문이지만, Rust 는 이를 알 만큼 똑똑하지 않습니다. 코드가 괜찮다는 것을 알고 있지만 Rust 가 그렇지 않은 경우, unsafe 코드를 사용해야 할 때입니다.

Listing 19-6 은 `unsafe` 블록, raw 포인터 및 일부 unsafe 함수 호출을 사용하여 `split_at_mut`의 구현이 작동하도록 하는 방법을 보여줍니다.

```rust
use std::slice;

fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
  1 let len = values.len();
  2 let ptr = values.as_mut_ptr();

  3 assert!(mid <= len);

  4 unsafe {
        (
          5 slice::from_raw_parts_mut(ptr, mid),
          6 slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}
```

Listing 19-6: `split_at_mut` 함수 구현에서 unsafe 코드 사용

"The Slice Type"에서 슬라이스는 일부 데이터에 대한 포인터와 슬라이스의 길이라는 것을 기억하십시오. `len` 메서드를 사용하여 슬라이스의 길이를 얻고 \[1] `as_mut_ptr` 메서드를 사용하여 슬라이스의 raw 포인터에 접근합니다 \[2]. 이 경우, `i32` 값에 대한 가변 슬라이스가 있으므로 `as_mut_ptr`은 `*mut i32` 유형의 raw 포인터를 반환하며, 이를 변수 `ptr`에 저장했습니다.

`mid` 인덱스가 슬라이스 내에 있다는 어설션을 유지합니다 \[3]. 그런 다음 unsafe 코드 \[4]로 이동합니다. `slice::from_raw_parts_mut` 함수는 raw 포인터와 길이를 가져와 슬라이스를 생성합니다. 이를 사용하여 `ptr`에서 시작하고 길이가 `mid`인 슬라이스를 만듭니다 \[5]. 그런 다음 `ptr`에서 `mid`를 인수로 사용하여 `add` 메서드를 호출하여 `mid`에서 시작하는 raw 포인터를 얻고, 해당 포인터와 `mid` 이후의 나머지 항목 수를 길이로 사용하여 슬라이스를 만듭니다 \[6].

`slice::from_raw_parts_mut` 함수는 raw 포인터를 가져와 이 포인터가 유효하다고 신뢰해야 하므로 unsafe 입니다. raw 포인터의 `add` 메서드도 오프셋 위치가 유효한 포인터라고 신뢰해야 하므로 unsafe 입니다. 따라서 `slice::from_raw_parts_mut` 및 `add`에 대한 호출을 둘러싸는 `unsafe` 블록을 배치하여 호출할 수 있었습니다. 코드를 살펴보고 `mid`가 `len`보다 작거나 같아야 한다는 어설션을 추가함으로써, `unsafe` 블록 내에서 사용된 모든 raw 포인터가 슬라이스 내의 데이터에 대한 유효한 포인터임을 알 수 있습니다. 이것은 `unsafe`의 적절하고 적절한 사용입니다.

결과 `split_at_mut` 함수를 `unsafe`로 표시할 필요가 없으며 안전한 Rust 에서 이 함수를 호출할 수 있다는 점에 유의하십시오. 이 함수가 접근할 수 있는 데이터에서 유효한 포인터만 생성하기 때문에, 안전한 방식으로 `unsafe` 코드를 사용하는 함수의 구현과 함께 unsafe 코드에 대한 안전한 추상화를 만들었습니다.

반대로, Listing 19-7 에서 `slice::from_raw_parts_mut`을 사용하면 슬라이스가 사용될 때 충돌이 발생할 수 있습니다. 이 코드는 임의의 메모리 위치를 가져와 길이가 10,000 개 항목인 슬라이스를 만듭니다.

```rust
use std::slice;

let address = 0x01234usize;
let r = address as *mut i32;

let values: &[i32] = unsafe {
    slice::from_raw_parts_mut(r, 10000)
};
```

Listing 19-7: 임의의 메모리 위치에서 슬라이스 생성

이 임의의 위치에 있는 메모리를 소유하지 않으며, 이 코드가 생성하는 슬라이스에 유효한 `i32` 값이 포함되어 있다는 보장이 없습니다. `values`를 유효한 슬라이스인 것처럼 사용하려고 하면 정의되지 않은 동작이 발생합니다.
