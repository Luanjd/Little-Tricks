# 应用yolov5, 将文件按文件类型分类
import os,shutil,time
import datetime

def file_path_correct(filepath, target_path):
    '''
    如果target_path中已经存在filename, 则返回新的path (file + datetime)
    '''
    filename = filepath.split('/')[-1]
    father_dir = '/'.join(filepath.split('/')[:-1])
    if os.path.exists(os.path.join(target_path, filename)):
        new_name = '{0}_{1}.{2}'.format(filename.split('.')[0],datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
                                         filename.split('.')[-1])
        new_path = father_dir + new_name
        os.rename(filepath, new_path)
        return new_path
    else:
        return filepath
   

def files_classify(target_path):
    '''
    先将工作目录置于根目录。适用于根目录是文件夹，子文件为文件夹
    '''
    global count  #定义全局变量
    dir_list = os.listdir(target_path)   #列出目标路径下的所有文件列表
    for dir in dir_list:  #遍历取到每一个文件名
        files_path = os.path.join(target_path, dir)
        for file in os.listdir(files_path):
            if file.find('.') == -1: #如果当前文件名中无扩展名则跳过
                print(dir, file, 'is a directory')
                continue    
            filetype = file.split('.')[-1]  #取得文件扩展名格式，windows下文件需设置为扩展名可见
            destination_path = os.path.join(target_path, filetype)  #取得当前扩展名文件夹路径
            if not os.path.exists(destination_path):
                os.mkdir(destination_path)      #如果工作目录下不存在以当前扩展名命名的文件夹则创建该文件夹（默认属性为0777）
                print('new dir made')
            # destinaition_path = os.path.join(target_path, filetype)  #取得当前扩展名文件夹路径
            # os.chdir(new_path)

            file_path = os.path.join(target_path, dir, file)
            try:
                shutil.move(file_path, destination_path)  # 移动相同格式的文件到对应的格式文件夹
            except:
                shutil.move(file_path_correct(file_path, destination_path), destination_path)
            count += 1

start = time.time()
count = 0
rep_count = 0
path = ""
files_classify('./media/data1/ljd/select/fire')
total_time = time.time() - start
print("程序运行时间：%0.2f"%total_time)
print("共处理文件：%d"%count)
