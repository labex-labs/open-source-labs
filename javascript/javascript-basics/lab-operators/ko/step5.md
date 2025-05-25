# 부정 (Not), 같지 않음 (Does-not-equal)

이것은 앞에 오는 값의 논리적으로 반대되는 값을 반환합니다. `true`를 `false`로, 그 반대로 바꿉니다. 동등성 연산자와 함께 사용될 때, 부정 연산자는 두 값이 같지 않은지 테스트합니다.

"Not"의 경우, 기본 표현식은 true 이지만, 비교는 `false`를 반환합니다. 왜냐하면 우리는 그것을 부정하기 때문입니다:

```js
// Not(!)
let myVariable = 3;
!(myVariable === 3);
```

"Does-not-equal"은 다른 구문을 사용하여 기본적으로 동일한 결과를 제공합니다. 여기서는 "myVariable 이 3 과 같지 않은가"를 테스트하고 있습니다. `myVariable`이 3 과 같기 때문에 이것은 `false`를 반환합니다:

```js
// Does-not-equal(!==)
let myVariable = 3;
myVariable !== 3;
```

탐구할 연산자가 훨씬 더 많지만, 지금은 이 정도면 충분합니다. 전체 목록은 [Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)를 참조하십시오.

> **참고:** 데이터 타입을 혼합하면 계산을 수행할 때 이상한 결과가 발생할 수 있습니다. 변수를 올바르게 참조하고 예상한 결과를 얻고 있는지 주의하십시오. 예를 들어, 콘솔에 `'35' + '25'`를 입력하십시오. 왜 예상한 결과를 얻지 못합니까? 따옴표가 숫자를 문자열로 바꾸기 때문에 숫자를 더하는 대신 문자열을 연결하게 되었습니다. `35 + 25`를 입력하면 두 숫자의 합계를 얻을 수 있습니다.
