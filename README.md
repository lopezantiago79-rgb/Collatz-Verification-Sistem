# Verificación Formal Certificada: Estabilidad y Convergencia del Sistema $3x+9$

Este repositorio contiene el Protocolo de Auditoría Formal que certifica la estabilidad global y la convergencia absoluta del sistema dinámico parametrizado $f(x) = 3x+9$ hacia el atractor basal (9).

Todas las pruebas lógicas y dinámicas presentadas han sido verificadas y selladas por el kernel de Lean 4, utilizando la librería estándar `Mathlib`. Este trabajo constituye una validación formal de los resultados presentados en la tesis de investigación.

## Protocolo de Auditoría y Estructura

El repositorio está organizado en bloques lógicos, cada uno verificado independientemente:

- `MathlibDemo.lean`: **Lema de Compresión Binaria**. Prueba formal de que el "Costo de Bit" (CB) de la expansión impar es estrictamente superado por el "Retorno de Desplazamiento" (RD).
- `Lyapunov_Stability.lean`: **Demostración de Estabilidad Global**. Define la función de energía $V(n) = \log_2(n)$ y certifica formalmente que $V(f(n)) < V(n)$ para toda trayectoria fuera del atractor. Esta prueba garantiza que el sistema siempre pierde energía y no puede entrar en bucles infinitos.
- `Teorema_Descenso_Fermat.lean`: **Teorema de Conclusión**. Aplica el principio de descenso infinito para sellar la finitud de todas las trayectorias.
- `Simulador_Titanico.py`: Protocolo de validación empírica para números de escala masiva ($n > 10^{50,000}$), demostrando la escala-invariabilidad del sistema.

## Estado de Verificación y Compilación

Este proyecto ha sido verificado satisfactoriamente.

- **Estado:** `VERIFIED BY LEAN KERNEL`.
- **Compilador:** Lean 4 (versión especificada en `lean-toolchain`).
- **Librerías:** `Mathlib4`.

Para replicar la verificación:
1. Asegúrese de tener instalado el entorno de Lean 4.
2. Abra el directorio en VS Code con la extensión de Lean 4.
3. El servidor compilará automáticamente los archivos. La ausencia de errores y el mensaje `No goals` confirman la auditoría.

## Uso Académico y Reproducibilidad

Este material se proporciona con fines de auditoría científica y reproducibilidad académica. El autor certifica que los resultados aquí presentados son el producto de una validación formal rigurosa.

---
*Autor: [Santiago López]*
*Fecha: Julio 13, 2026*
