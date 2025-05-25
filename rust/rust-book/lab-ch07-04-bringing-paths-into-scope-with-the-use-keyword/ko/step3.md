# `as` 키워드를 사용하여 새 이름 제공

`use`를 사용하여 동일한 이름을 가진 두 개의 타입을 동일한 범위로 가져오는 문제에 대한 또 다른 해결책이 있습니다. 경로 뒤에 `as`와 새 로컬 이름, 즉 타입에 대한 *별칭 (alias)*을 지정할 수 있습니다. Listing 7-16 은 `as`를 사용하여 두 개의 `Result` 타입 중 하나를 이름을 변경하여 Listing 7-15 의 코드를 작성하는 또 다른 방법을 보여줍니다.

파일 이름: `src/lib.rs`

```rust
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> Result {
    --snip--
}

fn function2() -> IoResult<()> {
    --snip--
}
```

Listing 7-16: `as` 키워드를 사용하여 범위를 가져올 때 타입의 이름 변경

두 번째 `use` 문에서 `std::io::Result` 타입에 대한 새 이름으로 `IoResult`를 선택했습니다. 이는 또한 범위 내로 가져온 `std::fmt`의 `Result`와 충돌하지 않습니다. Listing 7-15 와 Listing 7-16 은 관용적인 것으로 간주되므로 선택은 여러분에게 달려 있습니다!
