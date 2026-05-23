**PARTE 1: ESTRUCTURA JSON**

```json
{
  "titulo": "Convergencia de Conectividad Direct-to-Device (D2D) y Redes No Terrestres (NTN): Arquitecturas, Estándares y Desafíos en el Ecosistema 6G",
  "folder_name": "d2d_ntn_6g_convergence",
  "abstract_preliminar": "La convergencia entre conectividad Direct-to-Device (D2D) y Redes No Terrestres (NTN) representa un pilar fundamental para el ecosistema 6G, habilitando cobertura ubicua, resiliencia y nuevos servicios para dispositivos estándar. Este artículo presenta un marco técnico integral que analiza arquitecturas híbridas TN-NTN, evoluciones de estándares 3GPP (Rel-17 a Rel-19 y perspectivas 6G), y desafíos técnicos clave como compensación Doppler, movilidad, gestión de interferencias y optimización de recursos. Se propone una arquitectura de referencia unificada con payloads regenerativos, orquestación inteligente TN/NTN y soporte nativo para D2D en bandas sub-7 GHz y Ka. Se discuten métricas de desempeño, simulaciones de cobertura y trade-offs entre throughput, latencia y consumo energético. Los resultados destacan mejoras significativas en disponibilidad de servicio y eficiencia espectral, estableciendo una base reproducible para el despliegue de redes 6G verdaderamente integradas y resilientes.",
  "secciones": [
    {
      "nro": 1,
      "titulo_seccion": "Introducción",
      "objetivos": ["Motivar la necesidad de convergencia TN-NTN en 6G", "Definir alcance del marco propuesto", "Presentar contribuciones principales"],
      "subsecciones": ["1.1 Motivación y Contexto 6G", "1.2 Evolución de NTN y D2D", "1.3 Contribuciones del Trabajo"],
      "insumos": ["Figura 1: Visión general de la arquitectura", "Tabla 1: Comparación TN vs NTN"],
      "llaves_bibtex": ["Ullah2026_D2D", "Wang2025_NTN6G", "DeGaudenzi2026_NTN"]
    },
    {
      "nro": 2,
      "titulo_seccion": "Estado del Arte",
      "objetivos": ["Revisar estándares 3GPP", "Analizar arquitecturas existentes", "Identificar brechas técnicas"],
      "subsecciones": ["2.1 Evolución 3GPP NTN (Rel-17 a Rel-19)", "2.2 Avances en D2D Satelital", "2.3 Integración TN-NTN en 6G"],
      "insumos": ["Tabla 2: Comparativa de Releases 3GPP", "Figura 2: Evolución temporal de publicaciones"],
      "llaves_bibtex": ["Pasandi2024_D2DSurvey", "Wang2025_NTN6G", "Ericsson2025_NTN"]
    },
    {
      "nro": 3,
      "titulo_seccion": "Arquitecturas Propuestas",
      "objetivos": ["Definir arquitectura de referencia", "Especificar componentes clave", "Integrar D2D con NTN"],
      "subsecciones": ["3.1 Arquitectura Híbrida TN-NTN", "3.2 Payloads Regenerativos y Orquestación", "3.3 Soporte D2D en Bandas Sub-7 GHz y Ka"],
      "insumos": ["Figura 3: Diagrama del marco propuesto", "Eq. 1: Modelo de link budget D2D-NTN"],
      "llaves_bibtex": ["Ullah2026_D2D", "DeGaudenzi2026_NTN", "Basciani2026_RA"]
    },
    {
      "nro": 4,
      "titulo_seccion": "Estándares y Tecnologías Habilitadoras",
      "objetivos": ["Analizar especificaciones 3GPP", "Describir tecnologías clave", "Evaluar interoperabilidad"],
      "subsecciones": ["4.1 3GPP Releases y Roadmap 6G", "4.2 Técnicas de Mitigación Doppler y Movilidad", "4.3 Gestión de Recursos e Interferencias"],
      "insumos": ["Tabla 3: Requisitos técnicos por banda", "Figura 4: Protocolos de handover TN-NTN"],
      "llaves_bibtex": ["Ericsson2025_NTN", "3GPP_NTNR19", "Pasandi2024_D2DSurvey"]
    },
    {
      "nro": 5,
      "titulo_seccion": "Desafíos Técnicos y Soluciones",
      "objetivos": ["Identificar limitaciones principales", "Proponer mitigaciones", "Analizar trade-offs"],
      "subsecciones": ["5.1 Desafíos de Canal y Propagación", "5.2 Movilidad y Handover", "5.3 Eficiencia Energética y Escalabilidad"],
      "insumos": ["Tabla 4: Trade-offs arquitectónicos", "Figura 5: Análisis de cobertura simulada"],
      "llaves_bibtex": ["DeGaudenzi2026_NTN", "Wang2025_NTN6G", "Ullah2026_D2D"]
    },
    {
      "nro": 6,
      "titulo_seccion": "Discusión y Implicaciones",
      "objetivos": ["Interpretar hallazgos", "Analizar impacto operativo", "Discutir aspectos regulatorios"],
      "subsecciones": ["6.1 Implicaciones para Despliegues Comerciales", "6.2 Aspectos Regulatorios y Éticos", "6.3 Comparación con Estado del Arte"],
      "insumos": ["Tabla 5: Comparación de arquitecturas"],
      "llaves_bibtex": ["Wang2025_NTN6G", "Ericsson2025_NTN"]
    },
    {
      "nro": 7,
      "titulo_seccion": "Conclusiones y Trabajos Futuros",
      "objetivos": ["Sintetizar contribuciones", "Proponer líneas futuras", "Destacar impacto en 6G"],
      "subsecciones": ["7.1 Conclusiones Principales", "7.2 Direcciones de Investigación Futuras"],
      "insumos": [],
      "llaves_bibtex": ["Ullah2026_D2D", "DeGaudenzi2026_NTN", "Wang2025_NTN6G"]
    }
  ]
}
```

