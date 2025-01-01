'''
This program will use BLIP through Hugging Face Transformers and generate captions for any image supplied to it
'''

#Installing Libraries
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

#Initialize Model from Hugging Face
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

#Load Image
image = Image.open("https://upload.wikimedia.org/wikipedia/commons/5/54/Taobat%2C_Neelum_Valley._Kashmir.jpg")

# Prepare the image
inputs = processor(image, return_tensors="pt")

# Generate captions
outputs = model.generate(**inputs)
caption = processor.decode(outputs[0],skip_special_tokens=True)

print("Generated Caption:", caption)

url = "https://colab.research.google.com/drive/1e2rWdwWh_t-g8vIbwaQM-m4S0gYM7JDb?usp=sharing"

print(f"View complete Colab Notebook at {url}")