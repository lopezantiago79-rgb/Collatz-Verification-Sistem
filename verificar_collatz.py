import sys
import time

# Aumentar el límite de dígitos permitido por Python para manejar números monstruosos
sys.set_int_max_str_digits(150_000_000)

def verificar_collatz_optimizado(exponente_diez):
    """
    Inicializa el número inicial como 10^exponente_diez y ejecuta
    la secuencia de Collatz optimizada mediante operaciones de bits.
    """
    print(f"[*] Inicializando el número base: 10^{exponente_diez}...")
    start_time = time.time()
    
    # Generar el número inmenso de forma eficiente
    n = 10 ** exponente_diez
    
    print("[*] Estructurando órbita... Iniciando descenso disipativo.")
    pasos = 0
    max_valor_bits = n.bit_length()
    
    while n > 1:
        if (n & 1) == 0:
            # Operación Par: Shift a la derecha (equivalente a n // 2)
            n >>= 1
        else:
            # Operación Impar: (n * 2) + n + 1 (equivalente a 3n + 1)
            n = (n << 1) + n + 1
        pasos += 1
        
        # Muestra un reporte cada 50,000 pasos para monitorear el desplome binario
        if pasos % 50000 == 0:
            print(f"    -> Pasos ejecutados: {pasos} | Tamaño actual del contenedor: {n.bit_length()} bits")

    end_time = time.time()
    tiempo_total = end_time - start_time
    
    print("\n" + "="*50)
    print("¡VERIFICACIÓN EXITOSA COMPLETA!")
    print(f"Estado inicial: 10^{exponente_diez}")
    print(f"Tamaño inicial del contenedor: {max_valor_bits} bits")
    print(f"Total de pasos hasta el atractor basal: {pasos}")
    print(f"Tiempo de cómputo total: {tiempo_total:.4f} segundos")
    print("="*50)

# =========================================================================
# EJECUCIÓN DEL SCRIPT
# =========================================================================
if __name__ == "__main__":
    # Ajusta este valor para tus pruebas en computadoras potentes.
    # NOTA: 100,000,000 requerirá varias gigabytes de memoria RAM y tiempo de CPU.
    # Se recomienda empezar probando con 1_000_000 o 10_000_000 para verificar estabilidad local.
    EXPONENTE = 100_000_000 
    
    verificar_collatz_optimizado(EXPONENTE)
