from torch import nn

def create_model():
    # your code here
    # return model instance (None is just a placeholder)
    model = nn.Sequential(nn.Linear(784, 256),
                           nn.ReLU(),
                           nn.Linear(256, 16),
                           nn.ReLU(), 
                           nn.Linear(16, 10))

    return None
    return model

def count_parameters(model):
    # your code here
    # return integer number (None is just a placeholder)

    return None
    cnt = 0
    for i in model.parameters(): 
        if i.requires_grad == False: 
            continue
        cnt += i.numel()
    # верните количество параметров модели model
    return cnt
