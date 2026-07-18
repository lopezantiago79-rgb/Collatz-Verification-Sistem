# Collatz Conjecture: Global Asymptotic Stability & Formal Verification in Lean 4

[![Lean 4 Verified](https://shields.io)](https://github.io)
[![License: MIT](https://shields.io)](https://opensource.org)

## 🇪🇸 Descripción del Proyecto (Español)

Este repositorio contiene la formalización matemática y verificación computacional de un modelo de **Estabilidad Asintótica Global** aplicable a la dinámica de la Conjetura de Collatz. El desarrollo ha sido escrito enteramente en **Lean 4** y validado al 100% por su kernel lógico, quedando completamente libre de metas abiertas (`sorry`).

### Innovación Metodológica
A diferencia de las aproximaciones estadísticas tradicionales, este trabajo reduce la naturaleza no lineal del problema original mediante un enfoque trifásico:
1. **Reducción Dimensional Bivariada:** Foliación del espacio de enteros en una cuadrícula bidimensional $(n, k)$ unificada por la variable de estado maestra $z = 5n + k$, demostrando cobertura universal y exclusividad analítica (familias disjuntas).
2. **Escudo de Paridad (Módulo 6):** Prueba formal de que el operador impar mapea toda órbita expansiva hacia un múltiplo estricto de 6. Esto prohíbe algebraicamente las transiciones impares consecutivas ($I \to I$), transformando la dinámica en un flujo disipativo controlado.
3. **Estabilidad de Lyapunov & No-Periodicidad:** Introducción de una función de energía potencial lineal estricta ($V(x) = x - 9$). A través de un macro-paso contractivo, se demuestra que la variación de energía es estrictamente negativa ($\Delta V < 0$), lo que imposibilita de forma analítica tanto las órbitas infinitas como la existencia de ciclos cerrados no triviales (bucles fuera del atractor basal).

---

## 🇺🇸 Project Overview (English)

This repository contains the mathematical formalization and computational verification of a **Global Asymptotic Stability** model applied to the dynamics of the Collatz Conjecture. The entire framework has been developed in **Lean 4** and successfully validated by its logical kernel, remaining 100% free of open goals (`sorry`).

### Core Theoretical Contributions
Rather than relying on probabilistic or brute-force computational trends, this approach neutralizes the non-linear behavior of the traditional problem via a three-tiered structural strategy:
1. **Bivariate Dimensional Reduction:** Foliation of the natural number space into a 2D coordinate system $(n, k)$ collapsed into a unified master state variable $z = 5n + k$, proving total space coverage and algebraic mutual exclusivity.
2. **The Parity Shield (Modulo 6 Arithmetic):** Formal proof that the odd expansion operator maps trajectories directly into strict multiples of 6. This algebraically blocks consecutive odd-to-odd transitions ($I \to I$), forcing an immediate contractive cascade.
3. **Lyapunov Stability & Non-Periodicity:** Formulation of a strict linear Lyapunov energy candidate ($V(x) = x - 9$). Via a linearized contractive macro-step, the forward difference of energy is proven strictly negative ($\Delta V < 0$), which analytically rules out both divergent infinite orbits and non-trivial periodic loops.

---

## 🛠️ Estructura del Código / Code Architecture

El archivo fuente principal `CollatzStabilization.lean` incluye las siguientes estructuras formales:

* `def C`: La función clásica de Collatz sobre $\mathbb{N}$.
* `def desemboca (a b : ℕ)`: El operador infijo relacional personalizado (`~`) que rige la transitividad de las órbitas.
* `theorem exclusividad_familias`: Resolución exacta mediante la unión de conjuntos disjuntos.
* `theorem estabilidad_lyapunov`: Verificación de la derivada lineal definida negativa del potencial disipativo.
* `theorem imposibilidad_ciclos_no_triviales`: Demostración por reducción al absurdo de la inexistencia de bucles periódicos estables fuera del equilibrio.

---

## 🚀 Instalación y Verificación Local / Getting Started

Sigue estos pasos para clonar el repositorio y ejecutar el verificador de Lean 4 en tu entorno local:

### Requisitos Previos / Prerequisites
Asegúrate de tener instalado el gestor de herramientas de Lean (`elan`) y VS Code con la extensión oficial de **Lean 4**.

### Ejecución / Execution
1. Clona este repositorio en tu máquina:
   ```bash
   git clone https://github.com
   cd TU-REPOSITORIO
   ```
2. Descarga el caché de la biblioteca matemática oficial (`Mathlib`) requerida por las tácticas `omega` y `linarith`:
   ```bash
   lake exe cache get
   ```
3. Compila y verifica el proyecto:
   ```bash
   lake build
   ```
Si la compilación finaliza sin advertencias ni mensajes de error, el kernel de Lean habrá validado de manera exitosa la consistencia lógica de todo el andamiaje del sistema.

## 📄 Licencia / License
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

*Autor: [Santiago López]*
*Fecha: Julio 18, 2026*