**PARTE 2: BLOQUES BIBLIOGRÁFICOS SECCIONALES**

```bibtex
@article{Ullah2026_D2D,
  author    = {Ullah, M. A. and others},
  title     = {Direct-to-Device Connectivity for Integrated CNS in 6G NTN},
  journal   = {IEEE Transactions on Aerospace and Electronic Systems},
  year      = {2026},
  doi       = {10.1109/TAES.2026.XXXXXXX},
  url       = {https://arxiv.org/abs/2603.11848},
  note      = {[Online]. Available: https://arxiv.org/pdf/2603.11848}
}

@article{Wang2025_NTN6G,
  author    = {Wang, F. and Zhang, S. and others},
  title     = {Non-Terrestrial Networking for 6G: Evolution, Opportunities, and Future Directions},
  journal   = {Engineering},
  year      = {2025},
  doi       = {10.1016/j.eng.2025.05.013},
  url       = {https://www.sciencedirect.com/science/article/pii/S2095809925002917},
  note      = {[Online]. Available: https://doi.org/10.1016/j.eng.2025.05.013}
}

@article{DeGaudenzi2026_NTN,
  author    = {De Gaudenzi, R. and others},
  title     = {Beyond 5G non terrestrial networks for direct-to-device joint communication and positioning services},
  journal   = {npj Wireless Technology},
  year      = {2026},
  doi       = {10.1038/s44459-026-00047-w},
  url       = {https://www.nature.com/articles/s44459-026-00047-w},
  note      = {[Online]. Available: https://www.nature.com/articles/s44459-026-00047-w}
}
```

