import numpy as np
import gradio as gr 

def sepia(image):
    sepia_filter = np.array([[0.393, 0.769, 0.189],[0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])

    sepia_image =image.dot(sepia_filter.T)
    sepia_image /= sepia_image.max()
    return sepia_image


demo = gr.Interface(fn=sepia, inputs=gr.Image(), outputs="image")

demo.launch()
