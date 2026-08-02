# Análisis de Estabilidad Asintótica Global e Isomorfismo Bivariado mediante Verificación Formal en Lean 4

[![DOI](https://zenodo.org)](https://doi.org)
[![Lean4](https://shields.io)](https://github.io)
[![License: Dual-Academic/Commercial](https://shields.io)](LICENSE)

Este repositorio contiene la suite formal de verificación lógica, los scripts complementarios y el marco de desarrollo tecnológico correspondientes a la resolución de la **Conjetura de Collatz** mediante la teoría de sistemas dinámicos disipativos, funciones de Lyapunov y el principio de Descenso Infinito.

## 🔬 Resumen del Proyecto

A través de una foliación dimensional hacia una cuadrícula bivariada $(n,k)$, el espacio unidimensional clásico de Collatz es mapeado de forma estanca en dos familias paramétricas estrictamente disjuntas governed por la variable maestra de estado $z = 5n+k$ (con $z \ge 6$). Un análisis exhaustivo módulo 6 (**Escudo de Paridad**) demuestra analíticamente la prohibición absoluta de secuencias expansivas impares consecutivas. Al modelar la evolución temporal mediante una función candidato de Lyapunov lineal ($V(x) = x - 9$), se demuestra que la primera diferencia de energía potencial es estrictamente negativa ($\Delta V < 0$) para todo estado fuera del atractor basal, destruyendo la viabilidad de órbitas divergentes al infinito o ciclos no triviales.

## 🔐 Protocolo Criptográfico PACF (Post-Quantum)

Este repositorio introduce el **Protocolo de Cifrado por Convolución de Flujo Disipativo (PACF)**, un criptosistema asimétrico post-cuántico inmune al algoritmo de Shor. 

*   **Clave Pública (Cifrado):** Operador de flujo disipativo clásico linealizado. El mensaje se inyecta como un estado inicial masivo $n_0$ y se drena a una tasa media de **~4.14 bits por macro-paso** hasta su absorción en el atractor basal. El criptograma final se compone de la traza secuencial binaria de paridades.
*   **Clave Privada (Descifrado):** Basada en el operador inverso biyectivo (`invFun`) verificado en Lean 4. Resuelve las coordenadas diofánticas inversas de la cuadrícula en tiempo lineal $\mathcal{O}(M)$, anulando la explosión combinatoria exponencial $\mathcal{O}(2^k)$ que frena a cualquier atacante externo.

## 🛠️ Estructura del Repositorio

*   **`CollatzStabilization.lean`**: Suite de verificación formal en **Lean 4**. Consolida el homomorfismo dinámico, el escudo de paridad, el decremento de Lyapunov y el colapso del sumidero binario (100% libre de `sorry`).
*   **`crypto_system.py`**: Algoritmo ejecutable de simulación del criptosistema PACF (Cifrado/Descifrado determinista de strings masivos).
*   **`benford_analysis.py`**: Script de auditoría estadística que certifica la convergencia exacta del flujo logarítmico hacia la Ley de Benford.
*   **`manuscrito.pdf`**: Borrador definitivo del artículo científico indexado internacionalmente.

## 📖 Publicación y Citación Oficial

Este trabajo de investigación y su código fuente han sido sellados de forma permanente en la plataforma de ciencia abierta del **CERN (Zenodo)**. Puede citar este proyecto utilizando el identificador universal:

> **López, S.** (2026). *Análisis de Estabilidad Asintótica Global e Isomorfismo Bivariado mediante Verificación Formal en Lean 4*. Zenodo. https://doi.org

## ⚖️ Términos de Licenciamiento
Este proyecto se distribuye bajo un esquema de **Licencia Dual**. El uso es completamente gratuito para fines académicos y de investigación científica abierta. Queda prohibida la explotación comercial, industrial o corporativa del protocolo PACF sin la adquisición previa de una licencia comercial paga emitida por el autor. Consulte el archivo `LICENSE` para más detalles.

---
*Desarrollado de manera independiente en Villa Elisa, Entre Ríos, Argentina. Código verificado por el kernel de Lean 4 (Zero Open Goals).*
