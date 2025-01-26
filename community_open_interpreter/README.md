# AI Development Environment Setup Guide

A comprehensive guide for setting up an AI development environment using Ubuntu VM with both local and remote API options.

## 1. Ubuntu Virtual Machine Setup

### Prerequisites
- UTM for macOS ([Download](https://mac.getutm.app/))
- Ubuntu Server ISO
- Minimum 4GB RAM
- At least 2 CPU cores
- 20GB+ storage space

### Installation Steps

1. Install UTM on macOS
   ```bash
   # You can install via Homebrew
   brew install --cask utm
   ```

2. Download Ubuntu 24 ARM
    ```bash
    wget https://cdimage.ubuntu.com/daily-live/current/oracular-desktop-arm64.iso
    ```
    
## 2. Install Dependencies

### Basic Dependencies

```bash
# Update OS
sudo apt update -y
```

```bash
# Install Python and development tools
sudo apt install python3 python3-pip python3-dev build-essential curl wget git -y
```

### Python Packages
```bash
# Upgrade pip
python3 -m pip install --upgrade pip

# Install community open-interpreter
pip3 install open-interpreter
```

## 3. Running with Local API (Ollama)

### Install Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Start Ollama Service
```bash
systemctl start ollama
```

### Pull and Run Models
```bash
# Pull Mistral model
ollama pull mistral

# Verify installation
curl http://localhost:11434/api/version
```

### Example Usage

1. Basic API Call
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "What is machine learning?"
}'
```

2. Basic Usage (ollama > your_model)
```bash
interpreter --local
```

## 4. Running with Remote API (Claude)

### Setup Anthropic API
```bash
# Set API key
export ANTHROPIC_API_KEY='your-api-key-here'

# Add to bashrc for persistence
echo 'export ANTHROPIC_API_KEY=your-api-key-here' >> ~/.bashrc
source ~/.bashrc
```

### Run Open Interpreter

1. Basic Usage
```bash
interpreter --model claude-3-5-sonnet-20241022
```

2. Auto-confirm Mode
```bash
interpreter -y
```

## Additional Resources

- [UTM Documentation](https://docs.getutm.app/)
- [Ollama Documentation](https://ollama.com/docs)
- [Claude API Documentation](https://docs.anthropic.com/)
- [Open Interpreter Documentation](https://github.com/KillianLucas/open-interpreter)