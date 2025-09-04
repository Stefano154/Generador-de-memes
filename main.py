# Importar las librerías necesarias de Flask
from flask import Flask, render_template, request, send_from_directory

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal que muestra la página y procesa el formulario
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Muestra la página principal.
    - Si el usuario entra por primera vez (GET), carga una imagen por defecto.
    - Si el usuario envía el formulario (POST), recoge la imagen seleccionada,
      el color, el texto superior/inferior y su posición, y los pasa al template.
    """
    if request.method == 'POST':
        # Recoger la imagen seleccionada por el usuario
        selected_image = request.form.get('image-selector')

        # Recoger el color elegido para el texto o elementos visuales
        selected_color = request.form.get('color-selector')

        # Recoger el texto a mostrar (superior e inferior)
        text_top = request.form.get("textTop")
        text_bottom = request.form.get("textBottom")

        # Recoger la posición vertical (Y) de cada texto
        text_top_y = request.form.get("textTop_y")
        text_bottom_y = request.form.get("textBottom_y")

        # Renderizar la página HTML con los datos enviados por el usuario
        return render_template(
            'index.html',
            selected_image=selected_image,  # Imagen elegida
            text_top=text_top,              # Texto superior
            text_bottom=text_bottom,        # Texto inferior
            selected_color=selected_color,  # Color seleccionado
            text_top_y=text_top_y,          # Posición Y del texto superior
            text_bottom_y=text_bottom_y     # Posición Y del texto inferior
        )
    else:
        # Si no hay datos enviados (GET), mostrar la imagen por defecto
        return render_template('index.html', selected_image='logo.svg')


# Ruta para servir imágenes estáticas desde la carpeta "static/img"
@app.route('/static/img/<path:path>')
def serve_images(path):
    """
    Permite acceder a las imágenes almacenadas en 'static/img'
    escribiendo su nombre en la URL.
    """
    return send_from_directory('static/img', path)


# Ejecutar la aplicación en modo desarrollo (debug=True para reinicios automáticos)
app.run(debug=True)