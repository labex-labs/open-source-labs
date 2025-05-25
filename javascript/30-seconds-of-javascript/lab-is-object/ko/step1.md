# 값이 객체인지 확인하기

전달된 값이 객체인지 확인하려면 터미널/SSH 를 열고 `node`를 입력합니다. 다음 단계가 수행됩니다.

- `Object` 생성자는 주어진 값에 대한 객체 래퍼를 생성합니다.
- 값이 `null` 또는 `undefined`인 경우 빈 객체가 생성되어 반환됩니다.
- 값이 `null` 또는 `undefined`가 아닌 경우 주어진 값에 해당하는 유형의 객체가 반환됩니다.

다음은 값이 객체인지 확인하는 예시 함수입니다.

```js
const isObject = (obj) => obj === Object(obj);
```

다음은 `isObject` 함수를 사용하는 몇 가지 예시입니다.

```js
isObject([1, 2, 3, 4]); // true
isObject([]); // true
isObject(["Hello!"]); // true
isObject({ a: 1 }); // true
isObject({}); // true
isObject(true); // false
```
