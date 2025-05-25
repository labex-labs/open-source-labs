# 순환 JSON 문자열화 방법

순환 참조를 포함하는 JSON 객체를 문자열화하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `WeakSet.prototype.add()` 및 `WeakSet.prototype.has()`를 사용하여 확인된 값을 저장하고 검사하기 위해 `WeakSet`을 생성합니다.
3. `seen`에 이미 있는 값을 생략하고 필요한 경우 새 값을 추가하는 사용자 정의 replacer 함수와 함께 `JSON.stringify()`를 사용합니다.
4. ⚠️ **주의:** 이 함수는 순환 참조를 찾아 제거하므로 직렬화된 JSON 에서 순환 데이터 손실이 발생합니다.

`stringifyCircularJSON` 함수의 코드는 다음과 같습니다.

```js
const stringifyCircularJSON = (obj) => {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (value !== null && typeof value === "object") {
      if (seen.has(value)) return;
      seen.add(value);
    }
    return value;
  });
};
```

함수를 테스트하려면 순환 참조가 있는 객체를 생성하고 `stringifyCircularJSON`을 호출하면 됩니다.

```js
const obj = { n: 42 };
obj.obj = obj;
stringifyCircularJSON(obj); // '{"n": 42}'
```
