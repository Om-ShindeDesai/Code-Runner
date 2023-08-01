import pillow
import cv2
import pytesseract

def extract_text_from_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract OCR to extract text from the grayscale image
    extracted_text = pytesseract.image_to_string(gray_image)

    return extracted_text

# Example usage:
image_path = 'final_solve.png'
extracted_text = extract_text_from_image(image_path)
print("Extracted text:", extracted_text)
