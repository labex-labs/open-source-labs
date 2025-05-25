# Match Guard 를 사용한 추가 조건 (Extra Conditionals with Match Guards)

*match guard*는 `match` arm 에서 패턴 뒤에 지정된 추가적인 `if` 조건으로, 해당 arm 이 선택되려면 일치해야 합니다. Match guard 는 패턴만으로는 표현할 수 없는 더 복잡한 아이디어를 표현하는 데 유용합니다.

조건은 패턴에서 생성된 변수를 사용할 수 있습니다. Listing 18-26 은 첫 번째 arm 에 `Some(x)` 패턴이 있고 `if x % 2 == 0`의 match guard 가 있는 `match`를 보여줍니다 (숫자가 짝수이면 `true`가 됩니다).

파일 이름: `src/main.rs`

```rust
let num = Some(4);

match num {
    Some(x) if x % 2 == 0 => println!("The number {x} is even"),
    Some(x) => println!("The number {x} is odd"),
    None => (),
}
```

Listing 18-26: 패턴에 match guard 추가하기

이 예제는 `The number 4 is even`을 출력합니다. `num`이 첫 번째 arm 의 패턴과 비교될 때, `Some(4)`가 `Some(x)`와 일치하기 때문에 일치합니다. 그런 다음 match guard 는 `x`를 2 로 나눈 나머지가 0 과 같은지 확인하고, 그렇기 때문에 첫 번째 arm 이 선택됩니다.

`num`이 대신 `Some(5)`였다면, 첫 번째 arm 의 match guard 는 5 를 2 로 나눈 나머지가 1 이고 0 과 같지 않기 때문에 `false`였을 것입니다. 그러면 Rust 는 두 번째 arm 으로 이동하며, 두 번째 arm 에는 match guard 가 없으므로 모든 `Some` 변형과 일치하기 때문에 일치합니다.

패턴 내에서 `if x % 2 == 0` 조건을 표현할 방법이 없으므로 match guard 는 이 로직을 표현할 수 있는 기능을 제공합니다. 이 추가적인 표현력의 단점은 match guard 표현식이 포함될 때 컴파일러가 완전성을 확인하려고 시도하지 않는다는 것입니다.

Listing 18-11 에서 패턴 - 섀도잉 문제를 해결하기 위해 match guard 를 사용할 수 있다고 언급했습니다. `match` 외부의 변수를 사용하는 대신 `match` 표현식의 패턴 내에서 새 변수를 생성했음을 기억하십시오. 그 새 변수는 외부 변수의 값에 대해 테스트할 수 없다는 것을 의미했습니다. Listing 18-27 은 이 문제를 해결하기 위해 match guard 를 사용하는 방법을 보여줍니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let x = Some(5);
    let y = 10;

    match x {
        Some(50) => println!("Got 50"),
        Some(n) if n == y => println!("Matched, n = {n}"),
        _ => println!("Default case, x = {:?}", x),
    }

    println!("at the end: x = {:?}, y = {y}", x);
}
```

Listing 18-27: 외부 변수와 동일성을 테스트하기 위해 match guard 사용하기

이 코드는 이제 `Default case, x = Some(5)`를 출력합니다. 두 번째 match arm 의 패턴은 외부 `y`를 섀도잉할 새 변수 `y`를 도입하지 않으므로, match guard 에서 외부 `y`를 사용할 수 있습니다. 외부 `y`를 섀도잉했을 `Some(y)`로 패턴을 지정하는 대신, `Some(n)`을 지정합니다. 이렇게 하면 `match` 외부에는 `n` 변수가 없으므로 아무것도 섀도잉하지 않는 새 변수 `n`이 생성됩니다.

match guard `if n == y`는 패턴이 아니므로 새 변수를 도입하지 않습니다. 이 `y`는 새 섀도잉된 `y`가 아닌 외부 `y`이며, `n`을 `y`와 비교하여 외부 `y`와 동일한 값을 갖는 값을 찾을 수 있습니다.

_or_ 연산자 `|`를 match guard 에서 사용하여 여러 패턴을 지정할 수도 있습니다. match guard 조건은 모든 패턴에 적용됩니다. Listing 18-28 은 `|`를 사용하는 패턴과 match guard 를 결합할 때의 우선 순위를 보여줍니다. 이 예제의 중요한 부분은 `if y` match guard 가 `4`, `5`, _and_ `6`에 적용된다는 것입니다. `if y`가 `6`에만 적용되는 것처럼 보일 수 있지만 말입니다.

파일 이름: `src/main.rs`

```rust
let x = 4;
let y = false;

match x {
    4 | 5 | 6 if y => println!("yes"),
    _ => println!("no"),
}
```

Listing 18-28: match guard 와 여러 패턴 결합하기

match 조건은 `x`의 값이 `4`, `5`, 또는 `6`과 같고 _and_ `y`가 `true`인 경우에만 arm 이 일치한다고 명시합니다. 이 코드가 실행될 때, 첫 번째 arm 의 패턴은 `x`가 `4`이기 때문에 일치하지만, match guard `if y`는 `false`이므로 첫 번째 arm 이 선택되지 않습니다. 코드는 두 번째 arm 으로 이동하며, 이는 일치하고 이 프로그램은 `no`를 출력합니다. 그 이유는 `if` 조건이 패턴 전체 `4 | 5 | 6`에 적용되기 때문이며, 마지막 값 `6`에만 적용되는 것이 아닙니다. 즉, match guard 의 우선 순위는 패턴과 관련하여 다음과 같이 동작합니다.

```rust
(4 | 5 | 6) if y => ...
```

이것이 아니라:

```rust
4 | 5 | (6 if y) => ...
```

코드를 실행한 후, 우선 순위 동작이 분명해집니다. match guard 가 `|` 연산자를 사용하여 지정된 값 목록의 마지막 값에만 적용되었다면, arm 이 일치하고 프로그램은 `yes`를 출력했을 것입니다.
