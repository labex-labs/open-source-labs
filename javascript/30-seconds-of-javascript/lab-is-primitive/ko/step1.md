# 기본 값 확인하기

코딩 연습을 위해 터미널 또는 SSH 를 열고 `node`를 입력하세요. 그런 다음, 다음 단계를 따라 값이 기본 값인지 여부를 확인할 수 있습니다.

1. `Object(val)`을 사용하여 확인하려는 값에서 객체를 생성합니다.
2. 엄격한 부등호 연산자 `!==`를 사용하여 생성된 객체와 원래 값을 비교합니다.
3. 두 값이 같지 않으면 원래 값은 기본 값입니다.

`isPrimitive` 함수의 코드는 다음과 같습니다.

```js
const isPrimitive = (val) => Object(val) !== val;
```

다음 값으로 이 함수를 테스트할 수 있습니다.

```js
isPrimitive(null); // true
isPrimitive(undefined); // true
isPrimitive(50); // true
isPrimitive("Hello!"); // true
isPrimitive(false); // true
isPrimitive(Symbol()); // true
isPrimitive([]); // false
isPrimitive({}); // false
```

확인하려는 값이 기본 값인 경우 함수는 `true`를 반환합니다. 그렇지 않으면 `false`를 반환합니다.
