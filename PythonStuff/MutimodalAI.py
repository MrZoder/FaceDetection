import cv2
import sys
import speech_recognition as sr


def face_recogntion():
    while True:
        # Path to the XML file containing the pre-trained model for face detection
        cascPath = "haarcascade_frontalface_default.xml"
        # Create an instance of CascadeClassifier using the XML file
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Initialize the video capture object using the default camera (0)
        video_capture = cv2.VideoCapture(1)

        # Start an infinite loop to continuously capture and process frames from the video stream
        while True:
            # Capture a single frame from the video stream
            ret, frame = video_capture.read()

            # Check if the frame was not successfully captured, and skip to the next iteration if so
            if not ret:
                continue

            # Convert the captured frame from BGR color space to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the grayscale frame using the CascadeClassifier object
            # Returns a list of rectangles representing the bounding boxes of the detected faces
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE,
            )

            # Iterate over the list of detected faces and draw rectangles around them on the original colored frame
            for x, y, w, h in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the current frame with the detected faces in a window titled "Video"
            cv2.imshow("Video", frame)

            # Wait for a key press and check if the pressed key is "q"
            # If so, exit the loop and stop the program
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        # Release the video capture object and destroy all OpenCV windows
        video_capture.release()
        cv2.destroyAllWindows()

        choice = input("Press q to quit, any other key to continue: ")
        if choice.lower() == "q":
            break


def voice_recogntion():
    while True:
        # Perform speech recognition
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Kindly voice out your command!")
            audio = r.listen(source)

        try:
            print("Interpreted as: " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Apologies, the audio wasn't clear enough.")
        except sr.RequestError as e:
            print("There was an issue retrieving results. Error: {0}".format(e))

        choice = input("Press q to quit, any other key to continue: ")
        if choice.lower() == "q":
            break


while True:
    print(
        "Welcome to the multiModal AI. What service would you like to use? \n 1. Face Detection \n 2. Voice Detection"
    )
    choice = int(input("Enter your choice: "))

    if choice == 1:
        face_recogntion()
    elif choice == 2:
        voice_recogntion()
    else:
        print("Invalid choice. Please try again.")
