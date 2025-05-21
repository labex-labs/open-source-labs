# 객체 키에 접근하기

객체 키를 변환하기 전에, 키에 접근하는 방법을 이해해야 합니다. JavaScript 는 객체의 모든 키를 포함하는 배열을 반환하는 `Object.keys()` 메서드를 제공합니다.

Node.js 대화형 셸에서 다음을 시도해 보세요.

```javascript
Object.keys(user);
```

다음과 같은 출력을 볼 수 있습니다.

```
[ 'Name', 'AGE', 'Email' ]
```

이제 `toLowerCase()` 메서드를 사용하여 각 키를 소문자로 변환해 보겠습니다. `map()` 메서드를 사용하여 각 키를 변환할 수 있습니다.

```javascript
Object.keys(user).map((key) => key.toLowerCase());
```

출력은 다음과 같아야 합니다.

```
[ 'name', 'age', 'email' ]
```

훌륭합니다! 이제 모든 키가 소문자로 변환된 배열이 있습니다. 그러나 이러한 소문자 키와 원래 값을 가진 새로운 객체를 만들어야 합니다. 이를 위해 다음 단계에서 `reduce()` 메서드를 사용합니다.

계속 진행하기 전에 `reduce()` 메서드를 이해해 보겠습니다. 이 메서드는 배열의 각 요소에 대해 리듀서 함수를 실행하여 단일 출력 값을 생성합니다.

다음은 `reduce()`의 간단한 예입니다.

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue;
}, 0);

sum;
```

출력은 배열의 모든 숫자의 합인 `10`이 됩니다. `reduce()` 메서드의 `0`은 누산기 (accumulator) 의 초기 값입니다.
