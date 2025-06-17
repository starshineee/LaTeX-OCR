import gradio as gr
from pix2tex.cli import LatexOCR
from PIL import Image


custom_css = """
footer {
    display: none !important;
}
"""


model = LatexOCR()



def to_tex(image):
    img=Image.fromarray(image, mode='RGB')
    return model(img)

with gr.Blocks(css=custom_css) as interface:
    # 标题
    gr.Markdown("## Image to Latex")
    
    # 垂直排列的组件
    with gr.Column():
        input_component = gr.Image(label="Input Image",placeholder="Drag image or click to upload")
        output_component = gr.Textbox(label="Generated Latex Code")
    
    # 添加按钮触发处理
    btn = gr.Button("Convert")
    btn.click(fn=to_tex, inputs=input_component, outputs=output_component)
interface.launch(share=True)