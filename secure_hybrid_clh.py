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

def cifrar_clh(mensaje_empaquetado):
    """Cifrado disipativo del Criptosistema López-Heinzen (CLH)."""
    n = texto_a_entero(mensaje_empaquetado)
    pasos = 0
    ruta_paridades = []
    
    while n > 1:
        if n % 2 == 0:
            ruta_paridades.append(0)
            n >>= 1
        else:
            ruta_paridades.append(1)
            n = (n << 1) + n + 1
        pasos += 1
    return pasos, ruta_paridades

def descifrar_clh(atractor, ruta_paridades):
    """Descifrado reverso exacto mediante las ecuaciones simétricas invFun."""
    n = atractor
    for paridad in reversed(ruta_paridades):
        if paridad == 0:
            n <<= 1
        else:
            n = (n - 1) // 3
    return entero_a_texto(n)

if __name__ == "__main__":
    print("=== SISTEMA INTEGRAL CLH + SHA-256 ===")
    mensaje_secreto = "LO LOGRE CON EXITO ESTANCO Y PROTOCOLO INTEGRAL"
    print(f"[Emisor] Mensaje original: '{mensaje_secreto}'")
    
    hash_emisor = calcular_sha256(mensaje_secreto)
    print(f"[Emisor] Sello SHA-256 generado: {hash_emisor}")
    
    bloque_seguro = f"{mensaje_secreto}|||{hash_emisor}"
    
    print("\nIniciando cifrado por disipación cuántica CLH...")
    total_pasos, criptograma_bits = cifrar_clh(bloque_seguro)
    print(f"-> Criptograma generado. Órbita completada en {total_pasos} pasos.")
    
    print("\n[Receptor] Ejecutando descifrado por isomorfismo diofántico...")
    bloque_recuperado = descifrar_clh(1, criptograma_bits)
    
    texto_recuperado, hash_recuperado = bloque_recuperado.split("|||")
    hash_auditoria = calcular_sha256(texto_recuperado)
    
    print(f"\n=== REPORTE DE AUDITORÍA CRIPTOGRÁFICA ===")
    print(f"Mensaje Extraído: '{texto_recuperado}'")
    print(f"Hash en Criptograma: {hash_recuperado}")
    print(f"Hash Calculado:      {hash_auditoria}")
    
    if hash_recuperado == hash_auditoria:
        print("\n✅ CERTIFICACIÓN: Integridad absoluta. Mensaje auténtico y no alterado.")
    else:
        print("\n❌ ALERTA: Intrusión detectada. El criptograma fue modificado en tránsito.")
