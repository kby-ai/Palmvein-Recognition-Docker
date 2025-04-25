import sys
sys.path.append('.')

import os
import base64
import json
from ctypes import *
import cv2
import numpy as np
from flask import Flask, request, jsonify
from veinsdk import *
from roi import *

licensePath = "license.txt"
license = ""

machineCode = getMachineCode()
print("\nmachineCode: ", machineCode.decode('utf-8'))

try:
    with open(licensePath, 'r') as file:
        license = file.read().strip()
except IOError as exc:
    print("failed to open license.txt: ", exc.errno)

print("\nlicense: ", license)

ret = setActivation(license.encode('utf-8'))
print("\nactivation: ", ret)

ret = initSDK()
print("init: ", ret)

app = Flask(__name__) 

def mat_to_bytes(mat):
    """
    Convert cv::Mat image data (NumPy array in Python) to raw bytes.
    """
    # Encode cv::Mat as PNG bytes
    is_success, buffer = cv2.imencode(".png", mat)
    if not is_success:
        raise ValueError("Failed to encode cv::Mat image")
    return buffer.tobytes()

@app.route('/palmvein', methods=['POST'])
def palmvein():
    result = None
    score = None
    
    file1 = request.files['file1']
    file2 = request.files['file2']
    
    try:
        image1 = cv2.imdecode(np.frombuffer(file1.read(), np.uint8), cv2.IMREAD_COLOR)
    except:
        result = "Failed to open file1"
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    try:
        image2 = cv2.imdecode(np.frombuffer(file2.read(), np.uint8), cv2.IMREAD_COLOR)
    except:
        result = "Failed to open file2"
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
    roi1, label1 = get_roi_image(cv2.flip(image1, 1))
    roi2, label2 = get_roi_image(cv2.flip(image2, 1))

    if label1 != label2:
        result = "2 images are from the different hand"
        score = 0.0
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
        
    if roi1 is None or roi2 is None:
        result = "\n hand detection failed !\n plesae make sure that input hand image is valid or not."
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
    roi_byte1 = mat_to_bytes(roi1)
    roi_byte2 = mat_to_bytes(roi2)
    feature_array1, feature_array2 = (c_float * 1024)(), (c_float * 1024)()  # Assuming a maximum of 256 rectangles
    cnt1 = getFeature(roi_byte1, len(roi_byte1), feature_array1)
    cnt2 = getFeature(roi_byte2, len(roi_byte2), feature_array2)

    if cnt1 == 0 or cnt2 ==0:
        result = "feature extraction failed !"
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    score = getScore(feature_array1, cnt1, feature_array2, cnt2)
    if score >= 0.65:
        result = "Same Hand !"
        # print(f"\n 2 images are from the same hand\n similarity: {score}")
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    else:
        result = "Different Hand !"
        # print(f"\n 2 images are from the different hand\n similarity: {score}")
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response    

@app.route('/palmvein_base64', methods=['POST'])
def palmvein_base64():

    result = None
    score = None
    
    content = request.get_json()

    try:
        imageBase64 = content['base64_1']
        image_data = base64.b64decode(imageBase64) 
        np_array = np.frombuffer(image_data, np.uint8)
        image1 = cv2.imdecode(np_array, cv2.IMREAD_COLOR)   
    except:
        result = "Failed to open file1"
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    try:
        imageBase64 = content['base64_2']
        image_data = base64.b64decode(imageBase64) 
        np_array = np.frombuffer(image_data, np.uint8)
        image2 = cv2.imdecode(np_array, cv2.IMREAD_COLOR)   
    except:
        result = "Failed to open file2"
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
    roi1, label1 = get_roi_image(cv2.flip(image1, 1))
    roi2, label2 = get_roi_image(cv2.flip(image2, 1))

    if label1 != label2:
        result = "2 images are from the different hand"
        score = 0.0
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
        
    if roi1 is None or roi2 is None:
        result = "\n hand detection failed !\n plesae make sure that input hand image is valid or not."
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
    roi_byte1 = mat_to_bytes(roi1)
    roi_byte2 = mat_to_bytes(roi2)
    feature_array1, feature_array2 = (c_float * 1024)(), (c_float * 1024)()  # Assuming a maximum of 256 rectangles
    cnt1 = getFeature(roi_byte1, len(roi_byte1), feature_array1)
    cnt2 = getFeature(roi_byte2, len(roi_byte2), feature_array2)

    if cnt1 == 0 or cnt2 ==0:
        result = "feature extraction failed !"
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    score = getScore(feature_array1, cnt1, feature_array2, cnt2)
    if score >= 0.65:
        result = "Same Hand !"
        # print(f"\n 2 images are from the same hand\n similarity: {score}")
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    else:
        result = "Different Hand !"
        # print(f"\n 2 images are from the different hand\n similarity: {score}")
        response = jsonify({"result": result, "score": float(score)})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)