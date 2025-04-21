import os
import sys
from pathlib import Path
import PIL.Image
from google import genai
from google.genai import types

# Get API key from environment variable
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY environment variable is not set.")
    print("Please set it using: export GEMINI_API_KEY='your_key_here' (Linux/Mac)")
    print("Or: set GEMINI_API_KEY=your_key_here (Windows)")
    sys.exit(1)

# Initialize the client with the API key from environment variable
client = genai.Client(api_key=api_key)

def generate_story():
    """Generate a story with images"""
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",
        contents=(
            "Generate a story about a cute baby turtle in a 3d digital art style. "
            "For each scene, generate an image."
        ),
        config=types.GenerateContentConfig(
            response_modalities=["Text", "Image"]
        ),
    )
    
    # Process and display the response
    for part in response.parts:
        if part.text:
            print(part.text)
        if hasattr(part, 'image') and part.image:
            # Save the image
            image_count = len(list(Path('.').glob('story_image_*.png')))
            output_path = f"story_image_{image_count + 1}.png"
            with open(output_path, 'wb') as f:
                f.write(part.image.data)
            print(f"Image saved to {output_path}")

def edit_image(image_path, edit_instruction):
    """Edit an existing image using Gemini 2.0 Flash"""
    try:
        # Open the image
        image = PIL.Image.open(image_path)
        
        # Convert the image to the format Gemini requires
        # This will vary based on the exact API requirements
        
        # Send the image with edit instructions to Gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=[
                {
                    "parts": [
                        {"image": {"mime_type": f"image/{image_path.split('.')[-1]}", "data": Path(image_path).read_bytes()}},
                        {"text": edit_instruction}
                    ]
                }
            ],
            config=types.GenerateContentConfig(
                response_modalities=["Text", "Image"]
            ),
        )
        
        # Save the edited image
        edited_image_path = f"edited_{Path(image_path).name}"
        
        # Process the response to get the edited image
        for part in response.parts:
            if hasattr(part, 'image') and part.image:
                with open(edited_image_path, 'wb') as f:
                    f.write(part.image.data)
                print(f"Edited image saved to {edited_image_path}")
            if part.text:
                print(f"Model response: {part.text}")
                
        return edited_image_path
    
    except Exception as e:
        print(f"Error editing image: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) < 2:
        print("Usage options:")
        print("1. Generate story: python script.py story")
        print("2. Edit image: python script.py edit <image_path> \"<edit instructions>\"")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "story":
        generate_story()
    elif command == "edit" and len(sys.argv) >= 4:
        image_path = sys.argv[2]
        edit_instruction = sys.argv[3]
        edit_image(image_path, edit_instruction)
    else:
        print("Invalid command or missing arguments.")
        print("Usage options:")
        print("1. Generate story: python script.py story")
        print("2. Edit image: python script.py edit <image_path> \"<edit instructions>\"")