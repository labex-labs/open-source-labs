# Delete a Submodule

You have a Git repository that includes a submodule named `sha1collisiondetection`. You want to delete this submodule from your repository.

For this lab, we will use the Git repository named `https://github.com/git/git`. This repository includes a submodule named `sha1collisiondetection`.

To delete the `sha1collisiondetection` submodule from the repository, follow these steps:

1. Open your terminal and navigate to the root directory of your Git repository:
   ```
   cd git
   ```
2. Run the following command to unregister the `sha1collisiondetection` submodule:
   ```
   git submodule deinit -f -- sha1collisiondetection
   ```
3. Run the following command to remove the directory of the `sha1collisiondetection` submodule:
   ```
   rm -rf .git/modules/sha1collisiondetection
   ```
4. Run the following command to remove the working tree of the `sha1collisiondetection` submodule:
   ```
   git rm -f sha1collisiondetection
   ```

After these steps, the `sha1collisiondetection` submodule will be removed from your Git repository. If you run the `git submodule status` command, you won't get any information about the submodule.
