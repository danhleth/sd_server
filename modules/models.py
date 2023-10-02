from pydantic import BaseModel, Field
from typing import Any, Optional
from typing import Dict, List

from diffusers import StableDiffusionImg2ImgPipeline, EulerAncestralDiscreteScheduler
import torch
from pathlib import Path


class ImageToImageResponse(BaseModel):
    images: List[str]
    parameters: dict


class ENVConfig():
    def __init__(self):
        self.domain_name = 'image-service-storage.bsmart.city'
        self.output_dir = Path("./output")
        self.input_dir = Path("./input")

        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.input_dir.mkdir(parents=True, exist_ok=True)


# Load the Stable Diffusion pipeline
def init_stable_diffusion_anime():
    model_path = "/data/danh/sd_anime/stable-diffusion-webui/models/Stable-diffusion/aamAnyloraAnimeMixAnime_v1.safetensors"
    pipe = StableDiffusionImg2ImgPipeline.from_single_file(model_path, torch_dtype=torch.float16)
    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to("cuda")

    # Define the default parameters
    default_prompt = "modern anime, 2000s anime, anime style, best quality, masterpiece"
    default_negative_prompt = "(worst quality:1.5), (low quality:1.5), (normal quality:1.5), lowres, bad anatomy, vaginas in breasts, ((monochrome)), ((grayscale)), collapsed eyeshadow, multiple eyebrows, (cropped), oversaturated, sexy, errors, signature, watermark, jpeg artifacts, blurry, wrong gender, dented, missing limbs, extra limbs, deformed hand, long neck, username, artist name, conjoined fingers, deformed fingers, ugly eyes, imperfect eyes, skewed eyes, unnatural face, unnatural body, error, painting by a bad artist"
    default_steps = 40
    default_cfg_scale = 30
    default_denoising_strength = 0.6
    default_seed = 2412614579
    generator = torch.Generator(device="cuda").manual_seed(default_seed)
    return {"pipe": pipe,
            "prompt": default_prompt,
            "negative_prompt": default_negative_prompt,
            "steps": default_steps,
            "cfg_scale": default_cfg_scale,
            "denoising_strength": default_denoising_strength,
            "seed": default_seed,
            "generator": generator}


def init_stable_diffusion_disney():
    model_path = "/data/danh/sd_anime/stable-diffusion-webui/models/Stable-diffusion/disneyPixarCartoon_v10.safetensors"
    pipe = StableDiffusionImg2ImgPipeline.from_single_file(model_path, torch_dtype=torch.float16)
    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to("cuda")

    # Define the default parameters
    default_prompt = "modern anime, 2000s anime, anime style, best quality, masterpiece"
    default_negative_prompt = "(worst quality:1.5), (low quality:1.5), (normal quality:1.5), lowres, bad anatomy, vaginas in breasts, ((monochrome)), ((grayscale)), collapsed eyeshadow, multiple eyebrows, (cropped), oversaturated, sexy, errors, signature, watermark, jpeg artifacts, blurry, wrong gender, dented, missing limbs, extra limbs, deformed hand, long neck, username, artist name, conjoined fingers, deformed fingers, ugly eyes, imperfect eyes, skewed eyes, unnatural face, unnatural body, error, painting by a bad artist"
    default_steps = 40
    default_cfg_scale = 30
    default_denoising_strength = 0.6
    default_seed = 2412614579
    generator = torch.Generator(device="cuda").manual_seed(default_seed)
    return {"pipe": pipe,
            "prompt": default_prompt,
            "negative_prompt": default_negative_prompt,
            "steps": default_steps,
            "cfg_scale": default_cfg_scale,
            "denoising_strength": default_denoising_strength,
            "seed": default_seed,
            "generator": generator}


OBJ = {
    "sd_anime": init_stable_diffusion_anime(),
    "sd_disney": init_stable_diffusion_disney()
       }
