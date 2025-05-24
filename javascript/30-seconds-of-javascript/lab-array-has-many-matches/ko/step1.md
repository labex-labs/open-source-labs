# 배열에 여러 일치 항목이 있는지 확인하는 함수

배열에 주어진 함수와 일치하는 값이 두 개 이상 있는지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.filter()`를 `fn`과 함께 사용하여 일치하는 모든 배열 요소를 찾습니다.
3. `Array.prototype.length`를 사용하여 `fn`과 일치하는 요소가 두 개 이상인지 확인합니다.

다음은 사용할 수 있는 코드입니다.

```js
const hasMany = (arr, fn) => arr.filter(fn).length > 1;
```

다음은 몇 가지 예시입니다.

```js
hasMany([1, 3], (x) => x % 2); // true
hasMany([1, 2], (x) => x % 2); // false
```
