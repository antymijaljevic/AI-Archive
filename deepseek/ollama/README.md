# Ollama: Simplifying PyTorch Model Deployment on Edge Devices

## Overview

Ollama is an open-source platform designed to streamline the deployment of PyTorch models on edge devices such as smartphones and wearables. It leverages optimized frameworks like ollama-cpu and ollama-openvino (assuming "openvite" was a typo) to enhance performance on low-power hardware, making it ideal for real-time applications where inference speed is crucial.

## Key Features

1. **PyTorch-Compatible Frameworks**: Ollama supports PyTorch models, ensuring compatibility with the widely-used machine learning framework.
2. **Edge-Accelerated Inference**: Optimized for resource-constrained environments, Ollama ensures fast and efficient model inference on edge devices.
3. **Integration with Python**: Seamlessly integrates into Python-based workflows, enabling smooth integration with existing pipelines.

## Getting Started

### 1. Downloading Ollama

To begin, download Ollama from the official website:

[Download Ollama](https://ollama.com/download)

Follow the installation instructions provided for your operating system. Ensure you review the system requirements to confirm compatibility with your hardware.

### 2. Accessing Models via OllamaHub

Ollama provides a repository of pre-trained models known as OllamaHub. You can access different versions of the DeepSeek-R1 model, which likely refers to optimized versions of the GPT model:

- **1.5B Parameters**: Suitable for lighter applications.
- **8B Parameters**: Offers better performance with moderate resource usage.
- **14B Parameters**: Strikes a balance between accuracy and computational demands.
- **32B Parameters**: Delivers high accuracy but requires more powerful hardware.
- **70B Parameters**: The most powerful option, ideal for complex tasks.

To download these models, use the following commands in your terminal:

```bash
# For example, to download the 1.5B version:
ollama run deepseek-r1:1.5b

# And for the largest model:
ollama run deepseek-r1:70b
```

### 3. Setting Up GUI Chat with Chatbox

For an interactive chat experience, integrate Ollama with Chatbox:

[Chatbox AI](https://chatboxai.app/en)

#### Steps:

1. Open Chatbox and navigate to settings.
2. Under the model section, select Ollama as the API host.
3. Configure the API host to `http://127.0.0.1:11434`, which is the default port for Ollama.
4. Choose a DeepSeek model from the available options.
5. Save your settings to enable chatting with the deployed model.