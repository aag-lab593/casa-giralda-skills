---
name: auditar-marketing-casa-giralda
description: Auditar mensualmente el marketing digital de Casa Giralda en TikTok, Instagram y su sitio web. Usar al revisar resultados del mes, comparar videos, analizar GA4, Google Search Console o Google Trends, preparar el informe mensual, identificar qué funcionó y definir cambios para el siguiente mes con mínimo consumo de créditos.
---

# Auditor de Marketing Casa Giralda

## Objetivo

Convertir datos del día 1 al último día del mes en decisiones para aumentar consultas, reservas directas y cotizaciones de eventos.

## Reglas de eficiencia

1. Procesar números con `scripts/summarize_month.py`; no calcular fila por fila con el modelo.
2. Solicitar una sola entrega mensual de datos.
3. Analizar visualmente máximo seis videos: tres mejores y tres peores según el objetivo del mes.
4. Leer `references/data-contract.md` para preparar entradas y `references/report-structure.md` para redactar el informe.
5. No analizar Facebook, LinkedIn o Google Business Profile salvo petición explícita.
6. No inventar métricas, benchmarks, atribución ni ingresos. Marcar ausencias como “sin datos”.
7. Priorizar consultas, clics a WhatsApp, formularios y reservas sobre métricas de vanidad.

## Periodo

- Usar mes calendario completo, inclusive.
- Generar el cierre el último día del mes. Si todavía no terminó, rotularlo como corte parcial.
- Comparar con el mes anterior cuando exista una base comparable.

## Fuentes

- TikTok Analytics: vistas, tiempo medio, finalización, interacciones y seguidores.
- Instagram Insights: alcance, reproducciones, tiempo, guardados, compartidos, interacciones y seguidores.
- GA4: usuarios, sesiones, tráfico orgánico, páginas de entrada y conversiones.
- Search Console: consultas, páginas, clics, impresiones, CTR y posición promedio.
- Google Trends: contexto de demanda para Baños, hospedaje, eventos, piscina, feriados y promociones. No tratar Trends como tráfico propio.

Si no hay acceso directo, pedir CSV/XLSX o capturas del periodo. No bloquear el informe: emitir análisis parcial y listar exactamente qué falta.

## Flujo

1. Confirmar mes, objetivo comercial y promoción principal.
2. Validar cobertura del periodo y separar orgánico de pagado.
3. Normalizar archivos según `references/data-contract.md`.
4. Ejecutar `python3 scripts/summarize_month.py --social SOCIAL.csv --web WEB.csv --output resumen.json`.
5. Seleccionar videos por retención, compartidos y señal comercial; evitar elegir solo por vistas.
6. Revisar los seis videos disponibles: gancho de 0–3 s, promesa, ritmo, claridad, texto, prueba, CTA y comentarios.
7. Contrastar fuentes: Search Console explica visibilidad; GA4, comportamiento y conversiones; Trends, cambios externos en interés.
8. Redactar con `references/report-structure.md`.

## Decisiones

- **Escalar:** funcionó dos o más veces o generó señal comercial clara.
- **Probar:** hipótesis plausible con evidencia insuficiente; definir una prueba.
- **Corregir:** tema útil con problema de gancho, formato, CTA o página.
- **Detener:** repite bajo rendimiento sin señal comercial.

Cada recomendación debe incluir evidencia, cambio, responsable sugerido, indicador y fecha de revisión. Limitar el próximo mes a cinco acciones y máximo dos experimentos simultáneos.

## Resultado

Entregar un resumen ejecutivo con resultado, causas, decisiones y cinco acciones; añadir un anexo de métricas, contenidos, búsquedas, páginas y datos faltantes. Terminar con qué repetimos, qué dejamos, qué probamos y qué mediremos.
