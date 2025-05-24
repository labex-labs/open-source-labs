# 객체 키 딥 매핑 (Deep Map Object Keys)

객체의 키를 딥 매핑하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 제공된 객체와 새 키를 생성하는 함수를 사용하여 `deepMapKeys` 함수를 사용합니다.
3. 이 함수는 제공된 객체와 동일한 값을 가지며, 각 키에 대해 제공된 함수를 실행하여 생성된 키를 가진 객체를 생성합니다.
4. `Object.keys()`를 사용하여 객체의 키를 반복합니다.
5. `Array.prototype.reduce()`와 제공된 함수를 사용하여 동일한 값과 매핑된 키를 가진 새 객체를 생성합니다.
6. 값이 객체인 경우, 해당 키도 매핑하기 위해 `deepMapKeys`를 재귀적으로 호출합니다.

```js
const deepMapKeys = (obj, fn) =>
  Array.isArray(obj)
    ? obj.map((val) => deepMapKeys(val, fn))
    : typeof obj === "object"
      ? Object.keys(obj).reduce((acc, current) => {
          const key = fn(current);
          const val = obj[current];
          acc[key] =
            val !== null && typeof val === "object"
              ? deepMapKeys(val, fn)
              : val;
          return acc;
        }, {})
      : obj;
```

다음은 `deepMapKeys`의 사용 예시입니다.

```js
const obj = {
  foo: "1",
  nested: {
    child: {
      withArray: [
        {
          grandChild: ["hello"]
        }
      ]
    }
  }
};

const upperKeysObj = deepMapKeys(obj, (key) => key.toUpperCase());
/*
{
  "FOO":"1",
  "NESTED":{
    "CHILD":{
      "WITHARRAY":[
        {
          "GRANDCHILD":[ 'hello' ]
        }
      ]
    }
  }
}
*/
```
