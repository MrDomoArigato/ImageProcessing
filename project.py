def open_image():
    file=easygui.fileopenbox()
    image= cv2.imread(file)
    
    return(image)
    
def convert_hsv(image):
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return(image_hsv)

def convert_gray(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return(image_gray)

def convert_lab(image):
    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    return(image_lab)

def equalize_hist(image):
    image_enhanced = cv2.equalizeHist(image)
    return(image_enhanced)
    
def sharpen_kernel(image):
    kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return (sharpened_image)