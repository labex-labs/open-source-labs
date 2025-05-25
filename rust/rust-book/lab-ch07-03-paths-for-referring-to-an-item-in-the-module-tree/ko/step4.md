# 구조체와 열거형을 public 으로 만들기

`pub`을 사용하여 구조체와 열거형을 public 으로 지정할 수도 있지만, 구조체 및 열거형과 함께 `pub`을 사용하는 데 몇 가지 추가 세부 사항이 있습니다. 구조체 정의 앞에 `pub`을 사용하면 구조체를 public 으로 만들지만 구조체의 필드는 여전히 private 으로 유지됩니다. 각 필드를 개별적으로 public 으로 만들거나 그렇지 않을 수 있습니다. Listing 7-9 에서 public `toast` 필드가 있지만 private `seasonal_fruit` 필드가 있는 public `back_of_house::Breakfast` 구조체를 정의했습니다. 이는 고객이 식사와 함께 제공되는 빵의 종류를 선택할 수 있지만 셰프가 계절과 재고에 따라 식사에 어떤 과일을 곁들일지 결정하는 레스토랑의 경우를 모델링합니다. 사용 가능한 과일은 빠르게 변경되므로 고객은 과일을 선택하거나 어떤 과일을 받게 될지 볼 수도 없습니다.

파일 이름: `src/lib.rs`

```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant() {
    // Order a breakfast in the summer with Rye toast
    let mut meal = back_of_house::Breakfast::summer("Rye");
    // Change our mind about what bread we'd like
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);

    // The next line won't compile if we uncomment it; we're not
    // allowed to see or modify the seasonal fruit that comes
    // with the meal
    // meal.seasonal_fruit = String::from("blueberries");
}
```

Listing 7-9: 일부 public 필드와 일부 private 필드가 있는 구조체

`back_of_house::Breakfast` 구조체의 `toast` 필드가 public 이므로 `eat_at_restaurant`에서 점 표기법을 사용하여 `toast` 필드에 쓰고 읽을 수 있습니다. `seasonal_fruit`이 private 이므로 `eat_at_restaurant`에서 `seasonal_fruit` 필드를 사용할 수 없다는 점에 유의하세요. `seasonal_fruit` 필드 값을 수정하는 줄의 주석 처리를 해제하여 어떤 오류가 발생하는지 확인해 보세요!

또한 `back_of_house::Breakfast`에 private 필드가 있으므로 구조체는 `Breakfast`의 인스턴스를 생성하는 public 연관 함수를 제공해야 합니다 (여기서는 `summer`라고 명명했습니다). `Breakfast`에 그러한 함수가 없으면 `eat_at_restaurant`에서 private `seasonal_fruit` 필드의 값을 설정할 수 없으므로 `eat_at_restaurant`에서 `Breakfast`의 인스턴스를 만들 수 없습니다.

반대로, 열거형을 public 으로 만들면 모든 변형이 public 이 됩니다. Listing 7-10 과 같이 `enum` 키워드 앞에 `pub`만 있으면 됩니다.

파일 이름: `src/lib.rs`

```rust
mod back_of_house {
    pub enum Appetizer {
        Soup,
        Salad,
    }
}

pub fn eat_at_restaurant() {
    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;
}
```

Listing 7-10: 열거형을 public 으로 지정하면 모든 변형이 public 이 됩니다.

`Appetizer` 열거형을 public 으로 만들었으므로 `eat_at_restaurant`에서 `Soup` 및 `Salad` 변형을 사용할 수 있습니다.

열거형 변형이 public 이 아니면 열거형은 그다지 유용하지 않습니다. 모든 경우에 모든 열거형 변형에 `pub`을 주석 처리해야 하는 것은 번거로울 것이므로 열거형 변형의 기본값은 public 입니다. 구조체는 필드가 public 이 아니어도 유용한 경우가 많으므로 구조체 필드는 `pub`으로 주석 처리되지 않는 한 기본적으로 모든 것이 private 이라는 일반적인 규칙을 따릅니다.

아직 다루지 않은 `pub`과 관련된 상황이 하나 더 있으며, 이는 마지막 모듈 시스템 기능인 `use` 키워드입니다. 먼저 `use` 자체를 다루고, 그 다음 `pub`과 `use`를 결합하는 방법을 보여드리겠습니다.
