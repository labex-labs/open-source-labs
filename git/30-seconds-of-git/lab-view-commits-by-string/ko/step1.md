# 특정 문자열을 조작한 커밋 찾기

개발자로서 코드베이스 (codebase) 에서 특정 문자열을 수정한 모든 커밋을 찾아야 할 수 있습니다. 예를 들어, 특정 함수 이름 또는 변수를 추가하거나 제거한 모든 커밋을 찾고 싶을 수 있습니다. 이는 문제를 디버깅하거나 버그의 원인을 추적할 때 유용할 수 있습니다.

GitHub 에 호스팅된 `git-playground`라는 프로젝트를 작업하고 있다고 가정해 보겠습니다. `README.md` 파일에서 "Git Playground" 문자열을 수정한 모든 커밋을 찾고 싶습니다. 방법은 다음과 같습니다.

1. 저장소 디렉토리 (repository directory) 로 이동합니다.

```shell
cd git-playground
```

2. `git log -S` 명령을 사용하여 `README.md` 파일에서 "Git Playground" 문자열을 수정한 모든 커밋을 찾고, 화살표 키를 사용하여 커밋 목록을 탐색합니다. <kbd>Q</kbd>를 눌러 로그를 종료합니다.

```shell
git log -S"Git Playground" README.md
```

Git 은 `README.md` 파일에서 "Git Playground" 문자열을 수정한 모든 커밋 목록을 출력합니다.

```shell
commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
