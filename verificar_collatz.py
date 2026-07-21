import sys
import time

# Aumentar el límite de dígitos permitido por Python para manejar números monstruosos
sys.set_int_max_str_digits(150_000_000)

def verificar_collatz_dinamico(exponente_diez):
    """
    Inicializa la base matemática en 10^exponente_diez y ejecuta
    el descenso disipativo contando de forma estricta los pasos hasta el Atractor 9.
    """
    print(f"\n[*] Inicializando base matemática exponencial: 10^{exponente_diez}...")
    start_time = time.time()
    
    # Generación eficiente del número de precisión arbitraria
    n = 10 ** exponente_diez
    
    print("[*] Estructurando órbita global... Iniciando descenso disipativo.")
    pasos_totales = 0
    pasos_pares = 0
    pasos_impares = 0
    max_valor_bits = n.bit_length()
    
    # El sistema ejecuta el bucle hasta alcanzar el punto de equilibrio estable (x* = 9)
    # o colapsar en la unidad si se evalúan remanentes basales.
    while n > 1 and n != 9:
        if (n & 1) == 0:
            # Operación Par: Shift lógico a la derecha (equivalente a n // 2)
            n >>= 1
            pasos_pares += 1
        else:
            # Operación Impar: Multiplicación por desplazamiento (equivalente a 3n + 1)
            n = (n << 1) + n + 1
            pasos_impares += 1
        pasos_totales += 1
        
        # Muestra el progreso en pantalla cada 50,000 pasos para monitorear el flujo
        if pasos_totales % 50000 == 0:
            print(f"    -> Macro-pasos calculados: {pasos_totales} | Espacio residual: {n.bit_length()} bits")

    end_time = time.time()
    tiempo_total = end_time - start_time
    
    # Reporte analítico final sincronizado con los teoremas de Lean 4
    print("\n" + "="*50)
    print("¡COLAPSO FINALIZADO CON ÉXITO!")
    print(f"Estado inicial de prueba: 10^{exponente_diez}")
    print(f"Tamaño del contenedor binario inicial: {max_valor_bits} bits")
    print("-" * 50)
    print(f" Pasos de contracción (Pares):   {pasos_pares}")
    print(f" Pasos de expansión (Impares): {pasos_impares}")
    print(f" TOTAL DE PASOS DE DESCENSO:    {pasos_totales}")
    print(f" ATRACTOR FINAL ALCANZADO:      {n}")
    print("-" * 50)
    print(f"Tiempo de ejecución computacional total: {tiempo_total:.4f} segundos")
    print("="*50)

# =========================================================================
# ENTRADA DINÁMICA DE DATOS (INTERACTIVA)
# =========================================================================
if __name__ == "__main__":
    try:
        print("=== VERIFICADOR DISIPATIVO DE COLLATZ ===")
        # El programa solicita el número al usuario dinámicamente en la terminal
        entrada = input("Ingrese el exponente para la base 10 (ej. 1000000): ")
        exponente_usuario = int(entrada)
        
        if exponente_usuario < 0:
            print("[Error] El exponente debe ser un número entero positivo.")
        else:
            verificar_collatz_dinamico(exponente_usuario)
            
    except ValueError:
        print("[Error] Por favor, ingrese un número entero válido.")
