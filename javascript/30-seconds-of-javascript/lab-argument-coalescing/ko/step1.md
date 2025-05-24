# 인자 병합 사용하기

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요. 인자 병합은 인자 목록에서 처음으로 정의되고 null 이 아닌 인자를 반환하는 데 사용되는 기술입니다. 이를 위해 `Array.prototype.find()`와 `Array.prototype.includes()`를 사용하여 `undefined` 또는 `null`과 같지 않은 첫 번째 값을 찾습니다.

다음은 JavaScript 에서 인자 병합을 사용하는 방법의 예입니다.

```js
const coalesce = (...args) => args.find((v) => ![undefined, null].includes(v));
```

위 코드 조각에서 `coalesce`는 임의의 수의 인자를 받아 처음으로 정의되고 null 이 아닌 인자를 반환하는 함수입니다. 다음은 `coalesce` 함수를 사용하는 방법의 예입니다.

```js
coalesce(null, undefined, "", NaN, "Waldo"); // ''
```

이 예에서 `coalesce`는 `null`, `undefined`, 빈 문자열 `''`, `NaN`, 그리고 문자열 `'Waldo'`를 포함하는 인자 목록으로 호출됩니다. 함수는 빈 문자열 `''`을 반환하는데, 이는 목록에서 처음으로 정의되고 null 이 아닌 인자이기 때문입니다.
