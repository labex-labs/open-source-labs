# 테스트 주도 개발 (Test-Driven Development)

이제 로직을 `src/lib.rs`로 추출하고 인수 수집 및 오류 처리를 `src/main.rs`에 남겨두었으므로, 코드의 핵심 기능에 대한 테스트를 훨씬 쉽게 작성할 수 있습니다. 명령줄에서 바이너리를 호출하지 않고도 다양한 인수로 함수를 직접 호출하고 반환 값을 확인할 수 있습니다.

이 섹션에서는 다음 단계를 사용하여 테스트 주도 개발 (TDD) 프로세스를 통해 `minigrep` 프로그램에 검색 로직을 추가합니다.

1.  실패하는 테스트를 작성하고 예상한 이유로 실패하는지 확인하기 위해 실행합니다.
2.  새로운 테스트를 통과시키기 위해 충분한 코드를 작성하거나 수정합니다.
3.  방금 추가하거나 변경한 코드를 리팩터링하고 테스트가 계속 통과하는지 확인합니다.
4.  1 단계부터 반복합니다!

소프트웨어를 작성하는 여러 방법 중 하나일 뿐이지만, TDD 는 코드 설계를 추진하는 데 도움이 될 수 있습니다. 테스트를 통과시키는 코드를 작성하기 전에 테스트를 작성하면 프로세스 전반에 걸쳐 높은 테스트 커버리지를 유지하는 데 도움이 됩니다.

파일 내용에서 쿼리 문자열을 실제로 검색하고 쿼리와 일치하는 줄 목록을 생성하는 기능의 구현을 테스트 주도 방식으로 개발할 것입니다. 이 기능을 `search`라는 함수에 추가할 것입니다.
