import torch
import torch.nn as nn
from torch.utils.data import Dataset

class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, hidden_size_2, output_size):
        super(MLP, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(in_features = input_size, out_features = 1500),
            nn.Sigmoid(),
            nn.Linear(in_features = 1500, out_features = 512),
            nn.Sigmoid(),
            nn.Linear(in_features = 512, out_features = 256),
            nn.Sigmoid(),
            nn.Linear(in_features = 256, out_features = 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        out = self.layers(x)
        return out

