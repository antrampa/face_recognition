import os
import face_recognition
import cv2

# Load known faces and names
known_face_encodings = []
known_face_names = []

# Function to load and append a face
def load_face(name, file_path):
    image = face_recognition.load_image_file(file_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(name)

# Folder containing face images
folder_path = "images"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        # Extract the name from the filename (assuming the format "Name.jpg")
        name = os.path.splitext(filename)[0]
        file_path = os.path.join(folder_path, filename)
        
        # Load the face into the known_face_encodings and known_face_names lists
        load_face(name, file_path)

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Find faces in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"  # Default name if no match is found

        # If a match is found, use the name of the matched face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a rectangle around the face and display the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

