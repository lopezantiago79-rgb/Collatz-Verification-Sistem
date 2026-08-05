# Análisis de Estabilidad Asintótica Global e Isomorfismo Bivariado mediante Verificación Formal en Lean 4

[![DOI](https://zenodo.org)](https://doi.org)
[![Lean4](https://shields.io)](https://github.io)
[![License: Dual-Academic/Commercial](https://shields.io)](LICENSE)

Este repositorio contiene la suite formal de verificación lógica, los scripts analíticos complementarios y los modelos computacionales correspondientes a la investigación sobre la estructura algebraica y la estabilidad asintótica de las trayectorias de Collatz mediante sistemas dinámicos discretos disipativos.

## 🔬 Resumen de la Investigación

A través de una foliación dimensional hacia una cuadrícula bivariada $(n,k)$, la dinámica unidimensional clásica es mapeada en familias paramétricas disjuntas gobernadas por la variable maestra de estado $z = 5n+k$ (con $z \ge 6$). El proyecto desarrolla un análisis basado en el **Escudo de Paridad** para evaluar la exclusión analítica de secuencias expansivas impares consecutivas. Al modelar la evolución temporal mediante una función candidato de Lyapunov lineal ($V(x) = x - 9$), se busca fundamentar el colapso monótono de las órbitas hacia el atractor basal mediante el principio de Descenso Infinito.

## ⚙️ Prototipos de Investigación en Codificación Reversible (CLH)

El repositorio incluye una suite de herramientas en Python orientada a la experimentación empírica y al análisis de flujos reversibles asimétricos derivados de la dinámica bivariada del sistema:

1. **Esquema de Codificación Asimétrica Reversible (CLH):** Prototipo que modela la inyección y extracción determinista de cadenas de texto masivas convirtiéndolas en estados energéticos iniciales $n_0$. La trayectoria de paridades binarias actúa como un mapa topológico unívoco que permite al receptor legítimo revertir el flujo en tiempo lineal $\mathcal{O}(L)$ mediante las identidades `invFun` verificado sin objetivos abiertos en Lean 4.
2. **Protocolo Híbrido Autenticado (CLH-AEAD):** Extensión algorítmica experimental que encapsula un mecanismo de verificación de integridad mediante **SHA-256** dentro del bloque estructurado antes de la convolución de flujo, orientado al estudio de la detección de alteraciones en tránsito.
3. **Módulo Experimental de Cifrado de Flujo (Stream Cipher V4):** Prototipo de investigación que emplea un generador determinista de flujo inspirado en la dinámica de Collatz y una semilla estructurada de 512 bits para estudiar mecanismos de difusión y codificación reversible. Las propiedades criptográficas del generador constituyen un objeto de investigación en curso.

## 📊 Estado del Proyecto (Project Status)

*   **Formal Verification (Lean 4):** Completado (`zero open goals`, 100% libre de `sorry`).
*   **Python Prototypes:** Experimental.
*   **Cryptographic Evaluation:** En curso (*Ongoing*).

## 💻 Requisitos de Ejecución (Requirements)

*   **Lean** v4.x (incluyendo Mathlib)
*   **Python** v3.12+ (sin dependencias externas de librerías)

### Instrucciones de Despliegue Rápido
```bash
# Clonar el repositorio
git clone https://github.com

# Compilar la suite formal en Lean 4
lake build

# Ejecutar el prototipo de flujo criptográfico v4
python secure_stream_clh.py
```

## 🛠️ Estructura del Repositorio

* **`CollatzStabilization.lean`**: Código fuente formal en **Lean 4**. Consolida el homomorfismo dinámico, el escudo de paridad, el decremento de Lyapunov y el colapso del sumidero binario.
* **`secure_stream_clh.py`**: Algoritmo del cifrador de flujo dinámico con semilla simétrica estructurada de 512 bits (V4).
* **`secure_hybrid_clh.py`**: Prototipo funcional del esquema de codificación e integridad unificada (CLH + SHA-256).
* **`crypto_system.py`**: Script base de simulación para la traza elemental del mensaje maestro "LO LOGRE".
* **`benford_analysis.py`**: Script de auditoría estadística que mide la convergencia del flujo logarítmico hacia la Ley de Benford.
* **`Análisis de Estabilidad Asintótica Global e isomorfismo Bivariado mediante Verificación Formal en Lean 4.pdf`**: Borrador definitivo del artículo científico indexado con sus correspondientes apéndices matemáticos.

## 📖 Publicación y Citación Oficial (BibTeX)

Este trabajo de investigación independiente ha sido sellado y resguardado de forma permanente en el archivo de ciencia abierta del **CERN (Zenodo)**. Si desea citar este proyecto en trabajos académicos, utilice el siguiente formato:

```bibtex
@misc{lopezheinzen2026collatz,
  author       = {L{\'o}pez Heinzen, Santiago},
  title        = {An{\'a}lisis de Estabilidad Asint{\'o}tica Global e isomorfismo Bivariado mediante Verifikasi{\'o}n Formal en Lean 4},
  month        = aug,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21707849},
  url          = {https://doi.org}
}
```

## ⚖️ Términos de Licenciamiento
Este proyecto se distribuye bajo un esquema de **Licencia Dual**. El uso es libre y gratuito para fines académicos, educativos y de investigación científica abierta. Queda estrictamente prohibida la explotación comercial, industrial o corporativa del esquema CLH o sus derivados de software sin la autorización expresa y la adquisición de una licencia comercial paga emitida por el autor. Consulte el archivo `LICENSE` para más detalles.

---
*Desarrollado de manera independiente por el Prof. Santiago López Heinzen en Villa Elisa, Entre Ríos, Argentina. Código verificado por el kernel lógico de Lean 4.*
