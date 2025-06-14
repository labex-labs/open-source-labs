# 통합 테스트 (Integration Tests)

Rust 에서 통합 테스트는 라이브러리와 완전히 외부적으로 존재합니다. 다른 코드와 마찬가지로 라이브러리를 사용하며, 이는 라이브러리의 공개 API 의 일부인 함수만 호출할 수 있음을 의미합니다. 통합 테스트의 목적은 라이브러리의 여러 부분이 함께 올바르게 작동하는지 테스트하는 것입니다. 자체적으로 올바르게 작동하는 코드 단위는 통합될 때 문제가 발생할 수 있으므로, 통합된 코드에 대한 테스트 커버리지도 중요합니다. 통합 테스트를 생성하려면 먼저 `tests` 디렉토리가 필요합니다.
