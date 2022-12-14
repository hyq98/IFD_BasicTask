from torch.utils.data import Dataset, DataLoader
from PIL import Image
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

transform = transforms.Compose(
        [transforms.Resize([256, 256]),
         transforms.ToTensor(),
         transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])       # jiancha huachulaide tupian


class MyDataSet(Dataset):
    
    def __init__(self, dataset_type, label_type, transform=transform):
        dataset_path = ''
        self.transform = transform
        self.sample_list = list()
        self.dataset_type = dataset_type
        f = open(dataset_path + self.dataset_type + '/'+label_type+'.txt')
        lines = f.readlines()
        for line in lines:
            self.sample_list.append(line.strip())
        f.close()

    def __getitem__(self, index):
        item = self.sample_list[index]
        img = Image.open(item.split(' ', 1)[0]).convert('RGB')                  # 标签文件使用的‘ ’做分隔符；
        if self.transform is not None:
            img = self.transform(img)
        label = int(item.split(' ')[-1])                # -1是标签
        return img, label

    def __len__(self):
        return len(self.sample_list)


if __name__ == '__main__':

    ds = MyDataSet('/45TB/hyq/lyb/IFD_BasicTask/label/CWSU_label', 'png_0_cwsu_train')
    print('样本数：', ds.__len__())
    img, gt = ds.__getitem__(4)
    # print('img 类型：', type(img))
    print('img 标签：', gt)
    print('img 维度：', img.size())
    # imshow(img)
    loader = DataLoader(ds, batch_size=16, shuffle=False, num_workers=0)
    for data in loader:
        img, label = data
    print(type(img))
    print(img.shape)
    print(type(label))
    print(label.shape)



