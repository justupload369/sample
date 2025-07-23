# PyTorch Setup and Examples
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

def main():
    print("=" * 50)
    print("PyTorch Setup Complete!")
    print("=" * 50)
    
    # Check PyTorch installation
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"Number of GPUs: {torch.cuda.device_count()}")
    else:
        print("Running on CPU")
    
    print("\n" + "=" * 50)
    print("Basic Tensor Operations")
    print("=" * 50)
    
    # Create tensors
    x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
    y = torch.tensor([2.0, 4.0, 6.0, 8.0, 10.0])
    
    print(f"Tensor x: {x}")
    print(f"Tensor y: {y}")
    print(f"x + y: {x + y}")
    print(f"x * y: {x * y}")
    print(f"x.mean(): {x.mean()}")
    
    # Matrix operations
    matrix_a = torch.randn(3, 4)
    matrix_b = torch.randn(4, 2)
    result = torch.mm(matrix_a, matrix_b)
    
    print(f"\nMatrix A shape: {matrix_a.shape}")
    print(f"Matrix B shape: {matrix_b.shape}")
    print(f"A @ B shape: {result.shape}")
    
    print("\n" + "=" * 50)
    print("Simple Neural Network Example")
    print("=" * 50)
    
    # Simple neural network
    class SimpleNet(nn.Module):
        def __init__(self):
            super(SimpleNet, self).__init__()
            self.fc1 = nn.Linear(2, 10)
            self.fc2 = nn.Linear(10, 1)
            self.relu = nn.ReLU()
            
        def forward(self, x):
            x = self.relu(self.fc1(x))
            x = self.fc2(x)
            return x
    
    # Create model
    model = SimpleNet()
    print(f"Model: {model}")
    
    # Sample data
    X = torch.randn(100, 2)
    y = (X[:, 0] + X[:, 1] > 0).float().unsqueeze(1)
    
    # Loss and optimizer
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    
    # Training loop
    print("\nTraining the model...")
    for epoch in range(10):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        
        if epoch % 2 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
    
    print("\nModel training completed!")
    
    # Test the model
    with torch.no_grad():
        test_input = torch.tensor([[1.0, 2.0], [-1.0, -2.0]])
        predictions = torch.sigmoid(model(test_input))
        print(f"\nTest predictions: {predictions.flatten()}")
    
    print("\n" + "=" * 50)
    print("PyTorch setup is complete and working!")
    print("=" * 50)

if __name__ == "__main__":
    main()
