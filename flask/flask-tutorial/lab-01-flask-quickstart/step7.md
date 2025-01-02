# Running the Application Again

Let's run the application again and test the dynamic content feature.

1. Stop the Flask development server if it is still running (press Ctrl+C).
2. Run the following command to start the server again:

   ```bash
   flask run --host=0.0.0.0
   ```

3. Copy the URL of the tab **Web 5000** and paste it into a new tab in your browser.

   ![Copying Web 5000 URL](./assets/copy-url.png)

4. Append `/LabEx` to the end of the URL and press Enter.

   ![Hello LabEx webpage](./assets/hello-labex.png)

5. Change the value of the `name` parameter in the URL and press Enter.
