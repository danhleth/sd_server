from fastapi import FastAPI, APIRouter, File, UploadFile, Query
from modules.models import ImageToImageResponse, ENVConfig
from modules.img2img import img2img, img2url

import os


class API:
    def __init__(self, app:FastAPI):
        self.router = APIRouter()
        self.config = ENVConfig()
        
        self.app = app
        self.add_api_route("/sdapi/style_anime/v1/img2img",self.style_anime_img2img, methods=["POST"], response_model=ImageToImageResponse)
        self.add_api_route("/sdapi/style_anime/v1/img2url",self.style_anime_img2url, methods=["POST"], response_model=ImageToImageResponse)
        # self.add_api_route("/sdapi/style_disney/v1/img2img",self.style_disney_img2img, methods=["POST"], response_model=ImageToImageResponse)
        # self.add_api_route("/sdapi/style_disney/v1/img2url",self.style_disney_img2url, methods=["POST"], response_model=ImageToImageResponse)

    def style_anime_img2img(self, image:UploadFile=File(...)):
        return img2img(image, style="sd_anime", config=self.config) 

    def style_anime_img2url(self, image:UploadFile=File(...)):
        return img2url(image, style="sd_anime", config=self.config)

    # def style_disney_img2img(self, image:UploadFile=File(...)):
    #     return img2img(image, style="sd_disney", config=self.config) 

    # def style_disney_img2url(self, image:UploadFile=File(...)):
    #     return img2url(image, style="sd_disney", config=self.config)

    def add_api_route(self, path:str, endpoint, **kwargs):
        self.app.add_api_route(path, endpoint, **kwargs)