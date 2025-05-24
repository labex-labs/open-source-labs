# 함수를 사용하여 배열의 모든 요소가 고유한지 확인하기

제공된 매핑 함수를 기반으로 배열의 모든 요소가 고유한지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.map()` 메서드를 사용하여 제공된 함수 `fn`을 `arr` 배열의 모든 요소에 적용합니다.
3. 매핑된 값에서 새로운 `Set`을 생성하여 고유한 발생만 유지합니다.
4. `Array.prototype.length` 및 `Set.prototype.size` 메서드를 사용하여 고유하게 매핑된 값의 길이와 원래 배열의 길이를 비교합니다.

다음은 코드입니다.

```js
const allUniqueBy = (arr, fn) => arr.length === new Set(arr.map(fn)).size;
```

`allUniqueBy()` 함수를 사용하여 배열의 모든 요소가 고유한지 확인할 수 있습니다. 예를 들어:

```js
allUniqueBy([1.2, 2.4, 2.9], Math.round); // true
allUniqueBy([1.2, 2.3, 2.4], Math.round); // false
```
