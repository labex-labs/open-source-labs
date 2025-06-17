# Introduction

In this lab, we build on our knowledge from lab 1 where we used Docker commands to run containers. We will create a custom Docker Image built from a Dockerfile. Once we build the image, we will push it to a central registry where it can be pulled to be deployed on other environments. Also, we will briefly describe image layers, and how Docker incorporates "copy-on-write" and the union file system to efficiently store images and run containers.

We will be using a few Docker commands in this lab. For full documentation on available commands check out the [official documentation](https://docs.docker.com/).

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a <span class="text-green-600 dark:text-green-400">beginner</span> level lab with a <span class="text-green-600 dark:text-green-400">82%</span> completion rate. It has received a <span class="text-primary-600 dark:text-primary-400">100%</span> positive review rate from learners.
</div>
