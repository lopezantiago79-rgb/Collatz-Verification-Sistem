# Collatz Verification System

## Análisis de Estabilidad Asintótica Global e Isomorfismo Bivariado mediante Verificación Formal en Lean 4

Repositorio asociado al manuscrito de investigación sobre la dinámica de Collatz mediante una representación estructural bivariada, una variable de estado maestra y formalización matemática en Lean 4.

---

## Descripción

Este proyecto propone una representación alternativa de la dinámica clásica de Collatz mediante una **foliación del espacio de rutas** hacia un sistema bivariado de índices \((n,k)\).

La construcción introduce una variable de estado maestra \(z = 5n+k\), con el objetivo de reducir la descripción dimensional de las trayectorias a una única variable estructural.

El manuscrito desarrolla una clasificación de las rutas mediante dos familias paramétricas —Par e Impar— y establece un **Teorema de Cobertura del Espacio de Índices**, según el cual cada índice pertenece a una de las familias de manera exclusiva.

La investigación continúa con el análisis de subclases modulares, funciones de estabilidad y una función de tipo Lyapunov destinada a describir la disipación del sistema hacia el sumidero basal.

---

## Objetivo

El objetivo central del proyecto es estudiar la dinámica global del operador de Collatz mediante una transformación estructural que permita:

* Representar las rutas mediante una parametrización bivariada;
* Introducir la variable de estado maestra (\(z\));
* Demostrar la cobertura y exclusividad del espacio de índices;
* Establecer la correspondencia entre el espacio parametrizado y el sistema clásico;
* Analizar la dinámica mediante estructuras modulares;
* Estudiar la estabilidad asintótica mediante una función de Lyapunov;
* Formalizar los resultados principales mediante Lean 4.

El manuscrito plantea explícitamente que la transformación propuesta permite transferir los resultados de estabilidad del sistema parametrizado al sistema dinámico clásico mediante una biyección e isomorfismo estructural.

---

## Estructura matemática

### 1. Sistema dinámico de Collatz
Se considera el operador clásico de Collatz sobre los enteros positivos, separando las ramas correspondientes a los estados pares e impares. El análisis se centra en la estructura global de las rutas y en las relaciones entre diferentes trayectorias.

### 2. Foliación bivariada
Las rutas se organizan mediante un espacio de índices bivariado \((n,k)\). Las familias de índices presentan progresiones aritméticas con diferencia constante y permiten introducir la variable maestra \(z=5n+k\). El manuscrito utiliza esta reducción para representar la estructura de las rutas mediante una sola variable de estado.

### 3. Teorema de Cobertura del Espacio de Índices
El **Teorema 4.1 (Cobertura del Espacio)** establece la partición del espacio de índices en las familias Par e Impar. La demostración se estructura en dos partes:
1. **Existencia:** todo índice del dominio queda representado por alguna de las familias.
2. **Exclusividad:** las dos familias son disjuntas.

Como consecuencia, el sistema parametrizado posee una estructura de transición unívoca.

### 4. Subclases modulares
A partir de la parametrización global, el manuscrito estudia la estructura modular de las trayectorias, incluyendo las subclases asociadas con las congruencias relevantes del sistema. Estas subclases permiten analizar de forma separada los comportamientos expansivos y contractivos.

### 5. Estabilidad y función de Lyapunov
La dinámica parametrizada se estudia mediante una función de energía o potencial de tipo Lyapunov. La finalidad es caracterizar el descenso del sistema hacia el atractor basal y excluir, dentro del modelo desarrollado, trayectorias divergentes y ciclos no triviales.

---

## Biyección e isomorfismo estructural

La sección 10 del manuscrito introduce explícitamente el acoplamiento entre el espacio de índices y el sistema clásico.

Se define el mapeo \(\Phi(N)=N+4\), y se demuestra su inyectividad. La sobreyectividad se formula sobre el dominio (\(N \ge 4\)), mientras que los elementos basales (\(\{1,2,3\}\)) se incorporan mediante las condiciones de borde correspondientes.

