# Gemini 2.0 Flash Photo Editor

## Installation and Setup

1. Install required packages:
```bash
pip3 install -r requirements.txt
```

2. Set up your Google AI Studio account:
   * Visit Google AI Studio
   * Create an account or sign in
   * Navigate to the API section and generate an API key

3. Set your API key as an environment variable:
```bash
# For Linux/Mac
export GEMINI_API_KEY="your_api_key_here"

# For Windows
set GEMINI_API_KEY=your_api_key_here
```

Alternatively, you can create a .env file in the project directory:
```
GEMINI_API_KEY=your_api_key_here
```

And modify the script to use python-dotenv:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Usage

### Generate an Illustrated Story
```bash
python3 main.py story
```

### Edit an Image
```bash
python3 main.py edit path/to/your/image.jpg "Your editing instructions here"
```