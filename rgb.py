import  cv2
import numpy  as np

# taking the input 

capture = cv2.VideoCapture(0)

# using while loop since we perform frame by frame

while True:
    _,frame = capture.read()

    cv2.imshow('Vid',frame)

    cv2.waitKey(1)

    # setting the values of the base colors we want to focus 

    b = frame[:, :, 0]  # Blue channel
    g = frame[:, :, 1]  # Green channel
    r = frame[:, :, 2]  # Red channel
    
    # computing the mean for 
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)
     
    #displaying the dominant color 
    if b_mean > g_mean and b_mean > r_mean:
        print("Blue")
    elif g_mean > r_mean and g_mean > b_mean:
        print("Green")
    else:
        print("Red")

    # breaking the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()



    






