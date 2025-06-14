# Enum 정의하기

구조체 (struct) 가 `width`와 `height`를 가진 `Rectangle`과 같이 관련 필드와 데이터를 함께 그룹화하는 방법을 제공하는 반면, enum 은 값이 가능한 값 집합 중 하나임을 나타내는 방법을 제공합니다. 예를 들어, `Rectangle`이 `Circle` 및 `Triangle`도 포함하는 가능한 도형 집합 중 하나라고 말하고 싶을 수 있습니다. 이를 위해 Rust 는 이러한 가능성을 enum 으로 인코딩할 수 있도록 합니다.

코드에서 표현하고 싶은 상황을 살펴보고, 이 경우 enum 이 왜 유용하고 구조체보다 더 적합한지 알아보겠습니다. IP 주소로 작업해야 한다고 가정해 봅시다. 현재 IP 주소에 사용되는 두 가지 주요 표준은 버전 4 와 버전 6 입니다. 이것이 우리 프로그램이 접하게 될 IP 주소에 대한 유일한 가능성이기 때문에, 가능한 모든 변형을 *열거 (enumerate)*할 수 있으며, 여기서 열거 (enumeration) 라는 이름이 유래되었습니다.

모든 IP 주소는 버전 4 또는 버전 6 주소일 수 있지만 동시에 둘 다일 수는 없습니다. IP 주소의 이러한 속성은 enum 데이터 구조가 적합하게 만듭니다. enum 값은 해당 변형 중 하나만 가질 수 있기 때문입니다. 버전 4 및 버전 6 주소는 여전히 근본적으로 IP 주소이므로, 코드에서 모든 종류의 IP 주소에 적용되는 상황을 처리할 때는 동일한 유형으로 처리해야 합니다.

`IpAddrKind` 열거형을 정의하고 IP 주소가 가질 수 있는 가능한 종류인 `V4`와 `V6`를 나열하여 이 개념을 코드에서 표현할 수 있습니다. 이것이 enum 의 변형입니다.

```rust
enum IpAddrKind {
    V4,
    V6,
}
```

이제 `IpAddrKind`는 코드의 다른 곳에서 사용할 수 있는 사용자 정의 데이터 유형입니다.
