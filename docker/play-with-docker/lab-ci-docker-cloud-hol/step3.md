# Configure Autobuilds

Docker Cloud can automatically build new images when updates are pushed to a repository on GitHub.

In this step, you're going to build two GitHub repositories - one for the **voting** part of the app and one for the **results** part. You'll configure two new repositories in Docker Cloud so that each time a change is pushed to the source repo an updated Docker image will be built.

1. In your web browser, return to Docker Cloud and click the **Repositories** link on the left hand side.

2. Click the **+** icon near the top right of the page and select **Repository**.

3. Enter the following information in the **Create Repository** section:

   - **Name**: results
   - **Description**: Results service for the Docker voting app
   - **Visibilty**: public

4. In the **Build Settings** section, you should see that your GitHub account is connected. Click the **GitHub icon**.

5. Make sure the your appropriate GitHub organization is populated from the drop down list, and select **voting-demo** for repository.

6. Select "Click here to customize the build settings" to configure the build rules.

7. Click **Create** at the bottom of the page.

You will be taken to the repository page.

> Right now Docker Cloud doesn't let you specify the build context when you create a repository, so you need to update the settings

8. Navigate to the Builds page and click 'Configure Automated Builds'. Scroll down to Build Rule, and set the **Build Context** to **/results**:

## Create a second repository

Repeat steps 1-8 with the following modifications:

Create Repo (Step 3)

- **Name**: voting
- **Description**: Voting service for the Docker voting app

Specify the Dockerfile path (in Step 7):

- Enter **/voting/Dockerfile** for the **Dockerfile Path**

## Check to make sure the repositories were created

If you click the **Repositories** menu on the left you should see both the `voting` and `results` respositories were created.

Well done! You've created two new repos and configured them to autobuild whenever new changes are pushed to the associated GitHub repos.
