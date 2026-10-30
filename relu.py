import torch
import torch.nn as nn
x = torch.tensor([-2.0, 0.0, 3.0])
m = nn.ReLU()
y = m(x)
print(x,y)