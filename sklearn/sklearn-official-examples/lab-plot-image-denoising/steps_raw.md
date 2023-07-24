# Image Denoising using Dictionary Learning

## Introduction

In this lab, we will learn how to denoise a distorted image using dictionary learning. We will use an example comparing the effect of reconstructing noisy fragments of a raccoon face image using firstly online DictionaryLearning and various transform methods.

## Steps

### Step 1: Generate Distorted Image

The first step is to generate a distorted image. We will use the Scipy dataset to load a raccoon face image. We will downsample the image to increase the speed and distort the right half of the image.

### Step 2: Display the Distorted Image

We will display the distorted image to see the effect of distortion on the image.

### Step 3: Extract Reference Patches

We will extract all reference patches from the left half of the image. We will use Scikit-learn's extract_patches_2d function to extract patches. We will normalize the data by subtracting the mean and dividing by the standard deviation.

### Step 4: Learn the Dictionary from Reference Patches

In this step, we will learn the dictionary from reference patches. We will use Scikit-learn's MiniBatchDictionaryLearning to learn the dictionary. We will fit the dictionary on the extracted patches.

### Step 5: Extract Noisy Patches and Reconstruct them using the Dictionary

In this step, we will extract noisy patches from the distorted image and reconstruct them using the dictionary. We will use four different transform algorithms, Orthogonal Matching Pursuit, Least-angle Regression, and Thresholding, to reconstruct the patches. We will display the reconstructed image and compare it with the original image.

## Summary

In this lab, we learned how to denoise a distorted image using dictionary learning. We used Scikit-learn's MiniBatchDictionaryLearning to learn the dictionary and reconstruct the noisy patches. We also used four different transform algorithms to reconstruct the patches.
