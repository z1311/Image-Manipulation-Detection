#importing libs

import torch.nn as nn



# auth -> 1 and tp -> 0
class IMDModel(nn.Module):

    def __init__(self):
        super(IMDModel,self).__init__()

        self.maxpool = nn.MaxPool2d(kernel_size=2)
        self.relu = nn.ReLU()
        self.down_conv1 = nn.Sequential(
                        nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3),
                        nn.BatchNorm2d(64),
                        self.maxpool,
                        self.relu
        )
        self.down_conv2 = nn.Sequential(
                        nn.Conv2d(in_channels=64, out_channels=16, kernel_size=3),
                        nn.BatchNorm2d(16),
                        self.maxpool,
                        self.relu
        )
        self.linear = nn.Sequential(
                        nn.Linear(in_features=16*30*30, out_features=1024),
                        nn.BatchNorm1d(1024),
                        self.relu,
                        nn.Linear(in_features=1024, out_features=64),
                        nn.BatchNorm1d(64),
                        self.relu,
                        nn.Linear(in_features=64, out_features=2),
                        nn.Softmax()
        )


    def forward(self, img):

        d1 = self.down_conv1(img)
        d2 = self.down_conv2(d1)

        d2 = d2.view(-1, d2.shape[1]*d2.shape[2]*d2.shape[3])
        out = self.linear(d2)
        
        return out