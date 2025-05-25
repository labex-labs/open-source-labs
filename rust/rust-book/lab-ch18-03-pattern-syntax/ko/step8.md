# 열거형 디스트럭처링 (Destructuring Enums)

이 책에서 열거형을 디스트럭처링했습니다 (예: Listing 6-5). 하지만 열거형을 디스트럭처링하는 패턴이 열거형 내부에 저장된 데이터가 정의된 방식에 해당한다는 것을 아직 명시적으로 논의하지 않았습니다. 예를 들어, Listing 18-15 에서 Listing 6-2 의 `Message` 열거형을 사용하고 각 내부 값을 디스트럭처링하는 패턴으로 `match`를 작성합니다.

파일 이름: `src/main.rs`

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
  1 let msg = Message::ChangeColor(0, 160, 255);

    match msg {
      2 Message::Quit => {
            println!(
                "The Quit variant has no data to destructure."
            );
        }
      3 Message::Move { x, y } => {
            println!(
                "Move in the x dir {x}, in the y dir {y}"
            );
        }
      4 Message::Write(text) => {
            println!("Text message: {text}");
        }
      5 Message::ChangeColor(r, g, b) => println!(
            "Change color to red {r}, green {g}, and blue {b}"
        ),
    }
}
```

Listing 18-15: 서로 다른 종류의 값을 저장하는 열거형 변형 디스트럭처링

이 코드는 `Change color to red 0, green 160, and blue 255`를 출력합니다. `msg` \[1]의 값을 변경하여 다른 arm 의 코드가 실행되는 것을 확인해 보세요.

`Message::Quit` \[2]와 같이 데이터가 없는 열거형 변형의 경우 값을 더 이상 디스트럭처링할 수 없습니다. 리터럴 `Message::Quit` 값만 일치시킬 수 있으며 해당 패턴에는 변수가 없습니다.

`Message::Move` \[3]와 같은 구조체와 유사한 열거형 변형의 경우 구조체와 일치하도록 지정하는 패턴과 유사한 패턴을 사용할 수 있습니다. 변형 이름 뒤에 중괄호를 넣고 필드를 변수와 함께 나열하여 이 arm 에 대한 코드에서 사용할 조각을 분해합니다. 여기서는 Listing 18-13 에서 했던 것처럼 단축 형식을 사용합니다.

하나의 요소가 있는 튜플을 포함하는 `Message::Write` \[4] 및 세 개의 요소를 포함하는 튜플을 포함하는 `Message::ChangeColor` \[5]와 같은 튜플과 유사한 열거형 변형의 경우 패턴은 튜플과 일치하도록 지정하는 패턴과 유사합니다. 패턴의 변수 수는 일치하는 변형의 요소 수와 일치해야 합니다.
