import os
import PreTest


def getPath():
    while True:
        DirPath = input('Enter directory path:')
        if os.path.exists(DirPath):
            return DirPath
        else: print('Path does not exist!')

def getInputFolders() -> list:
    folders = list()
    while True:
        folder = input('''Enter folder's name:''')
        if not folder: break
        folders.append(folder)
    return folders

def FormatPath(path:str):
    return '\\\\'.join(path.split('\\'))

def concatenatePath(listStr:list):
    return '\\\\'.join(listStr)


def FileHandling(ResultFolder = 'Test_Result'):
    # get the path of folder from user and format it to use in python
    # DirPath = FormatPath(getPath())
    DirPath = 'C:\\Users\\ASUS\\Desktop\\File-Handling-Project\\Test_Case'
    
    # Get folders name
    # folders = getInputFolders() + ['Others', 'UnDefined']
    folders = ['AI1601', 'AI1602', 'AI1604', 'Others', 'UnDefined']
    
    # Create folder result if not exist
    if not os.path.isdir(concatenatePath([os.path.dirname(DirPath), ResultFolder])):
        os.makedirs(concatenatePath([os.path.dirname(DirPath), ResultFolder]))
    
    for folder in folders:
        if not os.path.isdir(concatenatePath([os.path.dirname(DirPath), ResultFolder, folder])):
            os.makedirs(concatenatePath([os.path.dirname(DirPath), ResultFolder, folder]))

    checkFolders = [False]*len(folders)
    files = os.listdir(DirPath)
    
    FileCounter = 0
    
    for file in files:
        if os.path.exists(concatenatePath([DirPath,file])):
            if os.path.isfile(concatenatePath([DirPath,file])):
                FileCounter += 1
                name = file.split('.')[0]
                checkFolders = [i.upper() in name.upper() for i in folders]
                
                if checkFolders.count(True) > 1:
                    checkFolders = [False]*len(folders)
                    checkFolders[folders.index('UnDefined')] = True
                elif checkFolders.count(True) == 0:
                    checkFolders[folders.index('Others')] = True
                FileCounter = os.system('copy "'+concatenatePath([DirPath,file])+'\" \"'+concatenatePath([os.path.dirname(DirPath), ResultFolder, folders[checkFolders.index(True)], file])+'"')
    print(f'Total {FileCounter} has been copied.')
    
FileHandling()

# path = 'C:\\Users\\ASUS\\Desktop\\File-Handling-Project\\Test_Case'
# folders = ['AI1601', 'AI1602', 'AI1604', 'Others', 'UnDefined']

# if not os.path.isdir('C:\\Users\\ASUS\\Desktop\\File-Handling-Project\\Test_Result'):
#     os.makedirs('C:\\Users\\ASUS\\Desktop\\File-Handling-Project\\Test_Result')

# for folder in folders:
#     if not os.path.isdir('C:\\Users\\ASUS\\Desktop\\File-Handling-Project\\Test_Result\\'+folder):
#         os.makedirs('C:\\Users\\ASUS\\Desktop\\File-Handling-Project\\Test_Result\\'+folder)


# pathResult = FormatPath(os.path.dirname(path)+'\Test_Result')
# checkFolders = [False]*len(folders)
# files = os.listdir(path)

# for file in files:
#     if os.path.isfile(path+'\\'+file):
#         name, extension = file.split('.')
#         checkFolders = [i in name.upper() for i in folders]
#         if checkFolders.count(True) > 1:
#             checkFolders = [False]*len(folders)
#             checkFolders[folders.index('UnDefined')] = True
#         elif checkFolders.count(True) == 0:
#             checkFolders[folders.index('Others')] = True
        
#         os.system('copy '+path+'\\'+file+' '+pathResult+'\\'+folders[checkFolders.index(True)] +'\\'+file)


# os.system('copy "a b.txt" "a b_copy.txt"')





    