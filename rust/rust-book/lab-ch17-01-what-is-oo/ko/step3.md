# 구현 세부 사항을 숨기는 캡슐화

OOP 와 일반적으로 관련된 또 다른 측면은 *캡슐화 (encapsulation)*의 개념입니다. 이는 객체의 구현 세부 사항이 해당 객체를 사용하는 코드에서 접근할 수 없다는 것을 의미합니다. 따라서 객체와 상호 작용하는 유일한 방법은 공개 API 를 통하는 것입니다. 객체를 사용하는 코드는 객체의 내부로 들어가 데이터나 동작을 직접 변경할 수 없어야 합니다. 이를 통해 프로그래머는 객체를 사용하는 코드를 변경할 필요 없이 객체의 내부를 변경하고 리팩터링할 수 있습니다.

7 장에서 캡슐화를 제어하는 방법을 논의했습니다. `pub` 키워드를 사용하여 코드에서 어떤 모듈, 타입, 함수, 메소드를 공개할지 결정할 수 있으며, 기본적으로 다른 모든 것은 비공개입니다. 예를 들어, `i32` 값의 벡터를 포함하는 필드를 가진 `AveragedCollection` 구조체를 정의할 수 있습니다. 이 구조체는 또한 벡터의 값의 평균을 포함하는 필드를 가질 수 있습니다. 즉, 누군가가 필요할 때마다 평균을 계산할 필요가 없습니다. 다시 말해, `AveragedCollection`은 계산된 평균을 캐시합니다. Listing 17-1 은 `AveragedCollection` 구조체의 정의를 보여줍니다.

파일 이름: `src/lib.rs`

```rust
pub struct AveragedCollection {
    list: Vec<i32>,
    average: f64,
}
```

Listing 17-1: 정수 목록과 컬렉션의 항목 평균을 유지하는 `AveragedCollection` 구조체

구조체는 다른 코드가 사용할 수 있도록 `pub`로 표시되지만, 구조체 내의 필드는 비공개로 유지됩니다. 이 경우, 목록에 값이 추가되거나 제거될 때마다 평균도 업데이트되도록 하려는 경우 중요합니다. Listing 17-2 에 표시된 것처럼 구조체에 `add`, `remove`, `average` 메소드를 구현하여 이를 수행합니다.

파일 이름: `src/lib.rs`

```rust
impl AveragedCollection {
    pub fn add(&mut self, value: i32) {
        self.list.push(value);
        self.update_average();
    }

    pub fn remove(&mut self) -> Option<i32> {
        let result = self.list.pop();
        match result {
            Some(value) => {
                self.update_average();
                Some(value)
            }
            None => None,
        }
    }

    pub fn average(&self) -> f64 {
        self.average
    }

    fn update_average(&mut self) {
        let total: i32 = self.list.iter().sum();
        self.average = total as f64 / self.list.len() as f64;
    }
}
```

Listing 17-2: `AveragedCollection`에 대한 공개 메소드 `add`, `remove`, `average`의 구현

공개 메소드 `add`, `remove`, `average`는 `AveragedCollection`의 인스턴스에서 데이터를 접근하거나 수정하는 유일한 방법입니다. `add` 메소드를 사용하여 `list`에 항목이 추가되거나 `remove` 메소드를 사용하여 제거될 때, 각 메소드의 구현은 `average` 필드도 업데이트하는 비공개 `update_average` 메소드를 호출합니다.

`list`와 `average` 필드를 비공개로 유지하여 외부 코드가 `list` 필드에 항목을 직접 추가하거나 제거할 수 없도록 합니다. 그렇지 않으면 `list`가 변경될 때 `average` 필드가 동기화되지 않을 수 있습니다. `average` 메소드는 `average` 필드의 값을 반환하여 외부 코드가 `average`를 읽을 수 있지만 수정할 수는 없도록 합니다.

`AveragedCollection` 구조체의 구현 세부 사항을 캡슐화했기 때문에, 데이터 구조와 같은 측면을 쉽게 변경할 수 있습니다. 예를 들어, `list` 필드에 `Vec<i32>` 대신 `HashSet<i32>`를 사용할 수 있습니다. `add`, `remove`, `average` 공개 메소드의 시그니처가 동일하게 유지되는 한, `AveragedCollection`을 사용하는 코드는 변경할 필요가 없습니다. 만약 `list`를 공개로 만들었다면, 반드시 그런 것은 아닐 것입니다. `HashSet<i32>`와 `Vec<i32>`는 항목을 추가하고 제거하는 다른 메소드를 가지고 있으므로, 외부 코드가 `list`를 직접 수정하는 경우 변경해야 할 가능성이 높습니다.

캡슐화가 언어가 객체 지향으로 간주되기 위한 필수적인 측면이라면, Rust 는 해당 요구 사항을 충족합니다. 코드의 다른 부분에 대해 `pub`를 사용할지 여부를 선택할 수 있으므로 구현 세부 사항을 캡슐화할 수 있습니다.
