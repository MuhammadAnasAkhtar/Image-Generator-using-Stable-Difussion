import gradio as gr
import torch
from diffusers import DiffusionPipeline


# Define the image generation function
def image_generation(prompt):
    # Check if GPU is available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Load the Stable Diffusion 2.1 pipeline (as you're using DiffusionPipeline now)
    pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1",
                                                 torch_dtype=torch.float16 if device == "cuda" else torch.float32,
                                                 text_encoder_3=None,
                                                 tokenizer_3=None)

    # Generate an image based on the prompt
    image = pipeline(
        prompt=prompt,
        negative_prompt="blurred, ugly, watermark, low resolution, blurry",
        num_inference_steps=40,
        height=1024,
        width=1024,
        guidance_scale=9.0
    ).images[0]
    
    return image

# Define the Gradio interface
interface = gr.Interface(
    fn=image_generation,
    inputs=gr.Textbox(lines=2, placeholder="Enter your Prompt..."),
    outputs=gr.Image(type="pil"),
    title="Image Creation using Stable Diffusion 3 Model",
    description="This application generates awesome images using the Stable Diffusion 3 model."
)

# Launch the Gradio app
interface.launch()
