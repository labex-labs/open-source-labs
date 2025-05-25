# Unsafe 트레이트 구현

`unsafe`를 사용하여 unsafe 트레이트를 구현할 수 있습니다. 트레이트는 컴파일러가 확인할 수 없는 불변성을 하나 이상 가진 메서드가 있는 경우 unsafe 합니다. Listing 19-11 에 표시된 것처럼 `trait` 앞에 `unsafe` 키워드를 추가하고 트레이트의 구현을 `unsafe`로 표시하여 트레이트가 `unsafe`임을 선언합니다.

    unsafe trait Foo {
        // methods go here
    }

    unsafe impl Foo for i32 {
        // method implementations go here
    }

Listing 19-11: Unsafe 트레이트 정의 및 구현

`unsafe impl`을 사용함으로써 컴파일러가 확인할 수 없는 불변성을 유지하겠다고 약속하는 것입니다.

예를 들어, "Send 및 Sync 트레이트를 사용한 확장 가능한 동시성"에서 논의한 `Send` 및 `Sync` 마커 트레이트를 기억하십시오. 컴파일러는 우리의 타입이 완전히 `Send` 및 `Sync` 타입으로 구성된 경우 이러한 트레이트를 자동으로 구현합니다. 원시 포인터와 같이 `Send` 또는 `Sync`가 아닌 타입을 포함하는 타입을 구현하고 해당 타입을 `Send` 또는 `Sync`로 표시하려는 경우 `unsafe`를 사용해야 합니다. Rust 는 우리의 타입이 스레드 간에 안전하게 전송되거나 여러 스레드에서 접근될 수 있다는 보장을 유지하는지 확인할 수 없습니다. 따라서 이러한 검사를 수동으로 수행하고 `unsafe`로 표시해야 합니다.
