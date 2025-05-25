# 값의 타입 얻는 함수

값의 타입을 얻으려면 다음 함수를 사용하십시오.

```js
const getType = (v) => {
  if (v === undefined) {
    return "undefined";
  }

  if (v === null) {
    return "null";
  }

  return v.constructor.name;
};
```

- 값이 `undefined` 또는 `null`인 경우 함수는 `'undefined'` 또는 `'null'`을 반환합니다.
- 그렇지 않으면 `Object.prototype.constructor` 및 `Function.prototype.name`을 사용하여 생성자의 이름을 반환합니다.

사용 예시:

```js
getType(new Set([1, 2, 3])); // 'Set'
```
