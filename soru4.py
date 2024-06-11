import numpy as np

hist_data = {
    100: 12, 101: 18, 102: 32, 103: 48, 104: 52, 105: 65, 106: 55, 107: 42,
    108: 32, 109: 16, 110: 10, 140: 5, 141: 18, 142: 25, 143: 32, 144: 40,
    145: 65, 146: 43, 147: 32, 148: 20, 149: 10, 150: 4
}

intensities = np.array(list(hist_data.keys()))
pixel_counts = np.array(list(hist_data.values()))

def global_thresholding(hist, T0=100, threshold=1):
    T = T0
    while True:
        G1 = intensities[intensities > T]
        G2 = intensities[intensities <= T]
        if len(G1) == 0 or len(G2) == 0:
            break
        m1 = np.sum(G1 * pixel_counts[intensities > T]) / np.sum(pixel_counts[intensities > T])
        m2 = np.sum(G2 * pixel_counts[intensities <= T]) / np.sum(pixel_counts[intensities <= T])
        T1 = (m1 + m2) / 2
        if abs(T1 - T) < threshold:
            break
        T = T1
    return T

optimal_threshold = global_thresholding(hist_data)
print("Optimal Eşik Değeri:", optimal_threshold)
