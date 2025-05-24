# Git 커밋 생성하기

코드에 몇 가지 변경 사항을 적용했고, 이를 Git 저장소에 스냅샷으로 저장하고 싶습니다. 하지만, 변경한 모든 사항을 저장하는 것이 아니라, 현재 기능 또는 버그 수정과 관련된 변경 사항만 저장하고 싶습니다. 관련 변경 사항만 포함하는 커밋을 어떻게 생성할 수 있을까요?

이 랩에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다. 다음 단계를 따르세요:

1. 저장소를 복제하고 이동합니다:

   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```

2. 환경에서 GitHub 계정을 구성합니다:

   ```
   git config --global user.name "your-name"
   git config --global user.email "your-email"
   ```

3. `README.md` 파일에 "hello,labex"를 추가하고, 스테이징 영역에 추가한 다음, "Update README.md" 메시지로 커밋합니다:

   ```
   echo "hello,labex" >> README.md
   git add .
   git commit -m "Update README.md"
   ```

   `-m` 옵션을 사용하면 커밋 메시지를 지정할 수 있습니다. 메시지가 변경 사항을 설명하고 포함하는 내용을 설명하는지 확인하십시오.

다음은 `git log` 명령을 실행한 결과입니다:

![git log command output](../assets/challenge-create-commit-step1-1.png)
