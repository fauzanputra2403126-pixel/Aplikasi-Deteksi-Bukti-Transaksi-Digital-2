import numpy as np

def compute_forensic_hamming(vector_x, vector_y):
    """
    Menghitung XOR, Hamming Weight, Hamming Distance, 
    dan menetapkan vonis keaslian dokumen.
    """
    n = len(vector_x)
    if len(vector_y) != n:
        raise ValueError("Dimensi vektor biner acuan dan uji harus persis sama!")
    
    # 1. Operasi XOR Bit-wise (e = x XOR y)
    error_vector = np.bitwise_xor(vector_x, vector_y)
    
    # 2. Perhitungan Hamming Weight & Hamming Distance
    hamming_weight = int(np.sum(error_vector))
    hamming_distance = int(np.count_nonzero(vector_x != vector_y))
    
    # 3. Verifikasi Teorema Matematika: d(x, y) == wt(e)
    is_verified = (hamming_distance == hamming_weight)
    
    # 4. Rasio Perubahan Bit (%)
    bit_change_ratio = (hamming_distance / n) * 100
    
    # 5. Vonis Keputusan Tunggal
    if hamming_distance == 0:
        verdict = "VALID_ASLI"
        title_output = "🟢 BUKTI TRANSAKSI INI ASLI"
        description = "Integritas berkas utuh 100%. Tidak terdeteksi pembalikan bit biner (bit flipping)."
    else:
        verdict = "MANIPULASI_PALSU"
        title_output = "🔴 BUKTI TRANSAKSI INI PALSU"
        description = f"Terdeteksi manipulasi piksel biner pada {hamming_distance:,} posisi bit. Bukti transaksi tidak sah!"
        
    return {
        'total_bits': n,
        'hamming_distance': hamming_distance,
        'hamming_weight': hamming_weight,
        'is_verified': is_verified,
        'bit_change_ratio': bit_change_ratio,
        'verdict': verdict,
        'title_output': title_output,
        'description': description,
        'error_vector': error_vector
    }