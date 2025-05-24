# 서브모듈 삭제

`sha1collisiondetection`이라는 서브모듈을 포함하는 Git 저장소가 있습니다. 이 서브모듈을 저장소에서 삭제하려고 합니다.

이 랩에서는 `https://github.com/git/git`이라는 Git 저장소를 사용합니다. 이 저장소에는 `sha1collisiondetection`이라는 서브모듈이 포함되어 있습니다.

저장소에서 `sha1collisiondetection` 서브모듈을 삭제하려면 다음 단계를 따르세요.

1. 터미널을 열고 Git 저장소의 루트 디렉토리로 이동합니다:
   ```
   cd git
   ```
2. 다음 명령을 실행하여 `sha1collisiondetection` 서브모듈을 등록 해제합니다:
   ```
   git submodule deinit -f -- sha1collisiondetection
   ```
3. 다음 명령을 실행하여 `sha1collisiondetection` 서브모듈의 디렉토리를 제거합니다:
   ```
   rm -rf .git/modules/sha1collisiondetection
   ```
4. 다음 명령을 실행하여 `sha1collisiondetection` 서브모듈의 작업 트리 (working tree) 를 제거합니다:
   ```
   git rm -f sha1collisiondetection
   ```

이 단계를 완료하면 `sha1collisiondetection` 서브모듈이 Git 저장소에서 제거됩니다. `git submodule status` 명령을 실행하면 서브모듈에 대한 정보가 표시되지 않습니다.
