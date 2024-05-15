import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import random_split
from torch.utils.data.dataloader import DataLoader



from tqdm import tqdm
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import time


from Model import CNN
from train import train


data_dir = './/Flowers'
BATCH_SIZE = 16
MAX_EPOCHS = 10

dataset = ImageFolder(data_dir,transform = transforms.Compose([
    transforms.Resize((150,150)),transforms.ToTensor()
]))

num_channels = dataset[0][0].shape[0]
num_classes = len(dataset.classes)

temp_data, test_data = random_split(dataset, [int(len(dataset)*0.8), int(len(dataset)*0.2)])
train_data, val_data = random_split(temp_data, [int(len(temp_data)*0.75), int(len(temp_data)*0.25)])


train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle = True)
val_loader = DataLoader(val_data, batch_size=BATCH_SIZE)
test_loader = DataLoader(test_data, batch_size=1)


trainSteps = len(train_loader)  # len(train_loader.dataset) // BATCH_SIZE
valSteps = len(val_loader)      # len(val_loader.dataset) // BATCH_SIZE

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f' Training on {device}')

model = CNN(num_channels,num_classes)
for n,v in model.named_parameters():
    print(n,v.shape)

model.to(device)
criterion = nn.NLLLoss()
# criterion = nn.CrossEntropyLoss()
# optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=0.0005)
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)


# Train the model
train_hist = pd.DataFrame(columns=['train_loss', 'train_acc', 'val_loss', 'val_acc'])


iterator = tqdm(range(1, MAX_EPOCHS + 1), total=MAX_EPOCHS+1)
for epoch in iterator:
# for epoch in range(1, MAX_EPOCHS+1):
    ep_sum = train(train_loader, val_loader, model, optimizer, criterion, device)
    iterator.write(f"EPOCH: {epoch}/{MAX_EPOCHS}Train loss: {ep_sum[0]:.4f}, Train accuracy: {ep_sum[1]:.4f} Val loss: {ep_sum[2]:.4f}, Val accuracy: {ep_sum[3]:.4f}")
    train_hist.loc[len(train_hist)] = ep_sum
    # print(f"EPOCH: {epoch}/{MAX_EPOCHS}")
    # print(f"Train loss: {avgTrainLoss:.4f}, Train accuracy: {trainCorrect:.4f}")
    # print(f"Val loss: {avgValLoss:.4f}, Val accuracy: {valCorrect:.4f}")
print('Finished training')

torch.save(model, 'CNN_flwr_{device}_{epoch}.pth')

plt.style.use("ggplot")
plt.figure()
plt.plot(train_hist["train_loss"], label="train_loss")
plt.plot(train_hist["val_loss"], label="val_loss")
plt.plot(train_hist["train_acc"], label="train_acc")
plt.plot(train_hist["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy on Dataset")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="lower left")
plt.savefig('plot.png')



print("[INFO] evaluating network...")
with torch.no_grad():
    model.eval()
    targets = []
    predictions = []
    for (inputs,labels) in test_loader:
        inputs = inputs.to(device)
        preds = model(inputs)
        predictions.extend(preds.argmax(axis=1).cpu().numpy())
        targets.extend(labels.cpu().numpy())

print(classification_report(np.array(targets), np.array(predictions), target_names=test_data.dataset.classes))
