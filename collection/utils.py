"""
Utils
"""
import math
import os
import requests

from PIL import Image


def files_count(dir_path: str) -> int:
    """
    This function counts files in a given directory
    """
    return len(os.listdir(dir_path))


def delete_last_element(url_list: list, num=1) -> list:
    """
    Remove the last element in the array
    """
    return url_list[:-num]


def get_name_from_url(url):
    """
    Getting name from url
    """
    return url.split('/')[-1]


def convert_size(size_bytes: int) -> str:
    """
    Convert bytes to KB, MB ...
    """
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


def get_file_size(file_path: str) -> str:
    """
    Return file size
    """
    return convert_size(os.stat(file_path).st_size)


def get_img_name_size(img_path: str) -> tuple:
    """
    Return img name, img size
    """
    img_name = get_name_from_url(img_path)
    img_size = get_file_size(img_path)
    return img_name, img_size


def get_filenames(dir_name: str) -> list:
    """
    Get all filenames in a given directory
    """
    filenames = []
    for root, dirs, files in os.walk(dir_name):
        for filename in files:
            filenames.append(filename)
    return filenames


def download_img(url: str, img_path: str) -> bool:
    """
    Download image by url
    """
    response = requests.get(url, stream=True)
    if response.ok:
        img = Image.open(response.raw)
        img.save(img_path)
        del response
        return True

    print('it is impossible to load a file with such url')
    return False


def download_imgs(url_list: list, imgs_path: str) -> list:
    """
    Download multiple images from different urls
    """
    downloaded_imgs = []
    for url in url_list:
        i = files_count(imgs_path)
        img_path = f'{imgs_path}{i}.jpg'
        if download_img(url, img_path):
            downloaded_imgs.append(img_path)
    return downloaded_imgs
