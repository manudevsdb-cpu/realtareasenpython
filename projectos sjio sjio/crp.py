import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Configuración del correo ---
remitente = "manudevsdva@gmail.com"
contraseña_app = "cmrq enyl dkmb orpu"
destinatario = "dmcardenasm@gmail.com"
asunto = "Mensaje desde Python"
mensaje = "Oli ama tengo hambre "

# --- Crear correo ---
correo = MIMEMultipart()
correo["From"] = remitente
correo["To"] = destinatario
correo["Subject"] = asunto
correo.attach(MIMEText(mensaje, "plain"))

# --- Enviar correo ---
try:
    servidor = smtplib.SMTP("smtp.gmail.com", 587)  # Servidor Gmail y puerto TLS
    servidor.starttls()  # Activar seguridad
    servidor.login(remitente, contraseña_app)
    servidor.send_message(correo)
    servidor.quit()
    print("Correo enviado ✅")
except Exception as e:
    print("Ocurrió un error:", e)