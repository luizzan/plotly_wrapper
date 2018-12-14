import requests
from PIL import Image
import numpy as np

def add_footer(self):

    try:
        if self.footer and self.kwargs.get('footer', True):
            main_img = Image.open(self.kwargs['filename'])
            footer_img = Image.open(requests.get(self.footer, stream=True).raw)

            footer_height = self.kwargs.get('footer_height', 40)
            footer_height = footer_height*self.kwargs.get('scale', 5)
            footer_img = footer_img.resize((main_img.size[0], footer_height))

            if self.footer_left:
                with Image.open(requests.get(self.footer_left, stream=True).raw) as left:
                    aspect_ratio = left.size[0]/left.size[1]
                    width = round(aspect_ratio*footer_height)
                    left = left.resize((width, footer_height), Image.ANTIALIAS)
                    footer_img.paste(left, (0,0))

            if self.footer_right:
                with Image.open(requests.get(self.footer_right, stream=True).raw) as right:
                    aspect_ratio = right.size[0]/right.size[1]
                    width = round(aspect_ratio*footer_height)
                    right = right.resize((width, footer_height), Image.ANTIALIAS)
                    pos = footer_img.size[0]-right.size[0]
                    footer_img.paste(right, (pos,0))

            imgs = np.vstack([main_img, footer_img])
            Image.fromarray(imgs).save(self.kwargs['filename'])

    except Exception as e:
        print(e)
        print('\n\nImage export error. Check footer images.')
