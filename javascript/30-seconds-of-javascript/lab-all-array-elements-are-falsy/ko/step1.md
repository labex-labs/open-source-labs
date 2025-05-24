# 배열의 모든 요소가 Falsy 인지 테스트하는 함수

배열의 모든 요소가 falsy 인지 테스트하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.some()`을 사용하여 제공된 predicate 함수를 기반으로 컬렉션의 요소 중 `true`를 반환하는 요소가 있는지 테스트합니다.
3. 두 번째 인수 `fn`을 생략하면 함수는 기본적으로 `Boolean`을 사용합니다.
4. 함수는 배열의 모든 요소가 falsy 이면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.

다음은 함수의 예시 구현입니다.

```js
const none = (arr, fn = Boolean) => !arr.some(fn);
```

다음과 같이 함수를 사용할 수 있습니다.

```js
none([0, 1, 3, 0], (x) => x == 2); // true
none([0, 0, 0]); // true
```
