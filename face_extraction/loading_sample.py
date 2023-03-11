from iresnet import  iresnet50
import torch

weight = torch.load("res50.pth")
model = iresnet50()
model.load_state_dict(weight)