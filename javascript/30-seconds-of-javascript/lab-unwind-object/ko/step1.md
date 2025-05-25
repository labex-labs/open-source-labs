# 객체 언와인드 함수 (Unwind Object Function)

배열 값을 가진 속성을 기준으로 객체를 언와인드하려면 `unwind` 함수를 사용합니다.

- 코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
- 이 함수는 객체 구조 분해 할당 (object destructuring) 을 사용하여 객체에서 지정된 `key`에 대한 키 - 값 쌍을 제외합니다.
- 그런 다음, 주어진 `key`의 값에 대해 `Array.prototype.map()`을 사용하여 객체 배열을 생성합니다.
- 각 객체는 `key`가 개별 값에 매핑된 것을 제외하고 원래 객체의 값을 포함합니다.

```js
const unwind = (key, obj) => {
  const { [key]: _, ...rest } = obj;
  return obj[key].map((val) => ({ ...rest, [key]: val }));
};
```

사용 예시:

```js
unwind("b", { a: true, b: [1, 2] }); // [{ a: true, b: 1 }, { a: true, b: 2 }]
```
