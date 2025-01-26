# PyTorch
PyTorch is a popular open-source machine learning framework that provides a flexible ecosystem of tools, libraries, and community-contributed code modules. It is widely used for:

Building custom AI models.
Training models on datasets.
Performing inference (making predictions) using pre-trained models or custom models.
Running experiments and visualizations.
Utilizing GPUs and TPUs for accelerated computation.
PyTorch supports both static and dynamic computational graphs, making it versatile for various use cases. It is highly customizable and can be used in research, production, and academic settings.

## Prerequisites
- macOS 13.0+
- M2 Max chip (also works with M1/M3)
- Python 3.11+ (recommended)
- 16GB+ RAM recommended

## Installation Steps

### 1. Install Python and Virtual Environment

# Install Python 3.11
```bash
brew install python@3.11
```

# Create virtual environment
```bash
python3 -m venv deepseek-env
source deepseek-env/bin/activate
```

### 2. Install PyTorch with MPS Support
```bash
pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
```

### 3. Install Python Additional Dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Download Model Weights

### 1. Install LFS (managing large repository files)
```bash
brew install git-lfs
```

### 2. LFS init
```bash
git lfs install
```

### 3. Clone Model DeepSeek-LLM-7B-Chat (25.7GB)
Get size before download
```bash
curl -s https://huggingface.co/api/models/deepseek-ai/deepseek-llm-7b-chat | jq .usedStorage | xargs -I {} echo "scale=2; {} / (1024^3)" | bc
```

Make dir
```bash
mkdir modules && cd modules
```

Clone
```bash
git clone https://huggingface.co/deepseek-ai/deepseek-llm-7b-chat .
```

### 4. Monitor traffic to verify model download (in separate terminal)
```bash
brew install nload && nload devices en0
```

```
models/
├── config.json
├── generation_config.json
├── pytorch_model-00001-of-00002.bin
├── pytorch_model-00002-of-00002.bin
├── pytorch_model.bin.index.json
├── special_tokens_map.json
├── tokenizer.json
└── tokenizer_config.json
```

### 5. Create Gradio UI Interface (app.py has been already set up)

### 6. Run the Application
```bash
python3 app.py
```

[Broswer](http://localhost:7860)

### 7. Remove Python Environment
```bash
deactivate
rm -rf deepseek-env
```