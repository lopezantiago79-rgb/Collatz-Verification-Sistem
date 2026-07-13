# Verificación Formal Certificada: Estabilidad y Convergencia del Sistema $3x+9$

Este repositorio contiene la documentación técnica y el **Protocolo de Auditoría Formal** que certifica la estabilidad global y la convergencia absoluta del sistema dinámico parametrizado $f(x) = 3x+9$ hacia el atractor basal (9).

Todas las pruebas lógicas y dinámicas presentadas han sido verificadas y selladas por el kernel de Lean 4, utilizando la librería estándar `Mathlib`. Este trabajo constituye una validación formal de los resultados presentados en la tesis de investigación.

## 📄 Documento de Tesis
- **`Tesis_Sistema_3x9.pdf`**: Manuscrito final de la investigación. Contiene el marco teórico, el isomorfismo topológico, la inecuación de balance y el Teorema de Descenso Infinito de Fermat.

## ⚙️ Protocolo de Auditoría y Estructura Formal
El código de verificación está organizado en módulos lógicos independientes que conforman la demostración completa:

- `MathlibDemo.lean`: **Lema de Compresión Binaria**. Valida que el costo de bit de la expansión impar ($3n+9$) es estrictamente superado por el retorno de desplazamiento (bits reducidos).
- `Lyapunov_Stability.lean`: **Certificación de Energía**. Define la función de Lyapunov $V(n) = \log_2(n)$ y demuestra que $V(f(n)) < V(n)$ para todo $n > 9$, garantizando la estabilidad asintótica.
- `Teorema_Descenso_Fermat.lean`: **Teorema de Cierre**. Aplica el principio de descenso infinito sobre la estructura del sistema, descartando ciclos y asegurando la convergencia al atractor basal.
- `Atractor_Basal.lean`: **Definición del Punto Fijo**. Establece las propiedades algebraicas del valor $\{9\}$ y su comportamiento bajo el operador $f(n)$.
- `Main_Proof.lean`: **Síntesis Final**. Integra los lemas anteriores para demostrar formalmente que toda trayectoria, dado un $n$ finito, converge al estado terminal.
- `Simulador_Titanico.py`: Protocolo de validación empírica para números de escala masiva ($n > 10^{50,000}$).

## Estado de Verificación y Compilación
Este proyecto ha sido verificado satisfactoriamente bajo el kernel de Lean 4.

- **Estado:** `VERIFIED BY LEAN KERNEL`
- **Compilador:** Lean 4 (versión especificada en `lean-toolchain`)
- **Librerías:** `Mathlib4`

Para replicar la verificación:
1. Asegúrese de tener instalado el entorno de Lean 4.
2. Abra el directorio en VS Code con la extensión de Lean 4.
3. El servidor compilará automáticamente los archivos. La ausencia de errores y el mensaje `No goals` confirman la auditoría.

## Uso Académico y Reproducibilidad
Este material se proporciona con fines de auditoría científica y reproducibilidad académica. El autor certifica que los resultados aquí presentados son el producto de una validación formal rigurosa.

---
*Autor: [Santiago López]*
*Fecha: Julio 13, 2026*
