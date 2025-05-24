# 컬렉션이 비어 있는지 확인하기

컬렉션이 비어 있는지 확인하려면 터미널/SSH 를 열고 `node`를 입력합니다. 이 프로그램은 값이 빈 객체/컬렉션인지, 열거 가능한 속성이 없는지, 또는 컬렉션으로 간주되지 않는 유형인지 확인합니다.

프로그램을 사용하려면 제공된 값이 `null`인지 또는 `length`가 `0`과 같은지 확인합니다. 다음은 예시 코드입니다.

```js
const isEmpty = (val) => val == null || !(Object.keys(val) || val).length;
```

그런 다음 다음 코드를 사용하여 프로그램을 테스트할 수 있습니다.

```js
isEmpty([]); // true
isEmpty({}); // true
isEmpty(""); // true
isEmpty([1, 2]); // false
isEmpty({ a: 1, b: 2 }); // false
isEmpty("text"); // false
isEmpty(123); // true - type is not considered a collection
isEmpty(true); // true - type is not considered a collection
```
