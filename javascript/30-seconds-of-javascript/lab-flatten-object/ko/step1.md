# 객체 평탄화

키 경로를 사용하여 객체를 평탄화하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 재귀를 사용하여 객체를 평탄화합니다.
3. `Object.keys()`를 `Array.prototype.reduce()`와 결합하여 모든 리프 노드를 평탄화된 경로 노드로 변환합니다.
4. 키의 값이 객체인 경우, `Object.assign()`을 사용하여 경로를 생성하기 위해 적절한 `prefix`와 함께 함수를 재귀적으로 호출합니다.
5. 그렇지 않으면, 적절한 접두사가 붙은 키 - 값 쌍을 누산기 객체에 추가합니다.
6. 모든 키에 접두사를 지정하려는 경우가 아니면 두 번째 인수 `prefix`를 생략합니다.

다음은 구현 예시입니다.

```js
const flattenObject = (obj, prefix = "") =>
  Object.keys(obj).reduce((acc, k) => {
    const pre = prefix.length ? `${prefix}.` : "";
    if (
      typeof obj[k] === "object" &&
      obj[k] !== null &&
      Object.keys(obj[k]).length > 0
    ) {
      Object.assign(acc, flattenObject(obj[k], pre + k));
    } else {
      acc[pre + k] = obj[k];
    }
    return acc;
  }, {});
```

`flattenObject` 함수는 다음과 같이 사용할 수 있습니다.

```js
flattenObject({ a: { b: { c: 1 } }, d: 1 }); // { 'a.b.c': 1, d: 1 }
```
