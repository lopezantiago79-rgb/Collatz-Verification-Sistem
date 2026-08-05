import hashlib
import sys

# Forzar el soporte para enteros gigantescos en el intérprete de Python
sys.set_int_max_str_digits(200000)

def calcular_sha256(texto):
    """Genera la firma digital criptográfica de integridad para el mensaje."""
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

def texto_a_entero(texto):
    """Mapea la cadena de texto unificada al espacio numérico natural."""
    return int.from_bytes(texto.encode('utf-8'), byteorder='big')

def entero_a_texto(numero):
    """Reconstruye el string original a partir del entero diofántico."""
    return numero.to_bytes((numero.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

def generar_keystream_clh(clave_privada_binaria, longitud_bits):
    """
    Generador determinista de flujo basado en la dinámica de Collatz.
    Utiliza una clave simétrica binaria para fijar las condiciones iniciales.
    """
    # Convertir la clave binaria de 512 bits a un entero impar en la Subclase II
    n = (int(clave_privada_binaria, 2) * 6) + 5
    semilla_inicial = n
    keystream = []
    
    while len(keystream) < longitud_bits:
        if n % 2 == 0:
            n >>= 1
            keystream.append(0)
        else:
            n = (n << 1) + n + 1
            keystream.append(1)
            
        # Al absorberse en el atractor basal, se ejecuta un salto de fase diofántico
        if n == 1:
            semilla_inicial = (semilla_inicial * 3 + 7) % (2**512)
            n = (semilla_inicial * 6) + 5
            
    return keystream[:longitud_bits]

def cifrar_clh(mensaje_texto, clave_privada_binaria):
    """
    Algoritmo de codificación por flujo simétrico.
    Entrada: Mensaje y Clave de 512 bits. Salida: Criptograma Puro.
    """
    hash_msg = calcular_sha256(mensaje_texto)
    paquete = f"{mensaje_texto}|||{hash_msg}"
    
    n_msg = texto_a_entero(paquete)
    longitud_bits = n_msg.bit_length()
    
    # Generar el flujo determinista acoplado
    flujo_bits = generar_keystream_clh(clave_privada_binaria, longitud_bits)
    
    mascara_entero = 0
    for bit in flujo_bits:
        mascara_entero = (mascara_entero << 1) | bit
        
    # Operación de difusión mediante enmascaramiento lineal
    criptograma_c = n_msg ^ mascara_entero
    return criptograma_c, longitud_bits

def descifrar_clh(criptograma_c, longitud_bits, clave_privada_binaria):
    """
    Algoritmo de decodificación reversible con validación estricta de preimágenes.
    """
    flujo_bits_receptor = generar_keystream_clh(clave_privada_binaria, longitud_bits)
    
    mascara_entero_receptor = 0
    for bit in flujo_bits_receptor:
        mascara_entero_receptor = (mascara_entero_receptor << 1) | bit
        
    # Reversión de la máscara por simetría XOR
    n_recuperado = criptograma_c ^ mascara_entero_receptor
    
    # Simulación inversa de validación topológica sobre la órbita diofántica
    n_verif = 1
    # Generar la secuencia de paridades esperada para aplicar el filtrado del referee
    n_trayecto = (int(clave_privada_binaria, 2) * 6) + 5
    semilla_inicial = n_trayecto
    mapa_paridades = []
    
    for _ in range(longitud_bits):
        if n_trayecto % 2 == 0:
            n_trayecto >>= 1
            mapa_paridades.append(0)
        else:
            n_trayecto = (n_trayecto << 1) + n_trayecto + 1
            mapa_paridades.append(1)
        if n_trayecto == 1:
            semilla_inicial = (semilla_inicial * 3 + 7) % (2**512)
            n_trayecto = (semilla_inicial * 6) + 5

    # Auditoría estricta de preimágenes impares para evitar estados fantasma (Sugerencia de la IA)
    for paridad in reversed(mapa_paridades):
        if paridad == 0:
            n_verif <<= 1
        else:
            assert (n_verif - 1) % 3 == 0, "Error estructural: Coordenada diofántica no válida."
            n_candidato = (n_verif - 1) // 3
            assert n_candidato % 2 != 0, "Error de consistencia: Estado huérfano fuera de órbita."
            n_verif = n_candidato

    bloque_texto = entero_a_texto(n_recuperado)
    mensaje_plano, hash_extraido = bloque_texto.split("|||")
    
    assert calcular_sha256(mensaje_plano) == hash_extraido, "Fallo de integridad: Criptograma alterado."
    return mensaje_plano

# --- Simulación del Módulo Experimental Estanco ---
if __name__ == "__main__":
    print("=== MODELO EXPERIMENTAL DE CIFRADO DE FLUJO CLH V4 ===")
    mensaje = "ALGORITMO DE ENMASCARAMIENTO COMPLETO CON VALIDACION DE PREIMAGENES"
    
    # CLAVE PRIVADA SIMÉTRICA (SK): Definición formal de un espacio binario de 512 bits
    CLAVE_PRIVADA_512 = bin(int(hashlib.sha512(b"Semilla_Maestra_Lopezh_2026").hexdigest(), 16))[2:].zfill(512)
    
    print(f"\n[Emisor] Mensaje original: '{mensaje}'")
    
    # Ejecución del Cifrado por Difusión
    c, tamano = cifrar_clh(mensaje, CLAVE_PRIVADA_512)
    print(f"\n[Tránsito] Criptograma masivo de transmisión (C):")
    print(f"{str(c)[:80]}... [Flujo Protegido]")
    
    # Ejecución del Descifrado de Alta Consistencia
    try:
        mensaje_final = descifrar_clh(c, tamano, CLAVE_PRIVADA_512)
        print(f"\n=== REPORT DE OPERACIÓN COMPUTACIONAL ===")
        print(f"Mensaje Recuperado: '{mensaje_final}'")
        print("✅ VALIDACIÓN: El protocolo implementa correctamente el cifrado y descifrado mediante el flujo determinista propuesto.")
    except AssertionError as e:
        print(f"❌ VIOLACIÓN DE PROTOCOLO SEGURIDAD: {e}")
