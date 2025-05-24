# 이전 브랜치로 돌아가기

개발자로서, 프로젝트를 진행하면서 새로운 기능을 작업하기 위해 다른 브랜치로 전환했다고 가정해 봅시다. 몇 가지 변경 사항을 적용한 후, 버그를 수정하기 위해 이전 브랜치로 다시 전환해야 한다는 것을 깨달았습니다. 새로운 브랜치에 변경 사항을 커밋하고 명령어를 사용하여 이전 브랜치로 빠르게 전환할 수 있습니다.

이전 브랜치로 다시 전환하는 방법을 보여주기 위해, `https://github.com/labex-labs/git-playground`라는 이름의 Git 저장소를 사용하겠습니다. 아래 단계를 따르세요:

1. 다음 명령어를 사용하여 저장소를 복제합니다:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. 저장소 디렉토리로 이동합니다:
   ```
   cd git-playground
   ```
3. `feature-branch`라는 이름의 새로운 브랜치를 생성합니다:
   ```
   git checkout -b feature-branch
   ```
4. 현재 브랜치를 확인하고 이전 브랜치로 빠르게 전환합니다. 새로운 브랜치의 이름은 `feature-branch`이고, 다시 전환하려는 이전 브랜치의 이름은 `master`입니다:
   ```
   git checkout -
   ```
   이렇게 하면 `master` 브랜치로 다시 전환되며, 변경 사항은 그대로 유지됩니다.
