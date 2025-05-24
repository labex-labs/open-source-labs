# 모든 배열 요소가 고유한지 확인하는 방법

배열의 모든 요소가 고유한지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 매핑된 값에서 새로운 `Set`을 생성하여 고유한 발생만 유지합니다.
3. `Array.prototype.length`와 `Set.prototype.size`를 사용하여 고유 값의 길이를 원래 배열과 비교합니다.

다음은 이러한 단계를 구현하는 예시 함수입니다.

```js
const allUnique = (arr) => arr.length === new Set(arr).size;
```

이 함수를 사용하여 배열에 모든 고유 요소가 있는지 다음과 같이 확인할 수 있습니다.

```js
allUnique([1, 2, 3, 4]); // true
allUnique([1, 1, 2, 3]); // false
```
