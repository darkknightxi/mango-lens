# Mango Lens: Mango Variety Classifier

## Overview
Mango Lens is an image classifier designed to identify the variety of mangoes based on images. This project aims to provide a simple yet effective solution for recognizing different types of mangoes, specifically Alphonso, Kesar, and Dasheri varieties. The classifier is built using a ResNet18 architecture and has been trained on a custom dataset comprising around 500 labeled mango images.

## Demo
Explore the Mango Lens in action [here](https://huggingface.co/spaces/darkknightxi/mangoes). Upload an image of a mango and let Mango Lens predict its variety.

## Dataset
The dataset used for training Mango Lens is curated using the DuckDuckGo image search API. Approximately 500 images of mangoes have been collected and labeled with the three main varieties: Alphonso, Kesar, and Dasheri.

## Training Details
Mango Lens utilizes the ResNet18 architecture for training, a popular and efficient deep learning model for image classification tasks. The training process involves four epochs, resulting in a reasonable error rate of 0.299. It's important to note that identifying mango varieties based solely on visual characteristics is a challenging task, even for experts. Given the constraints of a small dataset and the use of a relatively compact model, the achieved results are not too bad.


