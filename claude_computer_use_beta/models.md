# Claude 3 Models Quick Guide

## Model Types

### Claude 3 Family
- **Claude 3 Haiku**: Fastest response time
- **Claude 3 Opus**: Best for complex tasks
- **Claude 3.5 Sonnet**: Most intelligent [Released October 22, 2024]

## Temperature Settings

- **0 (Minimum)**
  - Most deterministic
  - Chooses most likely tokens
  - Best for accuracy and factual outputs
  
- **1 (Medium)**
  - Balanced randomness
  - Considers both likely and less likely options
  - Good for general use
  
- **>1 (High)**
  - More creative and random
  - Takes chances on less probable tokens
  - Can be less coherent

## Token Management
- Controls input tokens (text you send)
- Controls output tokens (text you receive)
- Temperature doesn't affect computation cost
- Same cost regardless of temperature setting (0 or 1)

## Getting Started

1. Generate API Key:
   - Visit https://console.anthropic.com/settings/keys

2. Access Workbench:
   - Visit https://console.anthropic.com/workbench

3. Test and Experiment:
   - Use Workbench to try different settings
   - Monitor outputs and performance
   - Adjust parameters as needed