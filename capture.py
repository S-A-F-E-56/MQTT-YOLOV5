import cv2
import time
import os


def text_countdown(img, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, font_thickness=2, outline_thickness=3, text_color=(0, 0, 255), outline_color=(0, 0, 0)):
    # Draw the outline
    for offset in range(-outline_thickness, outline_thickness + 1):
        if offset != 0:
            cv2.putText(img, text, (position[0] + offset, position[1]), font, font_scale, outline_color, font_thickness, cv2.LINE_AA)
            cv2.putText(img, text, (position[0] - offset, position[1]), font, font_scale, outline_color, font_thickness, cv2.LINE_AA)
            cv2.putText(img, text, (position[0], position[1] + offset), font, font_scale, outline_color, font_thickness, cv2.LINE_AA)
            cv2.putText(img, text, (position[0], position[1] - offset), font, font_scale, outline_color, font_thickness, cv2.LINE_AA)
    
    # Draw the text
    cv2.putText(img, text, position, font, font_scale, text_color, font_thickness, cv2.LINE_AA)

def take_photo(filename=''): 
    
    cap = cv2.VideoCapture(0) # Open a connection to the webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    countdown_start_time = time.time()
    countdown_duration = 5

    while True:
        ret, frame = cap.read() # Capture frame-by-frame

        if not ret:
            print("Error: Failed to capture image")
            break

        elapsed_time = time.time() - countdown_start_time # Calculate the elapsed time
        remaining_time = max(0, countdown_duration - int(elapsed_time))

        countdown_text = str(remaining_time) # Prepare text for countdown
        text_position = (frame.shape[1] // 2 - 30, 50)  # Centered horizontally, 50 pixels from the top

        if remaining_time > 0:
            text_countdown(frame, countdown_text, text_position, font_scale=2, font_thickness=2, outline_thickness=3) # Draw countdown text with outline
        
        cv2.imshow('Siapkan pose Anda', frame) # Show the frame with countdown

        if elapsed_time >= countdown_duration:
            break

        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()
    
    # Save the image
    folder_path = 'MQTT-YOLOV5/images'
    full_file_path = os.path.join(folder_path, filename)
    cv2.imwrite(full_file_path, frame)


    return filename

filename = take_photo('photo.jpg') # (photo) bisa diganti dengan ID atau nama pengguna

