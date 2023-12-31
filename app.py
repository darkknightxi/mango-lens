# -*- coding: utf-8 -*-
"""Deployment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v3NvxXElYmSzyH24hrIwxseSDOHAFH80
"""

from fastai.vision.all import *
import gradio as gr

learn = load_learner('export.pkl')
categories = ('alphonso', 'dasheri', 'kesar')

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))

image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label)
intf.launch(inline=False)

