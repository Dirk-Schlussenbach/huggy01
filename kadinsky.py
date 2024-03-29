from diffusers import AutoPipelineForText2Image
import torch

pipeline = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16"
).to("cuda")
generator = torch.Generator("cuda").manual_seed(31)
image = pipeline("x-ray of an Astronaut on the  moon, cold color palette, muted colors, detailed, 8k", generator=generator).images[0]

image.show()
image = image.save("geeks.jpg")