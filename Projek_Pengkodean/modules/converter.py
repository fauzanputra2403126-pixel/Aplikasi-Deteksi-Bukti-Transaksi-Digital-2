import numpy as np
from PIL import Image

def extract_roi_and_binarize(uploaded_image, target_size=(320, 100), threshold=128):
    """
    Standardisasi ukuran ROI gambar uji (y), binarisasi (0 & 1),
    dan ekstraksi menjadi Vektor Biner 1-Dimensi.
    """
    # 1. Buka gambar uji dan konversi ke Grayscale
    img = Image.open(uploaded_image).convert('L')
    
    # 2. Resize ke dimensi ROI standar (320x100 px)
    img_roi = img.resize(target_size, Image.Resampling.LANCZOS)
    
    # 3. Thresholding Biner: Intensitas < 128 diubah jadi bit 1 (teks), sisanya 0 (latar)
    img_np = np.array(img_roi)
    binary_matrix = np.where(img_np < threshold, 1, 0).astype(np.uint8)
    
    # 4. Flatten matriks 2D menjadi Vektor Biner 1D
    binary_vector = binary_matrix.flatten()
    
    return img_roi, binary_vector

def convert_template_to_vector(template_pil_image, threshold=128):
    """
    Mengonversi PIL Image Acuan Backend (x) menjadi Vektor Biner 1D.
    """
    img_np = np.array(template_pil_image)
    binary_matrix = np.where(img_np < threshold, 1, 0).astype(np.uint8)
    return binary_matrix.flatten()