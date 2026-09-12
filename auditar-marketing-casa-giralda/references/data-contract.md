# Contrato mínimo de datos

## Redes sociales

CSV UTF-8, una fila por publicación:

`platform,date,content_id,title,url,content_type,organic_or_paid,views,reach,likes,comments,shares,saves,followers_gained,watch_time_seconds,avg_watch_seconds,duration_seconds,profile_visits,link_clicks,inquiries`

Obligatorios: `platform`, `date`, `content_id`. Las métricas no disponibles pueden quedar vacías.

- interacción por alcance = (likes + comments + shares + saves) / reach
- compartidos = shares / reach
- guardados = saves / reach
- finalización aproximada = avg_watch_seconds / duration_seconds
- acción = (link_clicks + inquiries) / reach

No sumar alcance entre plataformas como personas únicas.

## Sitio web

CSV UTF-8, una fila por página y fuente o totales diarios:

`date,source,page,users,sessions,organic_sessions,engaged_sessions,whatsapp_clicks,event_form_starts,event_form_submits,booking_starts,bookings`

- interacción = engaged_sessions / sessions
- WhatsApp = whatsapp_clicks / sessions
- conversión de formulario = event_form_submits / event_form_starts
- conversión de reserva = bookings / booking_starts

## Search Console

Exportar consultas y páginas por separado:

`query_or_page,clicks,impressions,ctr,position`

Separar marca (`Casa Giralda`) y no marca (`hospedaje en Baños`, `eventos Baños`, etc.). No comparar posición promedio sin revisar impresiones y mezcla de consultas.

## Videos

Entregar URL o archivo de máximo seis videos con sus métricas. Si la plataforma impide abrirlos, usar originales o grabaciones de pantalla.
