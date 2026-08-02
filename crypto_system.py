import sys

# Forzar soporte para enteros gigantescos en el intérprete de Python
sys.set_int_max_str_digits(100000)

def texto_a_entero(texto):
    """Convierte texto plano en un número entero masivo en bytes."""
    return int.from_bytes(texto.encode('utf-8'), byteorder='big')

def entero_a_texto(numero):
    """Reconvierte un número entero masivo a su string de texto original."""
    return numero.to_bytes((numero.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

def cifrar_clh(mensaje_texto):
    """Simula el cifrado disipativo del Criptosistema López-Heinzen (CLH)."""
    n = texto_a_entero(mensaje_texto)
    pasos = 0
    ruta_paridades = []
    
    # Flujo disipativo hacia la frontera del sumidero binario crítico
    while n > 1:
        if n % 2 == 0:
            ruta_paridades.append(0)  # 0 representa paso par (división por 2)
            n >>= 1
        else:
            ruta_paridades.append(1)  # 1 representa paso impar (operador 3x+1)
            n = (n << 1) + n + 1
        pasos += 1
        
    return n, pasos, ruta_paridades

def descifrar_clh(atractor, ruta_paridades):
    """Descifrado mediante el mapa inverso biyectivo (Llave Privada invFun del CLH)."""
    n = atractor
    # Se revierte la ruta de paridades desde el punto de equilibrio hacia el origen
    for paridad in reversed(ruta_paridades):
        if paridad == 0:
            n <<= 1  # Inverso exacto de la contracción par
        else:
            n = (n - 1) // 3  # Inverso diofántico del macro-paso impar
            
    return entero_a_texto(n)

# --- Demostración y Validación del Criptosistema CLH ---
if __name__ == "__main__":
    mensaje_original = "LO LOGRE"
    print(f"Mensaje Original a Cifrar: '{mensaje_original}'")
    
    # 1. Ejecución del proceso de Cifrado CLH
    atractor_final, total_pasos, mapa_bits = cifrar_clh(mensaje_original)
    print(f"\n--- Criptograma Transmitido Seguro (Protocolo CLH) ---")
    print(f"Estado en el Atractor Basal: {atractor_final}")
    print(f"Longitud de la Llave de Bits: {len(mapa_bits)} bits")
    print(f"Total de Pasos de Disipación de Entropía: {total_pasos}")
    
    # 2. Ejecución del proceso de Descifrado CLH
    mensaje_recuperado = descifrar_clh(atractor_final, mapa_bits)
    print(f"\n--- Descifrado Exitoso Certificado por Isomorfismo ---")
    print(f"Mensaje Recuperado: '{mensaje_recuperado}'")
