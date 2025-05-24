# 조건을 만족하는 마지막 키를 찾는 함수

주어진 조건을 만족하는 객체의 마지막 키를 찾으려면 `findLastKey` 함수를 사용하십시오. 이 함수는 객체와 테스트 함수를 인수로 받습니다. 일치하는 키가 발견되면 함수는 해당 키를 반환합니다. 그렇지 않으면 `undefined`를 반환합니다. 다음은 함수가 마지막 키를 찾는 데 사용하는 단계입니다.

1. `Object.keys()`를 사용하여 객체의 모든 프로퍼티를 가져옵니다.
2. `Array.prototype.reverse()`를 사용하여 키의 순서를 반전시킵니다.
3. `Array.prototype.find()`를 사용하여 제공된 함수를 각 키 - 값 쌍에 대해 테스트합니다. 콜백 함수는 값, 키 및 객체, 이렇게 세 개의 인수를 받습니다.
4. 일치하는 키가 발견되면 해당 키를 반환합니다.

```js
const findLastKey = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .find((key) => fn(obj[key], key, obj));
```

다음은 `findLastKey`를 사용하는 예시입니다.

```js
findLastKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'pebbles'
```

이 함수를 사용하려면 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작하십시오.
