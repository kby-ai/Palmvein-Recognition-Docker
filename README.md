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
 
