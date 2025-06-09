import pytesseract
from PIL import Image
import re
from pdf2image import convert_from_path  # Extract images from PDF
import numpy as np

# Function to extract images from PDF
def extract_images_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    return images  # Returns a list of PIL images

# Function to extract text from an image
def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

# Function to detect type of content (numbers, alphabets, words)
def extract_sequences(text):
    lines = text.split('\n')

    # Find the first line with meaningful content (ignoring instructions)
    for i, line in enumerate(lines):
        if re.search(r'\d{5,}', line) or re.search(r'^[A-Z](?: [A-Z])+$', line, re.I) or re.search(r'^\b[a-zA-Z]{3,}\b(?: \b[a-zA-Z]{3,}\b)+$', line):
            sequence_lines = lines[i:]  # Capture everything after instructions
            break
    else:
        return "", "unknown"

    # Extract sequences
    numbers = re.findall(r'\d+', ' '.join(sequence_lines))
    alphabets = re.findall(r'^[A-Z](?: [A-Z])+$', ' '.join(sequence_lines), re.I)
    words = re.findall(r'\b[a-zA-Z]{3,}\b(?: \b[a-zA-Z]{3,}\b)+', ' '.join(sequence_lines))

    # Determine the type of sequence
    if len(numbers) > 0 and len(numbers) > len(alphabets) and len(numbers) > len(words):
        return ' '.join(numbers), "numbers"
    elif len(alphabets) > 0 and len(alphabets) > len(words):
        return ' '.join(alphabets), "alphabets"
    elif len(words) > 0:
        return ' '.join(words), "words"
    else:
        return "", "unknown"

# Function to process a PDF containing images
def process_pdf(file_path):
        try:
            images = extract_images_from_pdf(file_path)  # Convert PDF pages to images
            all_text = ""

            for img in images:
                text = extract_text_from_image(img)  # Extract text from each image
                all_text += text + "\n"

            sequences, sequence_type = extract_sequences(all_text)

            if sequences:
                print(f"Extracted {sequence_type.capitalize()}:\n", sequences)
            else:
                print("No valid sequence found.")
        except Exception as e:
            print(f"Error processing PDF: {e}")

        
def extract_story_from_txt(file_path):
    """Extracts the story text from a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        story_text = file.read()
    return story_text.strip()

def printStoryArticle():
    # Ask for user age and fetch appropriate text
    child_txt_path = "/content/child.txt"  # Any path to text file
    adult_txt_path = "/content/Mohammed Shami has given a contrast.txt"  # Any path to text file

    age = int(input("Enter the age of the client: "))

    if age < 18:
     retrieved_text = extract_story_from_txt(child_txt_path)
    else:
     retrieved_text = extract_story_from_txt(adult_txt_path)

    print("\n--- Retrieved Text ---\n", retrieved_text)

def performExercise(n, path):
    sequence_exercises = [1, 2, 3, 5, 7, 8, 9, 10]
    if n in sequence_exercises:
        process_pdf(path)
    if n == 4:
        printStoryArticle()
    if n == 6:
        print("Sixth Exercise")

def main():
    exerciseNo = int(input("Enter the exercise number(1-12): "))
    path = input("Enter path to exercise pdf: ").strip()
    try:
        if path:
         performExercise(exerciseNo, path)
    except Exception as e:
            print(f"Error processing PDF: {e}")
        
 
# Run the function
main()
