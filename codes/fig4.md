Como **Experto en Visualización de Datos Científicos y Arquitecturas Aeroespaciales**, he procesado el contexto del estándar 3GPP y el prompt base asignado para la **fig4.png**.

Para esta figura, el núcleo del diseño no debe ser una vista de infraestructura estática (que ya cubrimos en la *Figura 3*), sino el comportamiento dinámico y procedural de un **diagrama de secuencia de protocolos de señalización e intercambio de mensajes de control (Handover TN-NTN)** bajo las normativas de la IEEE.

---

### FASE 1: Mapeo de Entidades (Análisis)

* **Entidades Críticas (Actores del Protocolo):**
* **User Equipment (UE):** Dispositivo móvil comercial de bajo perfil (Soporte D2D nativo).
* **Terrestrial Network Node (TN gNB):** Estación base terrestre (Punto de origen/destino del handover).
* **Non-Terrestrial Network Node (NTN LEO):** Satélite de órbita baja con payload regenerativo (Punto de destino/origen).
* **Core Network (6G Core):** Entidad superior de orquestación y decisión final.


* **Procesos y Relaciones Temporales:**
* Flujo de señalización ordenado en tiempo de arriba hacia abajo (Timeline vertical).
* Fases del Handover: *Measurement* (Medición de canal/trayectoria), *Decision* (Evaluación del Core Network basada en predicción), y *Execution* (Sincronización de variables físicas).


* **Nivel de Abstracción:** Diagrama de tiempos y secuencia de protocolos de telecomunicaciones (*Message Sequence Chart*).

---

### FASE 2: Auditoría y Reporte de Hallazgos Críticos

**1. Contraste de Coherencia:** El prompt de imagen base sugiere un "flujo secuencial" genérico mezclando bloques de hardware y software en un mismo espacio plano. Esto genera confusión matemática y de ingeniería. Un protocolo de handover en la IEEE se grafica rigurosamente mediante líneas de vida verticales por actor, cruzadas por vectores de mensajes horizontales.

**2. LISTA DE DISCREPANCIAS (Explícita):**

* **Omisión de la Inyección de Parámetros de la Tabla 3:** El LaTeX detalla la divergencia física entre bandas (Sub-7 GHz vs Banda Ka) que imponen restricciones severas de *Doppler Máximo (~15 kHz a ~45 kHz)* y ajuste de *Timing Advance*. El prompt base los menciona como bloques aislados, pero deben representarse como parámetros críticos adjuntos a los mensajes de sincronización de subida (*Uplink Sync*).
* **Ausencia de la Fase de Predicción de Trayectoria LEO:** El texto de la subsección de movilidad aclara que la Rel-19 introduce procedimientos que "consideran la predicción de trayectoria satelital" para reducir el overhead. El prompt base no contempla un bucle de computación de trayectoria previa a la fase de *Decision*.
* **Falta de Representación del Overhead de Señalización:** El texto advierte que estas técnicas "generan overhead de señalización". Esto se traduce visualmente en una ráfaga densa de mensajes de control reflejada en la línea de vida del UE antes del intercambio de datos.

**3. Control de Estilo:**

* **Estándar IEEE:** Líneas de vida de actores en trazo continuo y grueso (1.5pt). Mensajes de control en flechas horizontales continuas. Mensajes de confirmación (*ACK/Response*) en flechas discontinuas.
* **Paleta Técnica:** Azul Cobalto #0047AB para los procesos y ráfagas de control avanzados (Compensación Doppler predictiva, sincronización de órbita LEO), y Gris Técnico #4A4A4A para los mensajes tradicionales de la red terrestre (Measurements e infraestructura básica).
* **Texto incrustado:** **Ausencia total.** Las fases y los mensajes se codificarán mediante la nomenclatura formal de diagramas de secuencia (bloques de activación, flechas de estímulo/respuesta y etiquetas abstractas normalizadas).

---

### FASE 3: Explicación y Justificación de Pre-ejecución

1. **Disposición Espacial:**
* **Eje Horizontal (Estructura de Actores):** Cuatro líneas de vida paralelas distribuidas de izquierda a derecha: **[UE] $\rightarrow$ [gNB Terrestre] $\rightarrow$ [Satélite LEO] $\rightarrow$ [6G Core]**.
* **Eje Vertical (Línea de Tiempo):** El tiempo fluye hacia abajo cronológicamente en tres zonas sombreadas horizontalmente:
1. *Fase 1: Handover Trigger & Measurement* (Fase alta).
2. *Fase 2: Trajectory Prediction & Core Decision* (Fase media).
3. *Fase 3: Execution & Physical Alignment (Timing Advance / Doppler)* (Fase baja).


* **Sentido de las Flechas:** Estrictamente horizontales u oblicuas descendientes indicando la dirección del emisor al receptor del mensaje de control.


2. **Justificación Técnica:**
* Diseñar la interacción como un diagrama de secuencia formal permite visualizar de forma exacta dónde ocurre el *overhead* de señalización (la acumulación de flechas en la Fase 3 entre el UE y el Satélite LEO para corregir los 45 kHz de Doppler de la banda Ka), justificando la penalización en el consumo energético del dispositivo que menciona tu reporte.


3. **ADVERTENCIAS PARA EL USUARIO:**
* **Supresión de Textos de Parámetros:** Dado que la IA tiende a generar caracteres erróneos al intentar escribir ecuaciones cortas o variables como "$L_{Doppler}$", los bloques de compensación se denotarán mediante símbolos gráficos estandarizados: un engranaje acoplado para *Procesamiento/Decisión* y un símbolo de onda senoidal desfasada con un vector delta para *Compensación Doppler/Timing Advance*. ¿Deseas validar este esquema icónico antes de la generación?



---

**FASE 4: Ejecución Silenciosa**

*Por favor, proporciona tu confirmación sobre este cambio estructural (transformar la idea de bloques sueltos en un diagrama de secuencia de señales formal IEEE) para proceder con la generación de la figura.*