```bibtex
@article{Pasandi2024_D2DSurvey,
  author    = {Pasandi, H. B. and others},
  title     = {A Survey on Direct-to-Device Satellite Communications: Advances, Challenges and Opportunities},
  journal   = {arXiv preprint},
  year      = {2024},
  doi       = {10.48550/arXiv.2410.XXXXX},
  url       = {https://par.nsf.gov/servlets/purl/10595613},
  note      = {[Online]. Available: https://par.nsf.gov/servlets/purl/10595613}
}

@article{Ericsson2025_NTN,
  author    = {Ericsson Research},
  title     = {Satellite direct to device: 4G or 3GPP NTN?},
  journal   = {Ericsson Technology Review},
  year      = {2025},
  url       = {https://www.ericsson.com/en/reports-and-papers/ericsson-technology-review/articles/satellite-direct-to-device-communication},
  note      = {[Online]. Available: https://www.ericsson.com/en/reports-and-papers/ericsson-technology-review/articles/satellite-direct-to-device-communication}
}

@misc{3GPP_NTNR19,
  author    = {3GPP},
  title     = {NR NTN Enhancements in Release 19},
  year      = {2025},
  url       = {https://www.3gpp.org/technologies/ntn-overview},
  note      = {[Online]. Available: https://www.3gpp.org/technologies/ntn-overview}
}
```

```bibtex
@article{Basciani2026_RA,
  author    = {Basciani, F. and others},
  title     = {Reference architecture for autonomy and adaptivity in satellite systems},
  journal   = {Journal of Systems and Software},
  year      = {2026},
  url       = {https://www.sciencedirect.com/science/article/abs/pii/S0164121226000361},
  note      = {[Online]. Available: https://doi.org/10.1016/j.jss.2026.XXXXX}
}
```

**PARTE 3: MAPA DE USO DE REFERENCIAS (POR SECCIÓN)**

```json
{
  "seccion_nro": 1,
  "titulo_seccion": "Introducción",
  "mapa_uso": {
    "Ullah2026_D2D": {
      "razon_seleccion": "Ejemplo reciente de D2D para conectividad integrada en 6G NTN.",
      "guia_redaccion": "Usar en 1.2-1.3 para motivar D2D en escenarios aéreos y terrestres, destacando roaming TN-NTN.",
      "subseccion_destino": "1.2"
    },
    "Wang2025_NTN6G": {
      "razon_seleccion": "Revisión comprehensiva de NTN en el contexto 6G.",
      "guia_redaccion": "Citar en 1.1 para contextualizar evolución y oportunidades de integración.",
      "subseccion_destino": "1.1"
    },
    "DeGaudenzi2026_NTN": {
      "razon_seleccion": "Análisis de arquitecturas LEO para D2D joint communication-positioning.",
      "guia_redaccion": "Introducir en 1.3 como base inspiradora para el marco propuesto.",
      "subseccion_destino": "1.3"
    }
  }
}
```

```json
{
  "seccion_nro": 2,
  "titulo_seccion": "Estado del Arte",
  "mapa_uso": {
    "Pasandi2024_D2DSurvey": {
      "razon_seleccion": "Survey exhaustivo sobre D2D satelital.",
      "guia_redaccion": "Usar en 2.2 para resumir avances, desafíos y ecosistema comercial.",
      "subseccion_destino": "2.2"
    },
    "Wang2025_NTN6G": {
      "razon_seleccion": "Evolución y direcciones futuras de NTN en 6G.",
      "guia_redaccion": "Base principal para 2.3, destacando orquestación y slicing.",
      "subseccion_destino": "2.3"
    },
    "Ericsson2025_NTN": {
      "razon_seleccion": "Perspectiva industrial sobre D2D NTN vs alternativas.",
      "guia_redaccion": "Contrastar en 2.1 con estándares 3GPP actuales.",
      "subseccion_destino": "2.1"
    }
  }
}
```

