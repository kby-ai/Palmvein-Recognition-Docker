<p align="center">
  <a href="https://play.google.com/store/apps/dev?id=7086930298279250852" target="_blank">
    <img alt="" src="https://github-production-user-asset-6210df.s3.amazonaws.com/125717930/246971879-8ce757c3-90dc-438d-807f-3f3d29ddc064.png" width=500/>
  </a>  
</p>

### Our facial recognition algorithm is globally top-ranked by NIST in the FRVT 1:1 leaderboards. <span><img src="https://github.com/kby-ai/.github/assets/125717930/bcf351c5-8b7a-496e-a8f9-c236eb8ad59e" alt="badge" width="36" height="20"></span>  
[Latest NIST FRVT evaluation report 2024-12-20](https://pages.nist.gov/frvt/html/frvt11.html)  

![FRVT Sheet](https://github.com/user-attachments/assets/16b4cee2-3a91-453f-94e0-9e81262393d7)

#### 🆔 ID Document Liveness Detection - Linux - [Here](https://web.kby-ai.com)  <span><img src="https://github.com/kby-ai/.github/assets/125717930/bcf351c5-8b7a-496e-a8f9-c236eb8ad59e" alt="badge" width="36" height="20"></span>
#### 🤗 Hugging Face - [Here](https://huggingface.co/kby-ai)
#### 📚 Product & Resources - [Here](https://github.com/kby-ai/Product)
#### 🛟 Help Center - [Here](https://docs.kby-ai.com)
#### 💼 KYC Verification Demo - [Here](https://github.com/kby-ai/KYC-Verification-Demo-Android)
#### 🙋‍♀️ Docker Hub - [Here](https://hub.docker.com/r/kbyai/palmvein-recognition)
```bash
sudo docker pull kbyai/palmvein-recognition:latest
sudo docker run -v ./license.txt:/home/openvino/kby-ai-palmvein/license.txt -p 8081:8080 -p 9001:9000 kbyai/palmvein-recognition:latest
```

# Palmvein-Recognition-Docker
## Overview
This repository demonstrates an efficient and accurate `palmvein` recognition technology by implementing palm-vein comparison based on palmvein feature extraction and face matching algorithm, which was implemented via a `Dockerized Flask API`.<br/>
It includes features that allow for testing `plamvein` recognition between two images using both image files and `base64-encoded` images.

> In this repo, we integrated `KBY-AI`'s palmvein recognition solution into `Linux Server SDK` by wrapping with docker image.<br/>
> We can customize the SDK to align with customer's specific requirements.

### ◾PalmRecognitionSDK Product List
  | No.      | Repository | SDK Details | Status |
  |------------------|------------------|------------------|------------------|
  | 1        | [Palmprint Recognition - Linux](https://github.com/kby-ai/Palmprint-Recognition-Linux)    | Palmprint Comparison Linux SDK | Available |
  | 2        | [Palmprint Recognition - Docker](https://hub.docker.com/r/kbyai/palmprint-recognition)    | Palmprint Comparison Docker Image | Available |
  | ➡️        | <b>[Palmvein Recognition - Linux](https://github.com/kby-ai/Palmvein-Recognition-Docker)</b>    | <b>Palmvein Comparison Linux SDK</b> | <b>Available</b> |
  | 4        | [Palmprint Recognition - Android](https://github.com/kby-ai/Palmprint-Recognition-Android)    | Palmprint Comparison Android SDK | Available |

> To get more products, please visit products [here](https://github.com/kby-ai):<br/>

## Try the API
### Online Demo
  This `SDK` can be tested on online test demo page [here](https://web.kby-ai.com):
  
  ![image](https://github.com/user-attachments/assets/4e660694-f5bf-4f00-be2b-822c093e2d94)
  
### Postman
  The `API` can be evaluated through `Postman` tool. Here are the endpoints for testing:
  - Test with an image file: Send a `POST` request to `http://127.0.0.1:8081/palmvein`.
  - Test with a `base64-encoded` image: Send a `POST` request to `http://127.0.0.1:8081/palmvein_base64`.
    ![image](https://github.com/user-attachments/assets/dfaf0151-db84-4330-bffc-8c5a41d66fa3)
    
## SDK License

This project demonstrates `KBY-AI`'s `Palmvein Recognition Server SDK`, which requires a license per machine.
- The code below shows how to use the license: https://github.com/kby-ai/Palmvein-Recognition-Docker/blob/c92c8d923c51591d869773f81a2af30dc309667e/app.py#L17-L29
- To request the license, please provide us with the `machine code` obtained from the `getMachineCode` function.

#### Please contact us:</br>
🧙`Email:` contact@kby-ai.com</br>
🧙`Telegram:` [@kbyai](https://t.me/kbyai)</br>
🧙`WhatsApp:` [+19092802609](https://wa.me/+19092802609)</br>
🧙`Discord:` [KBY-AI](https://discord.gg/CgHtWQ3k9T)</br>
🧙`Teams:` [KBY-AI](https://teams.live.com/l/invite/FBAYGB1-IlXkuQM3AY)</br>
 
### 1. System Requirements
  - `CPU`: 2 cores or more (Recommended: 2 cores)
  - `RAM`: 4 GB or more (Recommended: 8 GB)
  - `HDD`: 4 GB or more (Recommended: 8 GB)
  - `OS`: `Ubuntu 20.04` or later
  - Dependency: `ncnn` (Version: 2024.12.26)
    
### 2. Setup and Test
  - Clone the project:
    ```bash
    git clone https://github.com/kby-ai/Palmvein-Recognition-Docker.git
    ```
    ```bash
    cd Palmvein-Recognition-Docker
    ```
  - Build the `Docker` image:
    ```bash
    sudo docker build --pull --rm -f Dockerfile -t kby-ai-palmvein:latest .
    ```
  - Read `machine code`
    ```
    sudo docker run -e LICENSE="xxxxx" kby-ai-palmvein:latest
    ```
  - Send us `machine code` obtained.
    ![image](https://github.com/user-attachments/assets/3c84f49a-1a8a-4b4e-832b-a4e23b46d357)
  - Update the `license.txt` file by overwriting the `license key` that you received from `KBY-AI` team.
  - Run the `Docker` container:
    ```bash
    sudo docker run -v ./license.txt:/home/openvino/kby-ai-palmvein/license.txt -p 8081:8080 -p 9001:9000 kbyai/palmvein-recognition:latest
    ```
    ![image](https://github.com/user-attachments/assets/008fcf4d-8cf6-4e16-890b-e69d36d3d324)
  - Here are the endpoints to test the `API` through `Postman`:
    Test with an image file: Send a `POST` request to `http://{xx.xx.xx.xx}:8081/palmvein`.</br>
    Test with a `base64-encoded` image: Send a `POST` request to `http://{xx.xx.xx.xx}:8081/palmvein`.</br>

### 3. Execute the Gradio demo
  - Setup `Gradio`
    Ensure that the necessary dependencies are installed. </br>
    `Gradio` requires `Python 3.6` or above. </br>
    Install `Gradio` using `pip` by running the following command:
    ```bash
    pip install gradio
    ```
  - Run the demo with the following command:
    ```bash
    cd gradio
    python demo.py
    ```
  - `SDK` can be tested on the following URL: `http://127.0.0.1:9000`

## About SDK

### 1. Initializing the SDK

- Import SDK python package
  ```python
  import handtool
  ```
- Create new object for using `SDK` 
  ```python
  config = handtool.EncoderConfig()
  encoder = handtool.create_encoder(config)  
  ```
- Obtain the `machine code` to activate and request a license
  ```python
  machineCode = encoder.getMachineCode()
  print("\nmachineCode: ", machineCode.decode('utf-8'))
  ```
- Activate the `SDK` using the license key
  ```python
  ret = encoder.setActivation(license.encode('utf-8'))
  print("\nactivation: ", ret)
  ```  
  Once `ret` value is zero, SDK can get work started

### 2. APIs
  - Hand Detection
  
    The `SDK` provides a single API for detecting hands, determining `hand landmark`.</br>
    The function can be used as follows:
    ```python
    hand_type, x1, y1, x2, y2, detect_state = encoder.detect_using_bytes(img)
    roi = mat_to_bytes(get_roi(img, hand_type, x1, y1, x2, y2))
    ```
    * `hand_type`: it indicates hand type value, `0` value: `left hand`, `1` value: `right hand`.
    * `x1`, `y1`, `x2`, `y2`: hand landmark points to get `ROI` image.
    * `roi`: hand `ROI(Region Of Interest)` image to get palm feature.
  - Create Feature
    `encode_using_bytes` function returns palmprint feature against `ROI` data.</br>
    ```python    
    palmprint = encoder.encode_using_bytes(roi)
    ```
    * `roi`: hand `ROI(Region Of Interest)` image to get palm feature.
    * `palmprint`: palmprint feature calculated from hand `ROI` data.    
  - Similiarity
    The `compare_to` function takes two palmprint `feature`s as a parameter and returns `score` value to determine whether 2 input hands are from the same or different.
    ```python
    one_palmprint_code = encoder.encode_using_bytes(roi1)
    another_palmprint_code = encoder.encode_using_bytes(roi2)
    score = one_palmprint_code.compare_to(another_palmprint_code)
    ```

### 3. Threshold
  The threshold is `0.15` as a default.
  https://github.com/kby-ai/Palmprint-Recognition-Docker/blob/ddf1f039c55534d7189fda162b5c4df844131b72/app.py#L12-L13

