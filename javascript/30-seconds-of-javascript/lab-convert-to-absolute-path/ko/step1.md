# Node.js 에서 틸드 경로를 절대 경로로 변환하는 방법

Node.js 에서 코딩 연습을 시작하려면 터미널 또는 SSH 를 열고 `node`를 입력하십시오. 틸드 경로를 절대 경로로 변환하려면 다음 코드를 사용하십시오.

```js
const untildify = (str) =>
  str.replace(/^~($|\/|\\)/, `${require("os").homedir()}$1`);
```

이 코드는 정규 표현식과 `os.homedir()`을 사용하여 경로 시작 부분의 `~`를 홈 디렉토리로 대체합니다. 다음은 `untildify` 함수를 사용하는 예입니다.

```js
untildify("~/node"); // returns '/Users/aUser/node'
```
