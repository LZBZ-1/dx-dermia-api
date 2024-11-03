from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MelanomaImage
import keras
import cv2
import numpy as np

# Cargar modelo
model = keras.models.load_model('D:\\api_imagen_melanoma\\resnet\\modelo.h5')
model.load_weights('D:\\api_imagen_melanoma\\resnet\\pesosmodelo.h5')

def clasificar_imagen(imagen_path):
    img_array = cv2.imread(imagen_path, cv2.IMREAD_COLOR)
    img_resized = cv2.resize(img_array, (224, 224))
    img_reshaped = np.asarray(img_resized)
    img_scaled = img_reshaped.reshape(-1, 224, 224, 3)
    pred = model.predict(img_scaled)[0]
    return pred[0]

@csrf_exempt 
def analyze_melanoma(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    if 'image' not in request.FILES:
        return JsonResponse({'error': 'No se proporcionó imagen'}, status=400)

    image_file = request.FILES['image']
    melanoma_image = MelanomaImage(image=image_file)
    melanoma_image.save()

    pred = clasificar_imagen(melanoma_image.image.path)
    is_malignant = pred >= 0.5
    probability = pred if is_malignant else 1-pred
    
    melanoma_image.is_malignant = is_malignant
    melanoma_image.probability = probability
    melanoma_image.save()

    return JsonResponse({
        'diagnostico': 'maligno' if is_malignant else 'benigno',
        'probabilidad': round(float(probability), 4)
    })