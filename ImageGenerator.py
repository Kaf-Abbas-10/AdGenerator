import requests
import os
from PIL import Image
from io import BytesIO

def generate_image_pollinations(prompt, output_path="generated_ad.jpg"):
    url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}"
    
    try:
        print("Generating image...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Save image
        img = Image.open(BytesIO(response.content))
        img.save(output_path)
        print(f"Image saved to: {output_path}")
        return output_path
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def generate_image_stability(prompt, output_path="generated_ad.jpg"):
    API_KEY = "HUGGING_FACE_API_KEY"
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    try:
        print("Generating image...")
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        response.raise_for_status()
        
        img = Image.open(BytesIO(response.content))
        img.save(output_path)
        print(f"Image saved to: {output_path}")
        return output_path
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

if __name__ == "__main__":
    try:
        with open("generated_prompt.txt", "r") as f:
            prompt = f.read().strip()
        print("Using prompt from file:")
        print(prompt)
    except FileNotFoundError:
        prompt = "A serene morning scene with a steaming cup of organic green tea on a wooden table, surrounded by fresh tea leaves and herbs, soft natural lighting, photorealistic style, warm and inviting atmosphere, advertisement quality"
        print("Using default prompt:")
        print(prompt)
    
    print("\n" + "="*50)
    
    # Generate image using free API (Pollinations.ai - no API key needed)
    generate_image_pollinations(prompt)
    
    # Uncomment below to use Hugging Face instead (requires free API key)
    # generate_image_stability(prompt)