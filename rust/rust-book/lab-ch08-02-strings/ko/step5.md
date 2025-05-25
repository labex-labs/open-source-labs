# `push_str` 및 `push`를 사용하여 문자열에 추가하기

Listing 8-15 에 표시된 것처럼 `push_str` 메서드를 사용하여 문자열 슬라이스를 추가하여 `String`을 늘릴 수 있습니다.

```rust
let mut s = String::from("foo");
s.push_str("bar");
```

Listing 8-15: `push_str` 메서드를 사용하여 문자열 슬라이스를 `String`에 추가하기

이 두 줄 이후, `s`는 `foobar`를 포함하게 됩니다. `push_str` 메서드는 매개변수의 소유권을 가져갈 필요가 없기 때문에 문자열 슬라이스를 사용합니다. 예를 들어, Listing 8-16 의 코드에서 `s2`의 내용을 `s1`에 추가한 후에도 `s2`를 사용할 수 있기를 원합니다.

```rust
let mut s1 = String::from("foo");
let s2 = "bar";
s1.push_str(s2);
println!("s2 is {s2}");
```

Listing 8-16: `String`에 내용을 추가한 후 문자열 슬라이스 사용하기

`push_str` 메서드가 `s2`의 소유권을 가져갔다면, 마지막 줄에서 해당 값을 출력할 수 없을 것입니다. 하지만 이 코드는 우리가 예상한 대로 작동합니다!

`push` 메서드는 단일 문자를 매개변수로 받아 `String`에 추가합니다. Listing 8-17 은 `push` 메서드를 사용하여 문자 *l*을 `String`에 추가합니다.

```rust
let mut s = String::from("lo");
s.push('l');
```

Listing 8-17: `push`를 사용하여 `String` 값에 문자 하나 추가하기

결과적으로, `s`는 `lol`을 포함하게 됩니다.
