from modules.models import ImageToImageResponse
from modules.utils import pil_to_bytes, cal_relative_scale, generate_name
from modules.models import OBJ, ENVConfig
from PIL import Image

import io
from pathlib import Path

def img2img(image, config:ENVConfig, style, save_input=True, **kwargs):
    image_data = image.file.read()
    image = Image.open(io.BytesIO(image_data))
    width, height = image.size
    name = generate_name()

    if save_input:
        filedir = config.input_dir / f"input_image_{style}"
        filedir.mkdir(parents=True, exist_ok=True)
        filename =   filedir / f"{name}.png"
        image.save(filename)

    scale_by = cal_relative_scale(width, height, 768, 768)
    width = int(width * scale_by)
    height = int(height * scale_by)
    image = image.resize((width, height))
    pipe = OBJ[style]["pipe"]
    generated_image = pipe(prompt=OBJ[style]["prompt"],
                    negative_prompt=OBJ[style]["negative_prompt"],
                    image=image,
                    num_inference_steps=OBJ[style]["steps"],
                    generator=OBJ[style]["generator"],
                    guidance_scale=OBJ[style]["cfg_scale"],
                    strength=OBJ[style]["denoising_strength"]).images[0]

    return ImageToImageResponse(images=pil_to_bytes(generated_image), parameters={'scale_by': scale_by})

def img2url(image, config:ENVConfig, style, save_input=True, **kwargs):
    image_data = image.file.read()
    image = Image.open(io.BytesIO(image_data))
    width, height = image.size
    name = generate_name()

    if save_input:
        filedir = config.input_dir / f"input_image_{style}"
        filedir.mkdir(parents=True, exist_ok=True)
        filename =   filedir / f"{name}.png"
        image.save(filename)

    scale_by = cal_relative_scale(width, height, 768, 768)
    width = int(width * scale_by)
    height = int(height * scale_by)
    image = image.resize((width, height))
    pipe = OBJ[style]["pipe"]
    generated_image = pipe(prompt=OBJ[style]["prompt"],
                    negative_prompt=OBJ[style]["negative_prompt"],
                    image=image,
                    num_inference_steps=OBJ[style]["steps"],
                    generator=OBJ[style]["generator"],
                    guidance_scale=OBJ[style]["cfg_scale"],
                    strength=OBJ[style]["denoising_strength"]).images[0]

    filename = f"output_image_{style}"
    output_path = config.output_dir / filename 
    output_path.mkdir(parents=True, exist_ok=True)
    filename =  f"{filename}/{name}.png"
    output_path = output_path / f"{name}.png"
    generated_image.save(output_path)

    return ImageToImageResponse(images=f"{config.domain_name}/{filename}", parameters={'scale_by': scale_by})