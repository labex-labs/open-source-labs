# 인수 Coalescing 팩토리 코드

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 이 함수는 인수로 전달된 검증기를 기반으로 `true`로 평가되는 첫 번째 인수를 반환합니다.

```js
const coalesceFactory =
  (validator) =>
  (...args) =>
    args.find(validator);
```

`Array.prototype.find()`를 사용하여 제공된 인수 검증 함수 `valid`에서 `true`를 반환하는 첫 번째 인수를 반환합니다. 예를 들어,

```js
const customCoalesce = coalesceFactory(
  (v) => ![null, undefined, "", NaN].includes(v)
);
customCoalesce(undefined, null, NaN, "", "Waldo"); // 'Waldo'
```

여기서 `coalesceFactory` 함수는 `customCoalesce` 함수를 생성하도록 사용자 정의됩니다. `customCoalesce` 함수는 제공된 인수에서 `null`, `undefined`, `NaN`, 빈 문자열을 필터링하고 필터링되지 않은 첫 번째 인수를 반환합니다. `customCoalesce(undefined, null, NaN, '', 'Waldo')`의 출력은 `'Waldo'`입니다.
