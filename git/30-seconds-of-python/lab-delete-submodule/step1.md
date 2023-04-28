# Delete a Submodule

You have a Git repository that includes a submodule named `submodule1`. You want to delete this submodule from your repository.

For this challenge, we will use the Git repository named `https://github.com/labex-labs/git-playground`. This repository includes a submodule named `submodule1`.

To delete the `submodule1` submodule from the repository, follow these steps:

1. Open your terminal and navigate to the root directory of your Git repository.
2. Run the following command to unregister the `submodule1` submodule:

   ```
   git submodule deinit -f -- submodule1
   ```

3. Run the following command to remove the directory of the `submodule1` submodule:

   ```
   rm -rf .git/modules/submodule1
   ```

4. Run the following command to remove the working tree of the `submodule1` submodule:

   ```
   git rm -f submodule1
   ```

After completing these steps, the `submodule1` submodule will be deleted from your Git repository.
