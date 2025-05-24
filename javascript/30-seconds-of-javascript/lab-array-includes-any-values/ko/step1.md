# 배열에 값이 포함되어 있는지 확인하기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

배열에 다른 배열의 요소가 하나 이상 포함되어 있는지 확인하려면 `Array.prototype.some()` 및 `Array.prototype.includes()`를 사용합니다. 다음은 예시 함수입니다.

```js
const includesAny = (arr, values) => values.some((v) => arr.includes(v));
```

이 함수를 호출하고 비교하려는 두 배열을 인수로 전달할 수 있습니다. 이 함수는 `values`의 요소 중 하나 이상이 `arr`에 포함되어 있는지 여부를 나타내는 부울 값을 반환합니다. 다음은 몇 가지 예입니다.

```js
includesAny([1, 2, 3, 4], [2, 9]); // true
includesAny([1, 2, 3, 4], [8, 9]); // false
```
