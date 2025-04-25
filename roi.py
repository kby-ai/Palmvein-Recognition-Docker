import cv2
import numpy as np
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

roi_bad_pixel_number = 500  # the number of pixel where 3 values are zero in RGB channel on ROI image
roi_aspect_ratio_threshold = 100  # the passable aspect ratio threshold of ROI image
roi_size_threshold = 0.23
padding_size = 300 # the extra marine size of the frame inputted into Google Mediapipe Graph (this value must be a multiple of two)

def img_padding(img):
    h, w, _ = img.shape
    image = np.zeros((h + padding_size, w + padding_size, 3), np.uint8)
    image[int(padding_size / 2):-int(padding_size / 2), int(padding_size / 2):-int(padding_size / 2), :] = img
    return image

def img_crop(img_original, x2, x1, y2, y1, label):
    
    h, w, _ = img_original.shape
    img = np.zeros((h + 20, w + 20, 3), np.uint8)
    img[10:-10, 10:-10, :] = img_original
    if label == "Right":
        v1 = np.array([x2 * w, y2 * h])
        v2 = np.array([x1 * w, y1 * h])
    else:
        v2 = np.array([x2 * w, y2 * h])
        v1 = np.array([x1 * w, y1 * h])
    
    theta = np.arctan2((v2 - v1)[1], (v2 - v1)[0]) * 180 / np.pi
    R = cv2.getRotationMatrix2D(tuple([int(v2[0]), int(v2[1])]), theta, 1)
    
    v1 = (R[:, :2] @ v1 + R[:, -1]).astype(int)
    v2 = (R[:, :2] @ v2 + R[:, -1]).astype(int)
    img_r = cv2.warpAffine(img, R, (w, h))
    
    if 1:
        ux = int(v1[0] - (v2 - v1)[0] * 0.05)
        uy = int(v1[1] + (v2 - v1)[0] * 0.05)
        lx = int(v2[0] + (v2 - v1)[0] * 0.05)
        ly = int(v2[1] + (v2 - v1)[0] * 1)
    else:
        ux = int(v1[0] - (v2 - v1)[0] * 0.1)
        uy = int(v1[1] + (v2 - v1)[0] * 0.1)
        lx = int(v2[0] + (v2 - v1)[0] * 0.1)
        ly = int(v2[1] + (v2 - v1)[0] * 1.2)

    # delta_y is movement value in y ward
    delta_y = (ly - uy) * 0.15

    ly = int(ly - delta_y)
    uy = int(uy - delta_y)

    delta_x = (lx - ux) * 0.01
    lx = int(lx + delta_x)
    ux = int(ux + delta_x)
    
    if label == "Right":
        delta_x = (lx - ux) * 0.05
        lx = int(lx + delta_x)
        ux = int(ux + delta_x)
    # roi = img_r
    roi = img_r[uy:ly, ux:lx]
    if roi.shape[0] == 0 or roi.shape[1] == 0:
        print("error 1")
        return None, 3
    
    if abs(roi.shape[0] - roi.shape[1]) > roi_aspect_ratio_threshold:
        print("error 2", abs(roi.shape[0] - roi.shape[1]))
        return None, 4
    if roi.shape[1] / w < roi_size_threshold:
        print("error 3", roi.shape[1] / w)
        return None, 7
    
    n_zeros = np.count_nonzero(roi == 0)
    if n_zeros > roi_bad_pixel_number:
        print("error 4", n_zeros)
        return None, 5
    return roi, 0

def cupped_hand_filter(hand_landmarks):
    return hand_landmarks.landmark[12].y - hand_landmarks.landmark[11].y
         
def get_roi(path, hand_type, x1, y1, x2, y2):
    img = cv2.imread(path)
    
    if hand_type != 0:
        label = "Left"
    else:
        label = "Right"
    roi, _ = img_crop(img, x1, x2, y1, y2, label)
    return roi

def get_roi_image(img):

    label = "" 
    with mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=2,
            min_detection_confidence=0.5) as hands:
        # Read an image, flip it around y-axis for correct handedness output (see
        # above).
        if 1:            
            image = img_padding(img)
        else:
            image = cv2.flip(cv2.imread(file), 1)

        # Convert the BGR image to RGB before processing.
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Print handedness and draw hand landmarks on the image.
        if results.multi_handedness is not None:
            label = results.multi_handedness[0].classification[0].label
        
        if results.multi_hand_landmarks is None:
            return None, None

        image_height, image_width, _ = image.shape
        hand_landmarks = results.multi_hand_landmarks[0]
                    
        if cupped_hand_filter(hand_landmarks) > 0:
            return None, None
        else:                                
            roi, roi_msg_index = img_crop(image, hand_landmarks.landmark[5].x, hand_landmarks.landmark[17].x,
                                                hand_landmarks.landmark[5].y, hand_landmarks.landmark[17].y, label)
            
            return roi, label
