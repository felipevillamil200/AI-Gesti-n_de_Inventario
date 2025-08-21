=============================
ProductBuddy - Guía de Instalación
=============================

1️⃣ Requisitos Previos
---------------------
Antes de instalar ProductBuddy, asegúrate de tener:

- Python 3.10 o superior instalado
- Pip instalado
- Una cuenta y proyecto de Supabase con la tabla 'inventory'
- VS Code o cualquier editor de texto recomendado

---

2️⃣ Clonar el proyecto
---------------------
1. Descarga o clona el repositorio en tu computadora.
2. Abre la carpeta del proyecto en VS Code.

---

3️⃣ Crear entorno virtual
------------------------
En la terminal de VS Code, dentro de la carpeta del proyecto:

Windows PowerShell:
> python -m venv venv
> & .\venv\Scripts\Activate.ps1

Linux/Mac:
$ python3 -m venv venv
$ source venv/bin/activate

---

4️⃣ Instalar dependencias
------------------------
Con el entorno virtual activado, ejecuta:

> pip install -r requirements.txt

Si no tienes un `requirements.txt`, instala al menos:
- Flask
- supabase
- python-dotenv
- requests (si se usa en tu servicio de IA)

---

5️⃣ Configurar variables de entorno
----------------------------------
Crea un archivo `.env` en la raíz del proyecto con:

SUPABASE_URL=tu_supabase_url
SUPABASE_KEY=tu_supabase_anon_key

> Ejemplo:
> SUPABASE_URL=https://eqwagyesvjzbcciizcvr.supabase.co
> SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

---

6️⃣ Preparar inventario
----------------------
Puedes agregar productos de dos formas:

1. **Manual**: 
   - Entra a Supabase → Database → Tables → inventory → Browse Rows.
   - Edita los productos o agrega nuevos.

2. **CSV** (recomendado para muchos productos):
   - Crea un archivo `inventory.csv` con columnas:
     product_name,description,price,stock
   - Rellena los productos.
   - En Supabase → Browse Rows → Import CSV y selecciona tu archivo.

---

7️⃣ Ejecutar la aplicación
-------------------------
Con el entorno virtual activo:

> python app.py

- La aplicación Flask se ejecutará en: http://localhost:5000  
- Abre esa URL en tu navegador para usar ProductBuddy.

---

8️⃣ Probar la IA
----------------
- Escribe un mensaje en el chat, por ejemplo:
  - “Hola, ¿qué productos tienen?”
  - “Quiero comprar la Laptop X200”
- La IA te mostrará productos y gestionará la compra automáticamente.

---

9️⃣ Notas adicionales
--------------------
- Para agregar más productos en el futuro, simplemente edita la tabla `inventory` o importa un CSV actualizado.
- Asegúrate de tener stock suficiente antes de intentar compras.
- Puedes personalizar el comportamiento de la IA modificando `SYSTEM_PROMPT` en `utils/prompts.py`.

=============================
¡Listo! Ahora ProductBuddy está listo para usarse.
=============================
