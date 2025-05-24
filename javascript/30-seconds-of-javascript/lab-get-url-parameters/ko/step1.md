# URL 매개변수를 포함하는 객체

현재 URL 의 매개변수를 포함하는 객체를 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 적절한 정규 표현식과 함께 `String.prototype.match()`를 사용하여 모든 키 - 값 쌍을 추출합니다.
3. `Array.prototype.reduce()`를 사용하여 매핑하고 단일 객체로 결합합니다.
4. 현재 URL 에 적용할 인수로 `location.search`를 전달합니다.

다음은 코드입니다.

```js
const getURLParameters = (url) =>
  (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
    (a, v) => (
      (a[v.slice(0, v.indexOf("="))] = v.slice(v.indexOf("=") + 1)), a
    ),
    {}
  );
```

이 함수를 모든 URL 과 함께 사용하여 해당 매개변수를 가진 객체를 얻을 수 있습니다. 다음은 몇 가지 예입니다.

```js
getURLParameters("google.com"); // {}
getURLParameters("http://url.com/page?name=Adam&surname=Smith");
// {name: 'Adam', surname: 'Smith'}
```
