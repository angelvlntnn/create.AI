# Menggunakan Hugging FaceHub
import os
from langchain_community.llms import HuggingFaceEndpoint
import gradio as gr

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")

def chatbot(prompt):
    return llm.invoke(prompt).content
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)