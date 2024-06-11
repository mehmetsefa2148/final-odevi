import numpy as np
import pandas as pd

data_3 = pd.read_excel('soru3_data.xlsx')
image_3 = data_3.to_numpy()


def create_gaussian_kernel(size, sigma=1):
    kernel = np.zeros((size, size), dtype=np.float32)
    center = size // 2
    for i in range(size):
        for j in range(size):
            diff = np.sqrt((i - center) ** 2 + (j - center) ** 2)
            kernel[i, j] = np.exp(-(diff ** 2) / (2 * sigma ** 2))
    return kernel / np.sum(kernel)


def gaussian_blur(img, kernel_size=3, sigma=1):
    kernel = create_gaussian_kernel(kernel_size, sigma)
    img_height, img_width = img.shape
    pad_size = kernel_size // 2
    padded_img = np.pad(img, ((pad_size, pad_size), (pad_size, pad_size)), mode='constant', constant_values=0)

    blurred_img = np.zeros((img_height, img_width), dtype=np.float32)

    for i in range(img_height):
        for j in range(img_width):
            region = padded_img[i:i + kernel_size, j:j + kernel_size]
            blurred_img[i, j] = np.sum(region * kernel)

    return blurred_img.astype(np.uint8)


blurred_image = gaussian_blur(image_3)
print(pd.DataFrame(blurred_image))
