# PyTorch Project Setup

This project has PyTorch successfully installed and configured.

## Installation Details

- **PyTorch Version**: 2.7.1
- **TorchVision Version**: 0.22.1
- **TorchAudio Version**: 2.7.1
- **Python Version**: 3.13.2

## Files

- `main.py` - Basic PyTorch test script
- `pytorch_example.py` - Comprehensive PyTorch example with neural network
- `requirements.txt` - Python dependencies

## Running the Examples

To run the basic test:
```bash
python main.py
```

To run the comprehensive example:
```bash
python pytorch_example.py
```

## Features Demonstrated

1. **Basic Tensor Operations**
   - Creating tensors
   - Mathematical operations
   - Matrix multiplication

2. **Neural Network**
   - Simple feedforward network
   - Training loop
   - Loss computation
   - Model evaluation

3. **System Information**
   - PyTorch version check
   - CUDA availability check
   - Device information

## GPU Support

Currently installed with CPU support. To install with CUDA support (if you have an NVIDIA GPU), you can install the CUDA version:

```bash
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## Next Steps

You can now:
1. Build neural networks using `torch.nn`
2. Use automatic differentiation with `torch.autograd`
3. Load and preprocess data with `torch.utils.data`
4. Train models on GPU (if CUDA version is installed)
5. Use pre-trained models from `torchvision.models`
