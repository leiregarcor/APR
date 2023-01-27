# -*- coding: utf-8 -*-
"""mlp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/apr-upv/apr2223/blob/master/mlp.ipynb
"""

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

training_data = datasets.FashionMNIST(root="data", train=True,
    download=True, transform=ToTensor())
test_data = datasets.FashionMNIST(root="data", train=False,
    download=True, transform=ToTensor())

torch.manual_seed(23)
train_dataloader = DataLoader(training_data, batch_size=64,
  shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64,
  shuffle=True)

class NeuralNetwork(nn.Module):
  def __init__(self, input_size, layers: list, num_classes):
    super(NeuralNetwork, self).__init__()
    self.flatten = nn.Flatten()
    self.layers = nn.ModuleList()
    self.input_size = input_size
    for output_size, activation_function in layers:
      self.layers.append(nn.Linear(input_size, output_size))
      input_size = output_size
      self.layers.append(activation_function)
    self.layers.append(nn.Linear(input_size, num_classes))
  def forward(self, x):
    x = self.flatten(x)
    for layer in self.layers:
      x = layer(x)
    return x

torch.manual_seed(23)
C = 10
N,H,W = training_data.data.shape; D = H*W
for neuronas in [64,128,256,512,1024,2048]:
  M1= neuronas
  model = NeuralNetwork(D, [(M1, nn.ReLU())], C)

  def train_loop(dataloader, model, loss_fn, optimizer):
      size = len(dataloader.dataset)
      for batch, (X, y) in enumerate(dataloader):
          pred = model(X); loss = loss_fn(pred, y)
          optimizer.zero_grad(); loss.backward(); optimizer.step() # backprop
          if batch % 100 == 0:
              loss, current = loss.item(), batch * len(X)
              #print(f"trloss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

  def test_loop(dataloader, model, loss_fn):
      size = len(dataloader.dataset); nbatches = len(dataloader)
      teloss, correct = 0, 0
      with torch.no_grad():
          for X, y in dataloader:
              pred = model(X); teloss += loss_fn(pred, y).item()
              correct += (pred.argmax(1) == y).type(torch.float).sum().item()
      teloss /= nbatches; correct /= size
      #print(f"teacc: {(100*correct):>0.1f}%, teloss: {teloss:>8f} \n")
      return 1-correct

  learning_rate = 1e-3
  loss_fn = nn.CrossEntropyLoss()
  optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
  epochs = 30
  for t in range(epochs):
      #print(f"Epoch {t+1}\n-------------------------------")
      train_loop(train_dataloader, model, loss_fn, optimizer)
      err=test_loop(test_dataloader, model, loss_fn)
      if(t==30-1):
        print(f"{M1} {err*100:4.1f}")
#print("Done!")
