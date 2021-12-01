import json

from commons import get_model, transform_image

model = get_model()
imagenet_class_index = json.load(open('imagenet_class_index.json'))


def get_prediction(image_bytes):

    try:
        tensor = transform_image(image_bytes=image_bytes)
        outputs = model.forward(tensor)
    except Exception:
        return 0, '出错了，请更换图片'
    print('outputs:',outputs.max(1))
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]
