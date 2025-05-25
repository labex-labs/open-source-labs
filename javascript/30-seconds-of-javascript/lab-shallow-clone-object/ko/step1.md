# 객체의 얕은 복사본 생성 방법

객체의 얕은 복사본을 생성하려면 `Object.assign()`과 빈 객체 (`{}`) 를 사용합니다. 다음 단계를 따르세요:

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 다음 코드를 사용하여 원본 객체의 얕은 복사본을 생성합니다:

```js
const shallowClone = (obj) => Object.assign({}, obj);
```

3. 객체를 복사하려면 다음과 같이 `shallowClone()` 함수를 사용합니다:

```js
const a = { x: true, y: 1 };
const b = shallowClone(a); // a !== b
```

이 예제에서 `a`와 `b`는 서로 다른 두 객체이지만 동일한 값을 가지고 있습니다.
