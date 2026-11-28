# Custodia: buscador de envíos

Copia de respaldo del artifact publicado en claude.ai
(https://claude.ai/artifact/4DfAbYsxbJmyQFXj6wdyJW), versión 1795878437-f75c.

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

## Fotos y peso junto a cada envío

- Cada envío muestra su foto junto a la descripción en Buscar, Inventario,
  Rezago y disposición, Averías y Subastas, con una tira de las fotos sacadas
  del video (hasta 4 cuadros por video) y el peso.
- La foto de la báscula se guarda con el paquete (origen `bascula`): la que
  toma el personal con "Foto de la báscula", o el cuadro del video donde la IA
  leyó la pantalla. La ficha muestra el peso guardado y, si el personal lo
  corrigió, el peso que se leyó. La foto de la báscula no se usa en las
  comparaciones visuales.

## Paquetes en vinipel negro (no se pueden destapar)

- Casilla "Envuelto en vinipel negro" al registrar (la IA la marca sola si lo
  ve). Exige peso y medidas (largo x ancho x alto), muestra el protocolo de
  fotos y cambia los pasos de la grabación guiada: vuelta completa, vista de
  arriba con cinta métrica, linterna pegada al plástico para ver lo que se
  transparenta y de cerca lo que hay sobre el plástico.
- Comparación: si ambos paquetes están en vinipel, color, empaque y logos
  iguales no suman; si solo uno lo está, sus diferencias de caja no restan.
  Se agregó el rasgo "envoltura". Peso (±12 %) y medidas (±12 % o 3 cm)
  suman puntos; si no cuadran (más de 35 % de peso o 30 % / 6 cm de medida),
  el puntaje baja a 20 % como máximo. Se usa en reclamos (peso y medidas de la
  admisión de su guía o los que dio el cliente) y en el cruce con admisiones.
- La ficha de un paquete sin guía en vinipel o NN lista, sin IA, las
  admisiones y reclamos abiertos con el mismo peso y medidas.
- Reclamos y formulario del cliente piden el peso de la guía, las medidas y
  si iba envuelto en vinipel.

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
- Pestaña **Subastas**: los objetos abiertos que quedan en buen estado o
  usados. La IA reconoce el objeto en la foto y estima su precio nuevo y
  usado en Colombia (con lo que sabe la IA, no es una consulta en vivo; hay
  enlaces a MercadoLibre y Google Shopping para confirmarlo). Precio base
  sugerido: 60 % (bueno) o 50 % (usado) del precio de referencia, que es el
  precio verificado por el personal o, si no hay, el punto medio del usado
  estimado. Flujo: por tasar → precio por aprobar → lista → vendida (valor
  final y acta) o retirada. "Registrar venta" solo se activa cuando el lote
  de rezago cumplió el plazo de recuperación y el del ICBF, y si no hay un
  reclamo abierto que coincida. Confirmar con abogado que la subasta está
  permitida para rezagos postales.

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
