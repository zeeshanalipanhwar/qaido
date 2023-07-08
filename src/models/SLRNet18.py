from collections import OrderedDict

import torchvision
from torch import nn

class SLRNet18(nn.Module):
    def __init__(self, target_classes):
        super(SLRNet18, self).__init__()
        self.model = torchvision.models.resnet18(pretrained=True)

        fc = nn.Linear(512, target_classes)
        fc.requires_grad = True
        
        self.model.fc = fc
        
    def forward(self, images):
      return self.model(images)
