# 클로저로 환경 캡처하기

먼저 클로저를 사용하여 정의된 환경에서 값을 캡처하여 나중에 사용하는 방법을 살펴보겠습니다. 시나리오는 다음과 같습니다. 우리 티셔츠 회사는 프로모션으로 메일링 리스트에 있는 사람에게 독점적인 한정판 셔츠를 가끔씩 증정합니다. 메일링 리스트에 있는 사람들은 프로필에 자신이 좋아하는 색상을 선택적으로 추가할 수 있습니다. 무료 셔츠를 받을 사람의 선호하는 색상이 설정되어 있으면 해당 색상의 셔츠를 받습니다. 선호하는 색상을 지정하지 않은 사람은 회사에서 현재 가장 많이 보유하고 있는 색상의 셔츠를 받습니다.

이것을 구현하는 방법은 여러 가지가 있습니다. 이 예제에서는 `Red`와 `Blue` 변형을 가진 `ShirtColor`라는 enum 을 사용합니다 (단순화를 위해 사용 가능한 색상 수를 제한). 회사의 재고는 현재 재고에 있는 셔츠 색상을 나타내는 `Vec<ShirtColor>` 필드인 `shirts`를 가진 `Inventory` 구조체로 나타냅니다. `Inventory`에 정의된 `giveaway` 메서드는 무료 셔츠 당첨자의 선택적 셔츠 색상 선호도를 가져와서 해당 사람이 받게 될 셔츠 색상을 반환합니다. 이 설정은 Listing 13-1 에 나와 있습니다.

파일 이름: `src/main.rs`

```rust
#[derive(Debug, PartialEq, Copy, Clone)]
enum ShirtColor {
    Red,
    Blue,
}

struct Inventory {
    shirts: Vec<ShirtColor>,
}

impl Inventory {
    fn giveaway(
        &self,
        user_preference: Option<ShirtColor>,
    ) -> ShirtColor {
      1 user_preference.unwrap_or_else(|| self.most_stocked())
    }

    fn most_stocked(&self) -> ShirtColor {
        let mut num_red = 0;
        let mut num_blue = 0;

        for color in &self.shirts {
            match color {
                ShirtColor::Red => num_red += 1,
                ShirtColor::Blue => num_blue += 1,
            }
        }
        if num_red > num_blue {
            ShirtColor::Red
        } else {
            ShirtColor::Blue
        }
    }
}

fn main() {
    let store = Inventory {
      2 shirts: vec![
            ShirtColor::Blue,
            ShirtColor::Red,
            ShirtColor::Blue,
        ],
    };

    let user_pref1 = Some(ShirtColor::Red);
  3 let giveaway1 = store.giveaway(user_pref1);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref1, giveaway1
    );

    let user_pref2 = None;
  4 let giveaway2 = store.giveaway(user_pref2);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref2, giveaway2
    );
}
```

Listing 13-1: 셔츠 회사 증정 행사

`main`에 정의된 `store`는 이 한정판 프로모션을 위해 배포할 파란색 셔츠 2 개와 빨간색 셔츠 1 개를 가지고 있습니다 \[2]. 빨간색 셔츠를 선호하는 사용자와 \[3] 선호하는 색상이 없는 사용자 \[4]에 대해 `giveaway` 메서드를 호출합니다.

다시 말하지만, 이 코드는 여러 가지 방법으로 구현할 수 있으며, 여기서는 클로저에 집중하기 위해 `giveaway` 메서드의 본문을 제외하고 이미 배운 개념을 고수했습니다. `giveaway` 메서드에서 `Option<ShirtColor>` 유형의 매개변수로 사용자 선호도를 가져와 `user_preference`에서 `unwrap_or_else` 메서드를 호출합니다 \[1]. `Option<T>`에 대한 `unwrap_or_else` 메서드는 표준 라이브러리에 의해 정의됩니다. 이 메서드는 인수를 하나 받습니다. 즉, 인수가 없는 클로저로, 값 `T`를 반환합니다 (이 경우 `ShirtColor`인 `Option<T>`의 `Some` 변형에 저장된 동일한 유형). `Option<T>`가 `Some` 변형이면 `unwrap_or_else`는 `Some` 내부의 값을 반환합니다. `Option<T>`가 `None` 변형이면 `unwrap_or_else`는 클로저를 호출하고 클로저에서 반환된 값을 반환합니다.

`unwrap_or_else`의 인수로 클로저 표현식 `|| self.most_stocked()`를 지정합니다. 이것은 자체적으로 매개변수를 받지 않는 클로저입니다 (클로저에 매개변수가 있는 경우 두 수직 파이프 사이에 나타납니다). 클로저의 본문은 `self.most_stocked()`를 호출합니다. 여기서 클로저를 정의하고, `unwrap_or_else`의 구현은 결과가 필요한 경우 나중에 클로저를 평가합니다.

이 코드를 실행하면 다음이 출력됩니다.

```rust
The user with preference Some(Red) gets Red
The user with preference None gets Blue
```

여기서 한 가지 흥미로운 점은 현재 `Inventory` 인스턴스에서 `self.most_stocked()`를 호출하는 클로저를 전달했다는 것입니다. 표준 라이브러리는 우리가 정의한 `Inventory` 또는 `ShirtColor` 유형이나 이 시나리오에서 사용하려는 로직에 대해 아무것도 알 필요가 없었습니다. 클로저는 `self` `Inventory` 인스턴스에 대한 불변 참조를 캡처하고 우리가 `unwrap_or_else` 메서드에 지정한 코드와 함께 전달합니다. 반면에 함수는 이러한 방식으로 환경을 캡처할 수 없습니다.
