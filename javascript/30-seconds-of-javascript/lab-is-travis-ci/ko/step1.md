# 환경이 Travis CI 인지 확인하기

Travis CI 에서 실행 중인지 확인하려면 `isTravisCI()` 함수를 사용하십시오. 이 함수는 `TRAVIS` 및 `CI` 환경 변수가 있는지 확인합니다.

```js
const isTravisCI = () => "TRAVIS" in process.env && "CI" in process.env;
```

Travis CI 에서 코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
