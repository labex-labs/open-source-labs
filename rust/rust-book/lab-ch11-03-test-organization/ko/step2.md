# 유닛 테스트 (Unit Tests)

유닛 테스트의 목적은 코드의 각 유닛을 나머지 코드와 격리하여 테스트하여 코드가 예상대로 작동하는지 여부를 빠르게 파악하는 것입니다. 유닛 테스트는 테스트 중인 코드가 있는 각 파일의 `src` 디렉토리에 넣습니다. 규칙은 테스트 함수를 포함하는 `tests`라는 모듈을 각 파일에 생성하고 해당 모듈에 `cfg(test)`를 주석 처리하는 것입니다.
