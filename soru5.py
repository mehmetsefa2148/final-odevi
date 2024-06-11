import numpy as np

hist_data = {
    100: 12, 101: 18, 102: 32, 103: 48, 104: 52, 105: 65, 106: 55, 107: 42,
    108: 32, 109: 16, 110: 10, 140: 5, 141: 18, 142: 25, 143: 32, 144: 40,
    145: 65, 146: 43, 147: 32, 148: 20, 149: 10, 150: 4
}

def otsu_thresholding(hist):
    total = sum(hist.values())
    sumB, wB, maximum, level = 0, 0, 0, 0
    sum1 = sum([i * hist[i] for i in hist])

    for i in range(256):
        if i not in hist:
            continue
        wB += hist[i]
        if wB == 0:
            continue
        wF = total - wB
        if wF == 0:
            break
        sumB += i * hist[i]
        mB = sumB / wB
        mF = (sum1 - sumB) / wF
        between = wB * wF * ((mB - mF) ** 2)
        if between >= maximum:
            level = i
            maximum = between

    return level


otsu_threshold = otsu_thresholding(hist_data)
print("Otsu Eşik Değeri:", otsu_threshold)
