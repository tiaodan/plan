import os


def mkdir(path):
    folder = os.path.exists(path)
    if folder:
        # print(f'{path} 文件已存在')
        pass
    else:
        print(f'创建文件夹 {path}')
        os.makedirs(path)

# mkdir("C:/home1/haha/11/22")
print('A B '.strip())