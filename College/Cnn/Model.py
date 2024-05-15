# Define the CNN model
from torch import nn
from torch import flatten

class CNN(nn.Module):
    def __init__(self, num_channels=3, num_classes=12):
        super(CNN, self).__init__()
        
        self.conv1 = nn.Conv2d(in_channels=num_channels,out_channels=64, kernel_size=(3,3))
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=(2,2), stride=(2,2))
        
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=32, kernel_size=(5,5))
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=(2,2), stride=(2,2))
        
        self.fc1 = nn.Linear(in_features=39200,out_features=128)
        
        self.relu3 = nn.ReLU()
        
        self.fc2 = nn.Linear(in_features=128, out_features=num_classes)
        
        self.logsoftmax = nn.LogSoftmax(dim=1) # comment for loss = nn.CrossEntropyLoss()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)

        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pool2(x)

        x = flatten(x,1)
        
        x = self.fc1(x)
        x = self.relu3(x)
        x = self.fc2(x)
        
        out = self.logsoftmax(x)
        return out
