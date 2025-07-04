# 공통 동작을 위한 트레이트 정의하기

`gui`가 갖기를 원하는 동작을 구현하기 위해, `draw`라는 메서드 하나를 갖는 `Draw`라는 트레이트를 정의할 것입니다. 그런 다음 *트레이트 객체*를 사용하는 벡터를 정의할 수 있습니다. 트레이트 객체는 지정된 트레이트를 구현하는 타입의 인스턴스와 런타임에 해당 타입에서 트레이트 메서드를 찾아보는 데 사용되는 테이블을 모두 가리킵니다. `&` 참조 또는 `Box<T>` 스마트 포인터와 같은 일종의 포인터를 지정한 다음 `dyn` 키워드를 지정하고 관련 트레이트를 지정하여 트레이트 객체를 생성합니다. (트레이트 객체가 "동적으로 크기가 조정된 타입과 Sized 트레이트"에서 포인터를 사용해야 하는 이유에 대해 이야기할 것입니다.) 제네릭 또는 구체적인 타입 대신 트레이트 객체를 사용할 수 있습니다. 트레이트 객체를 사용하는 곳마다 Rust 의 타입 시스템은 컴파일 시간에 해당 컨텍스트에서 사용되는 모든 값이 트레이트 객체의 트레이트를 구현하는지 확인합니다. 결과적으로 컴파일 시간에 가능한 모든 타입을 알 필요가 없습니다.

Rust 에서는 다른 언어의 객체와 구별하기 위해 구조체와 열거형을 "객체"라고 부르지 않는다고 언급했습니다. 구조체 또는 열거형에서 구조체 필드의 데이터와 `impl` 블록의 동작은 분리되어 있는 반면, 다른 언어에서는 데이터와 동작이 하나의 개념으로 결합된 것을 종종 객체라고 합니다. 그러나 트레이트 객체는 데이터와 동작을 결합한다는 점에서 다른 언어의 객체와 _더 유사합니다_. 하지만 트레이트 객체는 트레이트 객체에 데이터를 추가할 수 없다는 점에서 전통적인 객체와 다릅니다. 트레이트 객체는 다른 언어의 객체만큼 일반적으로 유용하지 않습니다. 그들의 특정 목적은 공통 동작에 대한 추상화를 허용하는 것입니다.

Listing 17-3 은 `draw`라는 메서드 하나를 가진 `Draw`라는 트레이트를 정의하는 방법을 보여줍니다.

파일 이름: `src/lib.rs`

```rust
pub trait Draw {
    fn draw(&self);
}
```

Listing 17-3: `Draw` 트레이트의 정의

이 구문은 10 장에서 트레이트를 정의하는 방법에 대한 논의에서 익숙해야 합니다. 다음은 새로운 구문입니다. Listing 17-4 는 `components`라는 벡터를 포함하는 `Screen`이라는 구조체를 정의합니다. 이 벡터는 `Box<dyn Draw>` 타입이며, 이는 트레이트 객체입니다. `Draw` 트레이트를 구현하는 `Box` 내부의 모든 타입에 대한 대리자입니다.

파일 이름: `src/lib.rs`

```rust
pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}
```

Listing 17-4: `Draw` 트레이트를 구현하는 트레이트 객체의 벡터를 포함하는 `components` 필드가 있는 `Screen` 구조체의 정의

`Screen` 구조체에서 Listing 17-5 에 표시된 것처럼 각 `components`에서 `draw` 메서드를 호출하는 `run`이라는 메서드를 정의할 것입니다.

파일 이름: `src/lib.rs`

```rust
impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Listing 17-5: 각 구성 요소에서 `draw` 메서드를 호출하는 `Screen`의 `run` 메서드

이는 트레이트 바운드가 있는 제네릭 타입 매개변수를 사용하는 구조체를 정의하는 것과는 다르게 작동합니다. 제네릭 타입 매개변수는 한 번에 하나의 구체적인 타입으로만 대체될 수 있는 반면, 트레이트 객체는 런타임에 여러 구체적인 타입이 트레이트 객체를 채울 수 있도록 허용합니다. 예를 들어, Listing 17-6 과 같이 제네릭 타입과 트레이트 바운드를 사용하여 `Screen` 구조체를 정의할 수 있습니다.

파일 이름: `src/lib.rs`

```rust
pub struct Screen<T: Draw> {
    pub components: Vec<T>,
}

impl<T> Screen<T>
where
    T: Draw,
{
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Listing 17-6: 제네릭과 트레이트 바운드를 사용하여 `Screen` 구조체와 해당 `run` 메서드의 대체 구현

이렇게 하면 모든 구성 요소가 `Button` 타입이거나 모두 `TextField` 타입인 `Screen` 인스턴스로 제한됩니다. 항상 동질적인 컬렉션만 갖게 된다면, 제네릭과 트레이트 바운드를 사용하는 것이 좋습니다. 왜냐하면 정의가 컴파일 시간에 구체적인 타입을 사용하도록 단형화되기 때문입니다.

반면에 트레이트 객체를 사용하는 메서드를 사용하면 하나의 `Screen` 인스턴스가 `Box<Button>`과 `Box<TextField>`를 모두 포함하는 `Vec<T>`를 가질 수 있습니다. 이것이 어떻게 작동하는지 살펴보고 런타임 성능 영향에 대해 이야기해 보겠습니다.
