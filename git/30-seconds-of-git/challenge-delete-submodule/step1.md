# Delete a Submodule

You have a Git repository that includes a submodule named `sha1collisiondetection`. You want to delete this submodule from your repository.

## Example

For this challenge, we will use the Git repository named `https://github.com/git/git`. This repository includes a submodule named `sha1collisiondetection`.

To delete the `sha1collisiondetection` submodule from the repository, follow these steps:

1. Open your terminal and navigate to the root directory of your Git repository.
2. Unregister the `sha1collisiondetection` submodule.
3. Remove the directory of the `sha1collisiondetection` submodule.
4. Remove the working tree of the `sha1collisiondetection` submodule.

After these steps, the `sha1collisiondetection` submodule will be removed from your Git repository. If you run the `git submodule status` command, you won't get any information about the submodule.
