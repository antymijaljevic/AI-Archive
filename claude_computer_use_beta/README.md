# Claude Computer Use Demo

This repository contains a Docker-based demo for Claude's computer use capabilities, allowing Claude to interact with a virtual desktop environment.

## Prerequisites

- Docker installed on your system ([Get Docker](https://docs.docker.com/get-docker/))
- An Anthropic API key ([Get one here](https://console.anthropic.com/))
- At least 4GB of available RAM
- A modern web browser

## Quick Start

1. Set your Anthropic API key as an environment variable:

On Unix or MacOS:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

2. Run the Docker container:
```bash
docker run \
    -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

3. Access the demo:
- Open your web browser and navigate to: `http://localhost:8080`

## Port Mappings

The container exposes several ports:
- `8080`: Main web interface
- `5900`: VNC server
- `6080`: noVNC web client
- `8501`: Streamlit interface (if available)

## Container Details

The Docker container includes:
- A virtual desktop environment
- Pre-installed applications for Claude to interact with
- The necessary Python environment and dependencies
- A web-based interface for interaction

## Additional Resources

- [Claude Computer Use Documentation](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
- [Anthropic API Documentation](https://docs.anthropic.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Claude Computer Use GitHub Repository](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)