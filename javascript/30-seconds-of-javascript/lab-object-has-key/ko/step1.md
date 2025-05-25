# 객체가 키를 가지고 있는지 확인하는 JavaScript 함수

JavaScript 객체에 대상 값이 존재하는지 확인하려면 `hasKey` 함수를 사용하십시오.

이 함수는 두 개의 인수를 받습니다: 검색할 JSON 객체인 `obj`와 확인할 키의 배열인 `keys`. 객체에 주어진 키가 있는지 확인하는 단계는 다음과 같습니다.

1. `keys` 배열이 비어 있지 않은지 확인합니다. 비어 있다면 `false`를 반환합니다.
2. `Array.prototype.every()` 메서드를 사용하여 `keys` 배열을 반복하고 `obj`의 내부 깊이까지 각 키를 순차적으로 확인합니다.
3. `Object.prototype.hasOwnProperty()` 메서드를 사용하여 `obj`가 현재 키를 가지고 있지 않거나 객체가 아닌지 확인합니다. 이 조건 중 하나라도 참이면 전파를 중단하고 `false`를 반환합니다.
4. 그렇지 않으면, 다음 반복에서 사용할 키의 값을 `obj`에 할당합니다.
5. `keys` 배열이 성공적으로 반복되었다면 `true`를 반환합니다.

다음은 `hasKey` 함수의 코드입니다.

```js
const hasKey = (obj, keys) => {
  return (
    keys.length > 0 &&
    keys.every((key) => {
      if (typeof obj !== "object" || !obj.hasOwnProperty(key)) return false;
      obj = obj[key];
      return true;
    })
  );
};
```

다음은 `hasKey` 함수를 사용하는 몇 가지 예입니다.

```js
let obj = {
  a: 1,
  b: { c: 4 },
  "b.d": 5
};

hasKey(obj, ["a"]); // true
hasKey(obj, ["b"]); // true
hasKey(obj, ["b", "c"]); // true
hasKey(obj, ["b.d"]); // true
hasKey(obj, ["d"]); // false
hasKey(obj, ["c"]); // false
hasKey(obj, ["b", "f"]); // false
```