Posteriormente se estudia la variable \(z=5n+k\) como variable de estado destinada a preservar la estructura dinámica del operador clásico. El propósito de esta construcción es establecer la correspondencia entre la dinámica parametrizada y la dinámica clásica de Collatz.

---

## Condiciones basales

El sistema contempla explícitamente los estados basales y sus rutas asociadas.

En particular, se consideran las estructuras *\(R*(0) = 4 \to 2 \to 1\) y *\(R*(2) = 6 \to 3 \to 10 \sim R*(1)\) que constituyen los núcleos basales utilizados para acoplar el sistema parametrizado con las trayectorias clásicas.

---

## Verificación formal en Lean 4

Una parte fundamental del proyecto consiste en la formalización mecánica de los resultados matemáticos. El archivo principal de formalización es:

```text
CollatzStabilization.lean
```

El manuscrito especifica que el código está diseñado para ejecutarse en **Lean 4 v4.11.0** y que la arquitectura de formalización reproduce la estructura matemática desarrollada en el texto.

Entre los componentes formalizados se encuentran:
* La cobertura dinámica;
* La exclusividad de las familias;
* Las aplicaciones afines asociadas al espacio parametrizado;
* Las relaciones estructurales de la variable (\(z\));
* Las propiedades de estabilidad;
* Las recursiones contractivas del sistema.

La estrategia de formalización incluye, entre otros, los teoremas:

```text
cobertura_dinamica
exclusividad_estanca
```

permitiendo auditar separadamente la cobertura y la exclusividad del espacio de trabajo.

---

## Reproducción

Para reproducir la verificación formal se requiere:
* Lean 4;
* Mathlib;
* El archivo `CollatzStabilization.lean`;
* Los archivos auxiliares incluidos en el repositorio.

La compilación del proyecto permite comprobar mecánicamente las declaraciones y demostraciones formalizadas en Lean. El código Lean constituye la parte destinada a la verificación formal, mientras que los scripts auxiliares permiten reproducir los experimentos computacionales descritos en el manuscrito.

---

## Resultados computacionales

El manuscrito complementa la formalización con experimentos computacionales destinados a estudiar la dinámica de las trayectorias y el comportamiento del sistema a gran escala. Estos experimentos tienen carácter complementario respecto de la demostración matemática y la formalización en Lean.

---

## Extensión a estructuras aritméticas especiales

El trabajo incluye además un análisis específico de los **primos de Mersenne**.

La sección 12 estudia su correspondencia con las subclases modulares del sistema y demuestra una parametrización específica mediante la variable maestra ($z$).

El análisis muestra que los exponentes primos impares de los números de Mersenne conducen a una estructura particular dentro de la Subclase II y a una progresión modular asociada.

---

## Manuscrito

El desarrollo matemático completo, las definiciones, lemas, teoremas, demostraciones y resultados experimentales se encuentran en el manuscrito incluido en este repositorio.

**Título:**
> *Análisis de Estabilidad Asintótica Global e Isomorfismo Bivariado mediante Verificación Formal en Lean 4*

---

## Reproducibilidad y auditoría

El proyecto está concebido para permitir la inspección independiente de:
1. Las definiciones matemáticas;
2. La parametrización bivariada;
3. El Teorema de Cobertura;
4. La construcción de la variable ($z$);
5. La biyección con el espacio clásico;
6. El isomorfismo dinámico;
7. Las funciones de estabilidad;
8. La formalización en Lean 4;
9. Los experimentos computacionales.

La disponibilidad del código fuente permite que terceros puedan compilar y auditar independientemente la formalización.

---

## Estado del proyecto

**Estado:** Investigación matemática y formalización computacional.

**Área:** Teoría de números / sistemas dinámicos discretos / verificación formal.

**Herramientas principales:**
* Lean 4
* Mathlib
* Python

---

## Autor

**Profesor Santiago López**  
Investigación independiente en teoría de números

---

## Licencia

Este proyecto está bajo la **Licencia MIT**. Consulte el archivo `LICENSE` adjunto en este repositorio para obtener más detalles sobre los derechos de uso, modificación y distribución privada de los teoremas y métodos computacionales aquí descritos.
