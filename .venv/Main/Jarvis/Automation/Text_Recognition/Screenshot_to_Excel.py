import os
import re
import pytesseract
from PIL import Image
from openpyxl import Workbook

# Tesseract-OCR setup
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to WhatsApp Media folder
whatsapp_media_folder = r"C:\Path\to\WhatsApp\Media\WhatsApp Images"

# Initialize workbook
wb = Workbook()
ws = wb.active
ws.append(["Transaction ID", "Amount (Rs)", "Date", "Time", "File Name"])

def extract_payment_data(image_path):
    """Extract payment data (Transaction ID, Amount, Date, Time) from an image."""
    try:
        image = Image.open(image_path)
        raw_text = pytesseract.image_to_string(image)

        # Extract patterns
        transaction_id = re.search(r"Transaction ID[:\-]?\s*(\d+)", raw_text)
        amount = re.search(r"Paid Rs\.?\s*(\d+\.\d+)", raw_text)
        date = re.search(r"Date[:\-]?\s*([\d\w\s]+)", raw_text)
        time = re.search(r"Time[:\-]?\s*([\d:\s\w]+)", raw_text)

        return {
            "transaction_id": transaction_id.group(1) if transaction_id else "Not found",
            "amount": amount.group(1) if amount else "Not found",
            "date": date.group(1) if date else "Not found",
            "time": time.group(1) if time else "Not found",
        }
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

# Process images in the WhatsApp Media folder
for filename in os.listdir(whatsapp_media_folder):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        file_path = os.path.join(whatsapp_media_folder, filename)

        # Extract payment data
        payment_data = extract_payment_data(file_path)
        if payment_data and payment_data["transaction_id"] != "Not found":
            # Append data to Excel if it's a payment screenshot
            ws.append([
                payment_data["transaction_id"],
                payment_data["amount"],
                payment_data["date"],
                payment_data["time"],
                filename,
            ])

# Save the workbook
output_file = "WhatsApp_Payment_Data.xlsx"
wb.save(output_file)
print(f"Data saved to {output_file}")
