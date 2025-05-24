# 배열에서 중복 값 확인 방법

배열에 중복된 값이 있는지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Set`을 사용하여 배열의 고유한 값을 얻습니다.
3. `Set.prototype.size`와 `Array.prototype.length`를 사용하여 고유한 값의 개수가 원래 배열의 요소 수와 동일한지 확인합니다.

다음은 배열에서 중복 값을 확인하는 예시 코드 조각입니다.

```js
const hasDuplicates = (arr) => new Set(arr).size !== arr.length;
```

다음 코드로 이 함수를 테스트할 수 있습니다.

```js
hasDuplicates([0, 1, 1, 2]); // true
hasDuplicates([0, 1, 2, 3]); // false
```

`hasDuplicates` 함수는 배열에 중복된 값이 있으면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.
