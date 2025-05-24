# 누락된 서브모듈 클론

서브모듈을 포함하는 프로젝트에서 작업하고 있습니다. 프로젝트를 클론할 때, 서브모듈은 자동으로 클론되지 않습니다. 이는 프로젝트를 빌드하거나 실행하려 할 때 문제를 일으킵니다. 누락된 서브모듈을 클론하고 올바른 커밋을 체크아웃해야 합니다.

이 랩에서는 `https://github.com/git/git`이라는 Git 레포지토리를 사용합니다. 이 레포지토리는 레포지토리를 클론할 때 자동으로 클론되지 않는 서브모듈을 포함하고 있습니다.

누락된 서브모듈을 클론하고 올바른 커밋을 체크아웃하려면 다음 단계를 따르세요:

1. 레포지토리 디렉토리로 이동합니다:
   ```
   cd git
   ```
2. 서브모듈을 초기화합니다:
   ```
   git submodule update --init --recursive
   ```
3. 서브모듈의 올바른 커밋, 즉 `master` 브랜치로 체크아웃합니다:
   ```
   git submodule foreach git checkout master
   ```
   최종 결과는 다음과 같습니다:

```shell
Submodule 'sha1collisiondetection' (https://github.com/cr-marcstevens/sha1collisiondetection.git) registered for path 'sha1collisiondetection'
Cloning into '/home/labex/project/git/sha1collisiondetection'...
Submodule path 'sha1collisiondetection': checked out '855827c583bc30645ba427885caa40c5b81764d2'
```
