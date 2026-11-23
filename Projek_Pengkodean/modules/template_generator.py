import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Katalog Header & Identitas Visual Provider
PROVIDER_CONFIGS = {
    # M-Banking
    "Bank BCA": {"header": "BCA - TRANSFER BERHASIL", "accent": "M-BCA"},
    "Bank Mandiri": {"header": "LIVIN MANDIRI - RESI TRANSFER", "accent": "MANDIRI"},
    "Bank BRI": {"header": "BRIMO - BUKTI TRANSAKSI", "accent": "BRI"},
    "Bank BNI": {"header": "BNI MOBILE BANKING - RESI", "accent": "BNI"},
    "SeaBank": {"header": "SEABANK - TRANSFER SUKSES", "accent": "SEABANK"},
    
    # E-Wallet
    "ShopeePay": {"header": "SHOPEEPAY - BUKTI PEMBAYARAN", "accent": "SHOPEE"},
    "GoPay": {"header": "GOPAY - TRANSAKSI SUKSES", "accent": "GOPAY"},
    "DANA": {"header": "DANA - BUKTI TRANSAKSI", "accent": "DANA"},
    "OVO": {"header": "OVO - STRUK PEMBAYARAN", "accent": "OVO"}
}

def generate_reference_template(nominal_str="Rp 1.500.000", provider_name="Bank BCA", width=320, height=100):
    """
    Menghasilkan Citra Acuan Resmi (x) secara dinamis di backend
    berdasarkan nominal dan provider (m-banking / e-wallet) yang dipilih.
    Output: Image PIL (Grayscale)
    """
    # 1. Ambil konfigurasi header provider (Default ke BCA jika tidak ada)
    config = PROVIDER_CONFIGS.get(provider_name, PROVIDER_CONFIGS["Bank BCA"])
    
    # 2. Buat kanvas putih murni (255)
    img = Image.new('L', (width, height), color=255)
    draw = ImageDraw.Draw(img)
    
    # 3. Muat Font (Fallback ke default jika arial.ttf tidak tersedia)
    try:
        font_header = ImageFont.truetype("arial.ttf", 14)
        font_nominal = ImageFont.truetype("arial.ttf", 22)
    except IOError:
        font_header = ImageFont.load_default()
        font_nominal = ImageFont.load_default()
        
    # 4. Cetak Header Provider (Piksel Hitam = 0)
    draw.text((15, 15), config["header"], fill=0, font=font_header)
    
    # 5. Cetak Nominal Resmi Transaksi
    draw.text((15, 48), nominal_str, fill=0, font=font_nominal)
    
    return img