# JavaScript 에서 객체 Unflattening 방법

JavaScript 에서 키에 경로가 있는 객체를 unflatten 하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

2. 중첩된 `Array.prototype.reduce()`를 사용하여 평면 경로를 리프 노드 (leaf node) 로 변환합니다.

3. `String.prototype.split()`을 사용하여 점 구분 기호로 각 키를 분할하고 `Array.prototype.reduce()`를 사용하여 키에 대한 객체를 추가합니다.

4. 현재 누산기 (accumulator) 에 특정 키에 대한 값이 이미 포함되어 있는 경우 해당 값을 다음 누산기로 반환합니다.

5. 그렇지 않으면, 누산기 객체에 적절한 키 - 값 쌍을 추가하고 해당 값을 누산기로 반환합니다.

`unflattenObject` 함수의 코드는 다음과 같습니다.

```js
const unflattenObject = (obj) =>
  Object.keys(obj).reduce((res, k) => {
    k.split(".").reduce(
      (acc, e, i, keys) =>
        acc[e] ||
        (acc[e] = isNaN(Number(keys[i + 1]))
          ? keys.length - 1 === i
            ? obj[k]
            : {}
          : []),
      res
    );
    return res;
  }, {});
```

`unflattenObject` 함수를 사용하여 JavaScript 에서 객체를 unflatten 할 수 있습니다.

```js
unflattenObject({ "a.b.c": 1, d: 1 }); // { a: { b: { c: 1 } }, d: 1 }
unflattenObject({ "a.b": 1, "a.c": 2, d: 3 }); // { a: { b: 1, c: 2 }, d: 3 }
unflattenObject({ "a.b.0": 8, d: 3 }); // { a: { b: [ 8 ] }, d: 3 }
```
