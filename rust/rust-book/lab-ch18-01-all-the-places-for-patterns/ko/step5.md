# for 루프

`for` 루프에서 키워드 `for` 바로 뒤에 오는 값은 패턴입니다. 예를 들어, `for x in y`에서 `x`는 패턴입니다. Listing 18-3 은 `for` 루프에서 패턴을 사용하여 튜플을 _destructure_ (분해) 하는 방법을 보여줍니다. 이는 `for` 루프의 일부입니다.

파일 이름: `src/main.rs`

```rust
let v = vec!['a', 'b', 'c'];

for (index, value) in v.iter().enumerate() {
    println!("{value} is at index {index}");
}
```

Listing 18-3: 튜플을 destructure 하기 위해 `for` 루프에서 패턴 사용

Listing 18-3 의 코드는 다음을 출력합니다.

    a is at index 0
    b is at index 1
    c is at index 2

`enumerate` 메서드를 사용하여 반복자를 조정하여 해당 값과 해당 값의 인덱스를 생성하고, 이를 튜플에 넣습니다. 생성된 첫 번째 값은 튜플 `(0, 'a')`입니다. 이 값이 패턴 `(index, value)`와 일치하면 `index`는 `0`이 되고 `value`는 `'a'`가 되어 출력의 첫 번째 줄을 인쇄합니다.
