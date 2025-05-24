# 배열 요소 그룹화

원래 배열에서의 위치를 기반으로 배열 요소를 그룹화하려면 아래에 제공된 `zip` 함수를 사용하십시오.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- `zip` 함수는 `Math.max()`와 `Function.prototype.apply()`를 사용하여 인자 중 가장 긴 배열을 가져옵니다.
- 반환 값으로 해당 길이를 가진 배열을 생성하고, 매핑 함수와 함께 `Array.from()`을 사용하여 그룹화된 요소의 배열을 생성합니다.
- 인자 배열의 길이가 다를 경우, 값이 없는 위치에는 `undefined`가 사용됩니다.

```js
const zip = (...arrays) => {
  const maxLength = Math.max(...arrays.map((x) => x.length));
  return Array.from({ length: maxLength }).map((_, i) => {
    return Array.from({ length: arrays.length }, (_, k) => arrays[k][i]);
  });
};
```

사용 예시:

```js
zip(["a", "b"], [1, 2], [true, false]); // [['a', 1, true], ['b', 2, false]]
zip(["a"], [1, 2], [true, false]); // [['a', 1, true], [undefined, 2, false]]
```
