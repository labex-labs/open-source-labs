# 커밋 되돌리기

Git 저장소에 커밋을 했지만 실수를 했다는 것을 깨달았다고 가정해 봅시다. 저장소의 기록을 다시 작성하지 않고 커밋을 되돌리고 싶습니다. 어떻게 할 수 있을까요?

커밋을 되돌리는 방법을 시연하기 위해 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다. 다음 단계를 따르세요:

1. 저장소를 복제하고, 디렉토리로 이동하여 신원을 구성합니다:
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. 커밋 기록을 봅니다:
   ```
   git log
   ```
   각각 고유 식별자 (문자와 숫자의 긴 문자열) 를 가진 커밋 목록이 표시됩니다.
3. "Added file1.txt" 메시지가 있는 커밋을 선택하고 해당 식별자를 복사합니다.
4. `git revert` 명령을 사용하여 커밋을 되돌립니다:
   ```
   git revert <commit>
   ```
   `<commit>`을 되돌리려는 커밋의 식별자로 바꿉니다.
5. Git 은 텍스트 편집기를 열고 커밋 메시지를 입력할 수 있도록 하며, 기본 메시지를 그대로 둡니다.
6. 텍스트 편집기를 저장하고 닫습니다.
7. 커밋 기록을 다시 봅니다:
   ```
   git log
   ```
   원래 커밋으로 수행된 변경 사항을 되돌리는 새 커밋이 표시됩니다.

다음은 `git log` 명령을 실행한 결과입니다:

```
commit 0d01f357a798f8960959546750d89a7e56a04a44 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 24 21:52:43 2023 +0800

    Revert "Added file1.txt"

    This reverts commit cf80005e40a3c661eb212fcea5fad06f8283f08f.
```
