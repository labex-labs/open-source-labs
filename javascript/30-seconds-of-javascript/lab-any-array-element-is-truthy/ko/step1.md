# 배열 요소의 진실성 (Truthy) 여부 테스트

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

제공된 함수를 기반으로 컬렉션의 요소 중 하나라도 `true`를 반환하는지 확인하려면 `Array.prototype.some()`을 사용하십시오. `Boolean` 함수를 기본값으로 사용하려면 두 번째 인수 `fn`을 생략할 수 있습니다.

다음은 예제 코드입니다.

```js
const any = (arr, fn = Boolean) => arr.some(fn);
```

다음 예제를 사용하여 테스트할 수 있습니다.

```js
any([0, 1, 2, 0], (x) => x >= 2); // true
any([0, 0, 1, 0]); // true
```
