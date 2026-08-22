# AI Energy Analyzer

A GPU-free AI workload and GPU power simulation platform.

## Features

- AI message workload estimation
- Simulated GPU power
- Real-time power graph
- Time-based x-axis
- Peak GPU power
- Average GPU power
- Energy consumption
- Processing time
- LinkedIn-ready sharing text

## Important

This MVP does NOT measure physical GPU power.

All GPU power values are simulated.

## Installation

Create a virtual environment:

python -m venv .venv

Activate it.

### Windows

.venv\Scripts\activate

### macOS/Linux

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run:

uvicorn app:app --reload

Open:

http://127.0.0.1:8000

## Future versions

The simulator can later be connected to:

- Qwen
- Llama
- Mistral
- vLLM
- NVIDIA NVML
- NVIDIA DCGM
- Real GPU measurements