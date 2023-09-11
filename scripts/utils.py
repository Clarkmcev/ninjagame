import os
import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    # black background will become transparent
    # img.set_colorkey(0,0)
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path):
        print(img_name)
        images.append(load_image(path + '/' + img_name))
    return images