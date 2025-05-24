# 객체 속성에 기본값 할당 방법

`undefined`인 객체의 모든 속성에 기본값을 할당하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.assign()`을 사용하여 새로운 빈 객체를 생성하고 원래 객체를 복사하여 키 순서를 유지합니다.
3. `Array.prototype.reverse()`와 spread operator (전개 연산자, `...`) 를 사용하여 왼쪽에서 오른쪽으로 기본값을 결합합니다.
4. 마지막으로, `obj`를 다시 사용하여 원래 값을 가졌던 속성을 덮어씁니다.

다음은 코드 예시입니다.

```js
const defaults = (obj, ...defs) =>
  Object.assign({}, obj, ...defs.reverse(), obj);

defaults({ a: 1 }, { b: 2 }, { b: 6 }, { a: 3 }); // { a: 1, b: 2 }
```

이 코드 조각은 원래 객체에서 정의되지 않은 모든 속성에 대한 기본값을 가진 객체를 반환합니다.
