# 조건부 if let (if let) 표현식

6 장에서 `if let` 표현식을 주로 하나의 경우만 일치하는 `match`의 동등한 표현을 작성하는 더 짧은 방법으로 사용하는 방법에 대해 논의했습니다. 선택적으로, `if let`은 `if let`의 패턴이 일치하지 않는 경우 실행할 코드를 포함하는 해당 `else`를 가질 수 있습니다.

Listing 18-1 은 `if let`, `else if`, `else if let` 표현식을 혼합하고 일치시키는 것도 가능하다는 것을 보여줍니다. 이렇게 하면 패턴과 비교할 하나의 값만 표현할 수 있는 `match` 표현식보다 더 많은 유연성을 얻을 수 있습니다. 또한 Rust 는 일련의 `if let`, `else if`, `else if let` 분기의 조건이 서로 관련되어야 한다고 요구하지 않습니다.

Listing 18-1 의 코드는 여러 조건에 대한 일련의 검사를 기반으로 배경색을 결정합니다. 이 예제에서는 실제 프로그램이 사용자 입력에서 받을 수 있는 하드 코딩된 값을 가진 변수를 만들었습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let favorite_color: Option<&str> = None;
    let is_tuesday = false;
    let age: Result<u8, _> = "34".parse();

  1 if let Some(color) = favorite_color {
      2 println!(
            "Using your favorite, {color}, as the background"
        );
  3 } else if is_tuesday {
      4 println!("Tuesday is green day!");
  5 } else if let Ok(age) = age {
      6 if age > 30 {
          7 println!("Using purple as the background color");
        } else {
          8 println!("Using orange as the background color");
        }
  9 } else {
     10 println!("Using blue as the background color");
    }
}
```

Listing 18-1: `if let`, `else if`, `else if let`, 및 `else` 혼합

사용자가 좋아하는 색상을 지정하면 \[1] 해당 색상이 배경으로 사용됩니다 \[2]. 좋아하는 색상이 지정되지 않았고 오늘이 화요일인 경우 \[3] 배경색은 녹색입니다 \[4]. 그렇지 않고 사용자가 나이를 문자열로 지정하고 이를 숫자로 성공적으로 구문 분석할 수 있는 경우 \[5] 숫자의 값에 따라 색상은 보라색 \[7] 또는 주황색 \[8]입니다 \[6]. 이러한 조건이 적용되지 않으면 \[9] 배경색은 파란색입니다 \[10].

이 조건부 구조를 통해 복잡한 요구 사항을 지원할 수 있습니다. 여기에 있는 하드 코딩된 값을 사용하면 이 예제는 `Using purple as the background color`를 출력합니다.

`if let`은 `match` 분기가 할 수 있는 것과 동일한 방식으로 그림자 변수를 도입할 수도 있습니다. `if let Ok(age) = age` 라인 \[5]은 `Ok` 변형 내의 값을 포함하는 새로운 그림자 `age` 변수를 도입합니다. 즉, `if age > 30` 조건 \[6]을 해당 블록 내에 배치해야 합니다. 이 두 조건을 `if let Ok(age) = age && age > 30`으로 결합할 수 없습니다. 30 과 비교하려는 그림자 `age`는 새 범위가 중괄호로 시작될 때까지 유효하지 않습니다.

`if let` 표현식을 사용하는 단점은 컴파일러가 exhaustiveness (전체성) 을 확인하지 않는다는 것입니다. 반면 `match` 표현식에서는 확인합니다. 마지막 `else` 블록 \[9]을 생략하여 일부 경우를 처리하지 못한 경우 컴파일러는 가능한 논리 버그에 대해 경고하지 않습니다.
