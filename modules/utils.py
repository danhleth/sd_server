import io
import time
import random
import base64

def generate_name():
    name = 'GENimg2img_'
    for i in range(random.randint(5, 10)):
        name += random.choice('QAZXfrSWEDCVFRTqazxswgbnhyujmkiolpGBNHYUJedcvtMKIOLP')
        
    # Append current timestamp (in seconds) to the name
    timestamp = int(time.time())
    name += f'_{timestamp}'   

    return name


def cal_relative_scale(width, height, max_width, max_height):
    if width > max_width or height > max_height:
        scale = max_width / width
        if height * scale > max_height:
            scale = max_height / height
        return scale
    else:
        return 1


def pil_to_bytes(image):
    im_file = io.BytesIO()
    image.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
    im_b64 = base64.b64encode(im_bytes)
    return im_b64