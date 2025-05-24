# 배열 차이 (Array Difference)

두 배열 간의 차이를 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩을 시작합니다.

2. 배열 `b`에서 `Set`을 생성하여 `b`의 고유 값을 추출합니다.

3. `Array.prototype.filter()`를 배열 `a`에 사용하여 `Set.prototype.has()`를 통해 배열 `b`에 없는 값만 유지합니다.

다음은 코드입니다.

```js
const difference = (a, b) => {
  const s = new Set(b);
  return a.filter((x) => !s.has(x));
};
```

사용 예시:

```js
difference([1, 2, 3, 3], [1, 2, 4]); // Output: [3, 3]
```
