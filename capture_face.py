import cv2
import face_recognition

# Function to capture and save a face
def capture_and_save_face(name):
    # Open the default camera (camera index 0)
    cap = cv2.VideoCapture(0)

    # Check if the camera is successfully opened
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # If there's an issue reading the frame, break the loop
        if not ret:
            print("Error: Could not read frame.")
            break

        # Find faces in the frame
        face_locations = face_recognition.face_locations(frame)

        # If a face is found, save it and exit the loop
        if face_locations:
            face_image = frame[face_locations[0][0]:face_locations[0][2], face_locations[0][3]:face_locations[0][1]]
            cv2.imwrite(f"images/{name}.jpg", face_image)
            break

        # Display the frame
        cv2.imshow('Capture Face', frame)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

# Provide your name when calling the function
the_name = input("What your name? ")
capture_and_save_face(the_name)

