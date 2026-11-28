# Custodia: buscador de envíos

Copia de respaldo del artifact publicado en claude.ai
(https://claude.ai/artifact/4DfAbYsxbJmyQFXj6wdyJW), versión 1795873282-53cd.

App para la bodega de custodia de una transportadora en Colombia: búsqueda de
envíos por descripción, registro con video, reclamos, inventario, conciliación
de guías, disposición final (rezago y donación) y tablero.

Funciona dentro de claude.ai: usa `window.claude` (base de datos compartida,
archivos, IA y perfil de usuario). Abierta como archivo local se ve la
interfaz, pero sin datos.

## Clientes y privacidad

- Los clientes reportan su envío en un formulario aparte
  (`formulario_cliente.html`, publicado en
  https://claude.ai/artifact/BAiMtJfmiKdPprtB8fpiB5). El formulario no lee
  ningún dato: arma el reporte y lo envía por WhatsApp a la empresa.
- Si alguien sin acceso de personal abre la app interna (lector, visitante de
  fuera de la organización o sin sesión), ve solo una pantalla para reportar
  su envío. Las reglas de la base de datos le impiden leer paquetes,
  reclamos, fotos y configuración. Solo `publico/portal` (nombre, logo, color
  y WhatsApp de la empresa) es legible para todos.
- El personal puede eliminar fotos, videos y reclamos (si la subida está
  restringida, solo el personal autorizado y los administradores). Cada
  eliminación pide un motivo y queda en el Tablero (quién, cuándo, por qué,
  sin guardar los datos borrados). Los archivos que la cuenta no pudo borrar
  quedan ocultos y un administrador termina de borrarlos desde el Tablero.

## Averías y objetos fuera de caja

- Pestaña **Averías**: entran solos los paquetes en los que la IA (al
  registrar o al agregar fotos/videos) o el personal vio daños, más los de
  empaque roto o mojado y producto dañado. Cada caso muestra si ya venía
  averiado al admitirlo. La revisión pasa por: por revisar → confirmada (por
  indemnizar) → indemnizada (valor y número de caso), o descartada. "Copiar
  lista para la transportadora" copia una tabla para Excel o correo.
- **Abrir y fotografiar el objeto** (ficha del paquete): disponible con más
  de 3 meses en custodia o en rezago (acta y testigo obligatorios), o con la
  autorización del cliente. El objeto queda fuera de su caja, con fotos; la IA
  declara su estado (bueno, usado, dañado parcial o total, vencido) y se le
  asigna estante aparte: `OB-` buen estado, `OD-` dañado. Los paquetes que
  siguen cerrados conservan los estantes A–D. Si está dañado, pasa a Averías.
- El registro con apertura ("Abierto en rezago" o con autorización) acepta
  fotos y ofrece dejar el objeto fuera de su caja con la misma regla de
  estantes. El Inventario filtra "Siguen en su caja" / "Fuera de caja".

## Pendiente: integración con los sistemas de la transportadora (pospuesta)

Estado: **pospuesta** (25 nov 2026). Nada se ha conectado todavía.

- Documento técnico para el equipo de TI de la transportadora:
  https://claude.ai/artifact/Gq3VhNCHbJfad5925ptrXN
- Datos a recibir: guías en novedad/custodia, admisiones con fotos, reclamos
  de clientes y capturas de cámaras.
- Frecuencia prevista: cada hora, solo lectura, solo registros nuevos.
- Para retomar: enviar el documento a TI, recibir la forma de entrega (API,
  archivos en su nube o vista de base de datos) y una credencial de pruebas;
  firmar el contrato de transmisión de datos (Ley 1581 de 2012).
- Cámaras en vivo (fase 2), también pospuesta: el documento trae las preguntas
  para TI (marca del grabador, acceso ONVIF/RTSP, computador por bodega en la
  red de las cámaras, autorización y avisos de videovigilancia). La fase 1,
  búsqueda en clips MP4 exportados, ya está en la pestaña Cámaras.

## Pendiente: imagen visual (pospuesta)

Estado: **pospuesta** (26 nov 2026). Quedó publicado el diseño "centro de mando"
(modo noche principal y modo día, paneles de vidrio, medidores de coincidencia,
pulso de la red) con marca blanca por empresa (Tablero → Marca de la empresa).

Para retomar: color por defecto de la marca Custodia (hoy cian eléctrico),
intensidad del brillo, logos y colores reales de las transportadoras clientes,
y una portada para la galería y los enlaces compartidos.
