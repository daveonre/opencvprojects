import cv2 
 

def canny_edge_detection(frame): 
	# Convert the frame to grayscale for edge detection 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	
	# Apply Gaussian blur to reduce noise and smoothen edges 
	blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.5) 
	
	# Perform Canny edge detection 
	edges = cv2.Canny(blurred, 70, 135) 
	
	return blurred, edges


def main(): 
    # Open the default webcam  
    capturing = cv2.VideoCapture(0) 

    while True: 
        # Read a frame from the webcam 
        retreived, frame = capturing.read() 
        if not retreived: 
            print('Image not captured') 
            break
        
        # Perform Canny edge detection on the frame 
        blurred, edges = canny_edge_detection(frame)
        overlay = cv2.addWeighted(blurred, 0.5, edges, 0.5, 0)

        cv2.imshow("Blurred", blurred) 
        cv2.imshow("Edges", edges) 
        cv2.imshow("Overlay", overlay)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    capturing.release() 
    cv2.destroyAllWindows()


if __name__ == "__main__": 
    main()
