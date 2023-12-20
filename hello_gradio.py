import gradio as gr 

def greet(name):
    return "Hello "+ name+"! Welcome to gradio"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()