# PortSpy - Escaner de Puertos
Algoritmos y Estructuras de Datos 1

## Integrantes (Grupo 16)
- Federico Castillo Menegotto  
- Jesus Cambronero  
- Matias Diaz  
- Santiago Brandes  

## Introducción
Cada dispositivo conectado a una red utiliza puertos para comunicarse con otros equipos y servicios. Saber qué puertos están activos en una computadora o servidor puede ayudarnos a detectar posibles vulnerabilidades o simplemente entender mejor cómo funciona una red.

PortSpy es una herramienta desarrollada en Python que permite explorar dispositivos dentro de una red. Su función principal es enumerar endpoints, escanear puertos y visualizar su estado de forma clara y ordenada.

## Alcance del producto
**Funcionalidades del sistema:**
- Escaneo de red con sockets.
- Barrido de CIDR (192.168.1.0/24). 
- Almacenar outputs en archivos. 
- Input usando archivos.
- Ejecución con argumentos
- Banner Grabbing.
- Ingreso de rangos de puertos.
- Escaneo de puertos con concurrencia (threading).
- Detección del estado de cada puerto.
- Escaneo de múltiples hosts.
- Búsqueda de patrones con re.
- Presentación de resultados con tablas.

## Requisitos funcionales (29/5/25)

| Tema de la materia                          | Implementación en el proyecto                                                                 |
|--------------------------------------------|-----------------------------------------------------------------------------------------------|
| Listas                                      | Convertir IPs de un archivo a listas para poder ejecutar los escaneos  |
| Matrices                                    | Mostrar estado de puertos, banners y hosts.                                                   |
| Funciones Lambda, Reduce, Filter y Slicing | Obtener puertos abiertos, contar puertos abiertos, ordenar output por puertos y extraer sublistas de puertos. |
| Funciones de Cadena de Caracteres          | Limpiar IP (sacar los espacios en blanco), normalizar estado de puertos, obtener prefijo de red y comprar estados de puertos. |
| Diccionarios y Tuplas | Uso de tuplas en puertos comunes (TOP_COMMON_PORTS). Uso de diccionarios al almacenar escaneos a multiples hosts |
| Try y Except  | Implementado en network_scanner.py para atajar timeouts (por ejemplo puerto 135, 139 y 445) y errores |
| Test Unitarios | Implementado en tests_operaciones_matriz.py para verificar que el formato de almacenamiento de los escaneos sea correcto |
| Manejo de Archivos | Implementado en leer_ips.py (Lee un archivo de texto con una ip por  línea) y en exportar_escaneo.py (Exporta el escaneo a un archivo JSON  si una flag y el nombre del archivo es especificado) | 

## Flujo del usuario
El usuario ejecuta la herramienta en la terminal, pasando el host y rango de puertos (opcional) por argumentos.  
El programa emite tráfico de red (paquetes TCP, HTTP. SMB, etc) e intenta establecer un “Three Way Handshake” con determinados puertos.  
Posteriormente intenta hacer Banner Grabbing.  
Luego almacena la ip, el puerto, el estado y el banner y es mostrado por consola.

## Tecnologías Propuestas
- **Lenguaje Principal:** Python  
- **Framework:** Python (Socket)  
- **Librerías:** Socket, Concurrent.futures, Functools  
- **Almacenamiento:** JSON y Archivo de Texto

## Glosario
**Socket:** Un socket es un punto final en una comunicación de red, que puede enviar y recibir datos a través de una dirección IP y un puerto. Es como un punto de conexión para comunicarse entre dos dispositivos (o procesos) a través de una red.

**Thread:** Un thread (o hilo en español) es una unidad de ejecución dentro de un proceso. Un proceso puede tener múltiples hilos que se ejecutan de manera concurrente, compartiendo la misma memoria y recursos.

**TCP:** El Transmission Control Protocol (TCP) es un protocolo de comunicación que permite el envío confiable de datos entre dispositivos en una red. Es uno de los protocolos principales de Internet y se usa en aplicaciones como la web (HTTP/HTTPS), correo electrónico (SMTP, IMAP) y transferencia de archivos (FTP).

**Three Way Handshake:** El three-way handshake es el proceso de establecimiento de conexión en TCP. Consiste en tres intercambios de paquetes entre el cliente y el servidor para asegurarse de que ambos están listos para comunicarse de manera confiable.

**Endpoint:** Son los puntos de entrada y salida de información a la red, y por lo tanto, son objetivos potenciales de ataques cibernéticos. 
