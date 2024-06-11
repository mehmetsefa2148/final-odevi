import pandas as pd
import numpy as np

data_1_2 = pd.read_excel('soru1_2_data.xlsx')
image = data_1_2.to_numpy()

def contrast_stretching(img, L=256):
    min_val = np.min(img)
    max_val = np.max(img)
    stretched_img = ((img - min_val) / (max_val - min_val)) * (L - 1)
    return stretched_img.astype(np.uint8)


stretched_image = contrast_stretching(image)
print(pd.DataFrame(stretched_image))
