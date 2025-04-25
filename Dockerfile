FROM openvino/ubuntu20_runtime:2024.5.0

USER root
RUN rm -rf /var/lib/apt/lists/* && apt update && apt install -y unzip \
    libjpeg8 \
    libwebp6 \
    libpng16-16 \
    libtbb2 \
    libtiff5 \
    libtbb-dev \
    libopenexr-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libgomp1

# Set up working directory
RUN mkdir -p /home/openvino/kby-ai-palmvein
WORKDIR /home/openvino/kby-ai-palmvein

# Copy shared libraries and application files
COPY ./libopencv.zip .
RUN unzip libopencv.zip
RUN cp -f libopencv/* /usr/local/lib/ 
RUN ldconfig

# Copy Python and application files
COPY ./model ./model
COPY ./libvein.so .
COPY ./app.py .
COPY ./roi.py .
COPY ./veinsdk.py .
COPY ./requirements.txt .
COPY ./run.sh .
COPY ./license.txt .
COPY ./ncnn.zip .
RUN unzip ncnn.zip

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set up entrypoint
CMD ["bash", "./run.sh"]

# Expose ports
EXPOSE 8080 9000
