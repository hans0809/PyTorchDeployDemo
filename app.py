import os
import time
from flask import Flask, render_template, request, redirect

from inference import get_prediction
from commons import format_class_name
import numpy as np
import io
from PIL import Image

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])#必须两个都写
def upload_file():
    print('hahah')
    if request.method == 'POST':
        print('i use post')
        print('request.url:',request.url)
        print('request.files:',request.files)
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return
        img_bytes = file.read()
        print('img_bytes:',img_bytes)
        image = Image.open(io.BytesIO(img_bytes))
        image_name=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
        image.save('static\{}.png'.format(image_name))

        class_id, class_name = get_prediction(image_bytes=img_bytes)
        class_name = format_class_name(class_name)
        print('image_name:',image_name)
        return render_template('result.html', class_id=class_id,
                               class_name=class_name,image_name=image_name+'.png')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
