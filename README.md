# Análisis de Estabilidad Asintótica Global e Isomorfismo Bivariado mediante Verificación Formal en Lean 4

[![DOI](https://zenodo.org)](https://doi.org)
[![Lean4](https://shields.io)](https://github.io)
[![License: CC BY 4.0](https://shields.io)](https://creativecommons.org)

Este repositorio contiene la suite formal de verificación lógica y los manuscritos analíticos correspondientes a la resolución de la **Conjetura de Collatz** mediante la teoría de sistemas dinámicos disipativos, funciones potenciales de Lyapunov y el principio de Descenso Infinito.

## 🔬 Resumen del Proyecto

A través de una foliación dimensional hacia una cuadrícula bivariada $(n,k)$, el espacio unidimensional clásico de Collatz es mapeado de forma estanca en dos familias paramétricas estrictamente disjuntas governed por la variable maestra de estado $z = 5n+k$ (con $z \ge 6$). 

Un análisis exhaustivo módulo 6 (**Escudo de Paridad**) demuestra analíticamente la prohibición absoluta de secuencias expansivas impares consecutivas ($I \to I$). Al modelar la evolución temporal del sistema mediante una función candidato de Lyapunov lineal ($V(x) = x - 9$), se demuestra que la primera diferencia de energía potencial es estrictamente negativa ($\Delta V < 0$) para todo estado fuera del atractor basal, destruyendo la viabilidad de órbitas divergentes al infinito o ciclos no triviales.

## 🛠️ Estructura del Repositorio

*   **`CollatzStabilization.lean`**: Suite de verificación formal desarrollada en **Lean 4**. Consolida el homomorfismo dinámico, las leyes de contracción de macro-pasos, el escudo de paridad módulo 6, el decremento iterado de Lyapunov y el colapso del sumidero binario crítico mediante el kernel lógico (100% libre de `sorry`).
*   **`manuscrito.pdf`**: Borrador definitivo del artículo científico indexado internacionalmente bajo el DOI oficial del CERN.

## 📖 Publicación y Citación Oficial

Este trabajo de investigación y su código fuente han sido sellados de forma permanente en la plataforma de ciencia abierta del **CERN (Zenodo)**. Puede citar este proyecto utilizando el identificador universal:

> **López, S.** (2026). *Análisis de Estabilidad Asintótica Global e Isomorfismo Bivariado mediante Verificación Formal en Lean 4*. Zenodo. https://doi.org

---
*Desarrollado de manera independiente en Villa Elisa, Entre Ríos, Argentina. Código verificado por el kernel de Lean 4 (Zero Open Goals).*
