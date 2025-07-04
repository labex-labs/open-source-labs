# 해시 맵 (Hash Maps) 에서 연관된 값과 함께 키 저장하기

마지막으로 살펴볼 일반적인 컬렉션은 *해시 맵 (hash map)*입니다. `HashMap<K, V>` 타입은 *해싱 함수 (hashing function)*를 사용하여 `K` 타입의 키를 `V` 타입의 값에 매핑하여 저장합니다. 이 해싱 함수는 이러한 키와 값을 메모리에 배치하는 방식을 결정합니다. 많은 프로그래밍 언어에서 이러한 종류의 데이터 구조를 지원하지만, _hash_, _map_, _object_, _hash table_, _dictionary_, 또는 _associative array_ 등과 같이 다른 이름을 사용하는 경우가 많습니다.

해시 맵은 벡터 (vector) 처럼 인덱스를 사용하여 데이터를 찾는 대신, 임의의 타입일 수 있는 키를 사용하여 데이터를 찾고 싶을 때 유용합니다. 예를 들어, 게임에서 각 팀의 점수를 해시 맵에 추적할 수 있습니다. 여기서 각 키는 팀 이름이고 값은 각 팀의 점수입니다. 팀 이름이 주어지면 해당 점수를 검색할 수 있습니다.

이 섹션에서는 해시 맵의 기본 API 를 살펴볼 것이지만, 표준 라이브러리의 `HashMap<K, V>`에 정의된 함수에는 더 많은 유용한 기능이 숨겨져 있습니다. 언제나 그렇듯이, 자세한 내용은 표준 라이브러리 문서를 참조하십시오.
