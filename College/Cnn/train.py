import torch


def train(trainloader, valloader, model,optimizer, criterion, device):
    model.train()
    totalTrainLoss = 0
    totalValLoss = 0
    trainCorrect = 0
    valCorrect = 0

    for (inputs, labels) in trainloader:
        (inputs, labels) = (inputs.to(device), labels.to(device))
        # labels = torch.tensor(labels)
        preds = model(inputs)
        loss = criterion(preds, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        totalTrainLoss += loss
        trainCorrect += (preds.argmax(1) == labels).type(torch.float).sum().item()

    with torch.no_grad():
        model.eval()
        for (inputs, labels) in valloader:
            (inputs, labels) = (inputs.to(device), labels.to(device))
            preds = model(inputs)
            loss = criterion(preds, labels)
            totalValLoss += loss
            valCorrect += (preds.argmax(1) == labels).type(torch.float).sum().item()

    avgTrainLoss = totalTrainLoss / len(trainloader)
    avgValLoss = totalValLoss / len(valloader)

    avgTrainLoss = avgTrainLoss.cpu().detach().numpy()
    avgValLoss = avgValLoss.cpu().detach().numpy()

    trainCorrect = trainCorrect / len(trainloader.dataset)
    valCorrect = valCorrect / len(valloader.dataset)

    return [avgTrainLoss, trainCorrect, avgValLoss, valCorrect]
