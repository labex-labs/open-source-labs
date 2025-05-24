# 객체의 딥 클론 (Deep Clone) 지침

객체를 딥 클론하려면 다음 단계를 따르세요.

1. 새 터미널/SSH 인스턴스를 생성하고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 재귀 (recursion) 를 사용하여 기본형 (primitives), 배열 (arrays), 객체 (objects) 를 클론하되, 클래스 인스턴스 (class instances) 는 제외합니다.
3. 전달된 객체가 `null`인지 확인하고, 그렇다면 `null`을 반환합니다.
4. `Object.assign()`과 빈 객체 (`{}`) 를 사용하여 원본의 얕은 복사본 (shallow clone) 을 생성합니다.
5. `Object.keys()`와 `Array.prototype.forEach()`를 사용하여 딥 클론이 필요한 키 - 값 쌍을 결정합니다.
6. 객체가 `Array`인 경우, `clone`의 `length`를 원본의 길이로 설정하고 `Array.from()`을 사용하여 클론을 생성합니다.
7. 딥 클론을 구현하려면 다음 코드를 사용합니다.

```js
const deepClone = (obj) => {
  if (obj === null) return null;
  let clone = Object.assign({}, obj);
  Object.keys(clone).forEach(
    (key) =>
      (clone[key] =
        typeof obj[key] === "object" ? deepClone(obj[key]) : obj[key])
  );
  if (Array.isArray(obj)) {
    clone.length = obj.length;
    return Array.from(clone);
  }
  return clone;
};
```

딥 클론 함수를 테스트하려면 다음 코드를 사용합니다.

```js
const a = { foo: "bar", obj: { a: 1, b: 2 } };
const b = deepClone(a); // a !== b, a.obj !== b.obj
```
