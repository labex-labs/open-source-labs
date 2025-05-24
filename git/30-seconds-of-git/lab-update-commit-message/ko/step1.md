# 마지막 커밋 메시지 변경

Git 저장소에 변경 사항을 커밋했지만, 커밋 메시지에 오타가 있다는 것을 깨달았다고 가정해 봅시다. 실제로 변경한 내용은 변경하지 않고 실수를 수정하고 싶습니다. 어떻게 할 수 있을까요?

마지막 커밋 메시지를 변경하는 방법을 보여주기 위해 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다. 다음 단계를 따르세요:

1. 저장소를 복제하고, 디렉토리로 이동하여 신원을 구성합니다:
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. 마지막 커밋의 커밋 메시지를 "Fix the network bug"로 수정합니다:
   ```
   git commit --amend -m "Fix the network bug"
   ```
   이렇게 하면 기본 텍스트 편집기가 열리고 커밋 메시지를 수정할 수 있습니다. 편집기를 저장하고 닫아 프로세스를 완료합니다.
3. 커밋 메시지가 변경되었는지 확인합니다:
   ```
   git log --oneline
   ```

로그에서 업데이트된 커밋 메시지를 볼 수 있습니다:

```
54b830b (HEAD -> master) Fix the network bug
cf80005 Added file1.txt
b00b937 Initial commit
```
