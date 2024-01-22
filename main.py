import torch
from diffusers import AutoPipelineForText2Image
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'


pipeline = AutoPipelineForText2Image.from_pretrained(
	"runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16, variant="fp16").to("cuda")



image = pipeline(
	"stained glass of darth vader, backlight, centered composition, masterpiece, photorealistic, 8k").images[0]
#image
# image.save("yoda-pokemon.png")
# image
# image
image.show()
image = image.save("geeks.jpg")