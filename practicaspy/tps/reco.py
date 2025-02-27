import cv2
import tensorflow as tf
import numpy as np

# Cargar el modelo preentrenado MobileNetV2 de TensorFlow
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Preprocesar la imagen
def preprocess_image(frame):
    frame_resized = cv2.resize(frame, (224, 224))  # Redimensionar a 224x224 para MobileNetV2
    frame_array = np.array(frame_resized)  # Convertir a un array de numpy
    frame_array = np.expand_dims(frame_array, axis=0)  # Añadir una dimensión para el batch
    frame_array = tf.keras.applications.mobilenet_v2.preprocess_input(frame_array)  # Preprocesar la imagen
    return frame_array

# Acceder a la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar frame por frame
    ret, frame = cap.read()

    if not ret:
        break

    # Preprocesar la imagen
    preprocessed_frame = preprocess_image(frame)

    # Realizar la predicción
    predictions = model.predict(preprocessed_frame)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]

    # Mostrar las predicciones en la imagen
    label = decoded_predictions[0][1]  # Obtener el nombre de la clase
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Mostrar la imagen
    cv2.imshow('Object Recognition', frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
