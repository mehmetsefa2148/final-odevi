import numpy as np
import pandas as pd

data_1_2 = pd.read_excel('soru1_2_data.xlsx')
image = data_1_2.to_numpy()


def histogram_equalization(img):
    flat = img.flatten()

    hist, bins = np.histogram(flat, bins=256, range=[0, 256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * (255 / cdf[-1])
    equalized_img = np.interp(flat, bins[:-1], cdf_normalized)
    equalized_img = equalized_img.reshape(img.shape)

    return equalized_img.astype(np.uint8)


equalized_image = histogram_equalization(image)

print(pd.DataFrame(equalized_image))