```json
{
  "seccion_nro": 3,
  "titulo_seccion": "Arquitecturas Propuestas",
  "mapa_uso": {
    "Ullah2026_D2D": {
      "razon_seleccion": "Arquitectura D2D para ICNS en NTN.",
      "guia_redaccion": "Apoyar 3.1 y 3.3 con ejemplos de roaming seamless.",
      "subseccion_destino": "3.1"
    },
    "DeGaudenzi2026_NTN": {
      "razon_seleccion": "Candidatas arquitecturas LEO para D2D.",
      "guia_redaccion": "En 3.2 para payloads y trade-offs de posicionamiento/comunicación.",
      "subseccion_destino": "3.2"
    },
    "Basciani2026_RA": {
      "razon_seleccion": "Arquitectura de referencia para adaptividad satelital.",
      "guia_redaccion": "Base modular para la propuesta en 3.1.",
      "subseccion_destino": "3.1"
    }
  }
}
```

```json
{
  "seccion_nro": 4,
  "titulo_seccion": "Estándares y Tecnologías Habilitadoras",
  "mapa_uso": {
    "Ericsson2025_NTN": {
      "razon_seleccion": "Análisis detallado de 3GPP NTN D2D.",
      "guia_redaccion": "Principal referencia para roadmap en 4.1.",
      "subseccion_destino": "4.1"
    },
    "3GPP_NTNR19": {
      "razon_seleccion": "Documentación oficial 3GPP sobre NTN Rel-19.",
      "guia_redaccion": "Citar especificaciones técnicas en 4.1 y 4.2.",
      "subseccion_destino": "4.1"
    },
    "Pasandi2024_D2DSurvey": {
      "razon_seleccion": "Desafíos prácticos de implementación D2D.",
      "guia_redaccion": "Apoyar mitigaciones en 4.3.",
      "subseccion_destino": "4.3"
    }
  }
}
```

```json
{
  "seccion_nro": 5,
  "titulo_seccion": "Desafíos Técnicos y Soluciones",
  "mapa_uso": {
    "DeGaudenzi2026_NTN": {
      "razon_seleccion": "Análisis profundo de desafíos D2D en LEO.",
      "guia_redaccion": "Usar en 5.1 y 5.2 para Doppler, movilidad y arquitecturas.",
      "subseccion_destino": "5.1"
    },
    "Wang2025_NTN6G": {
      "razon_seleccion": "Oportunidades y limitaciones en integración 6G.",
      "guia_redaccion": "En 5.3 para escalabilidad y eficiencia energética.",
      "subseccion_destino": "5.3"
    },
    "Ullah2026_D2D": {
      "razon_seleccion": "Limitaciones en entornos reales.",
      "guia_redaccion": "Apoyar análisis de cobertura en 5.1.",
      "subseccion_destino": "5.1"
    }
  }
}
```

```json
{
  "seccion_nro": 6,
  "titulo_seccion": "Discusión y Implicaciones",
  "mapa_uso": {
    "Wang2025_NTN6G": {
      "razon_seleccion": "Implicaciones a futuro de NTN en 6G.",
      "guia_redaccion": "Base para 6.3 y comparación con estado del arte.",
      "subseccion_destino": "6.3"
    },
    "Ericsson2025_NTN": {
      "razon_seleccion": "Perspectiva comercial e industrial.",
      "guia_redaccion": "Discutir despliegues en 6.1.",
      "subseccion_destino": "6.1"
    }
  }
}
```

```json
{
  "seccion_nro": 7,
  "titulo_seccion": "Conclusiones y Trabajos Futuros",
  "mapa_uso": {
    "Ullah2026_D2D": {
      "razon_seleccion": "Visión integrada D2D-NTN.",
      "guia_redaccion": "Comparar contribuciones en 7.1.",
      "subseccion_destino": "7.1"
    },
    "DeGaudenzi2026_NTN": {
      "razon_seleccion": "Arquitecturas avanzadas joint COM-PNT.",
      "guia_redaccion": "Sugerir extensiones en 7.2.",
      "subseccion_destino": "7.2"
    },
    "Wang2025_NTN6G": {
      "razon_seleccion": "Direcciones futuras de investigación NTN.",
      "guia_redaccion": "Proponer líneas de trabajo en 7.2.",
      "subseccion_destino": "7.2"
    }
  }
}
```