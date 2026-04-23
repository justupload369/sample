# PyTorch setup example
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

# Create a simple tensor
x = torch.tensor([1.0, 2.0, 3.0])
print("Sample tensor:", x)
