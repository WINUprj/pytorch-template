import torch 
from torch.utils.data import DataLoader, Dataset 


class TableTrainData(Dataset):
    def __init__(self, data, labels):
        super().__init__()
        self.data_ = data
        self.labels_ = labels 

    def __call__(self):
        raise NotImplementedError 


class TableTestData(Dataset):
    def __init__(self, test_data):
        self.test_data_ = test_data 
    
    def __call__(self):
        raise NotImplementedError 


class ImageTrainData(Dataset):
    def __init__(self, data, labels, img_dir, transform=None):
        super().__init__()
        self.data_ = data 
        self.labels_ = labels 
        self.img_dir_ = img_dir 
        self.transform_ = transform 

    def __call__(self):
        raise NotImplementedError 


class ImageTestData(Dataset):
    def __init__(self, data, img_dir, transform=None):
        super().__init__()
        self.data_ = data 
        self.img_dir_ = img_dir
        self.transform_ = transform 

    def __call__(self):
        raise NotImplementedError 