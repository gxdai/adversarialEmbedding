import os
import argparse
import numpy as np

def generateListFile(inputDir, trainList, testList):
    fid_train   =   open(trainList, 'w')
    fid_test    =   open(testList, 'w')
    class_names =   os.listdir(inputDir)    # list all the classes

    for i, class_name in enumerate(class_names):
        subpath = os.path.join(inputDir, class_name)
        trainpath = os.path.join(subpath, 'train')
        trainFile = os.listdir(trainpath)
        testpath = os.path.join(subpath, 'test')
        testFile = os.listdir(testpath)
        for tmpFile in trainFile:
            if ('.jpg' in tmpFile) or ('.JPG' in tmpFile):
                fid_train.write(os.path.join(trainpath, tmpFile) + ' ' + str(i) + '\n')
        for tmpFile in testFile:
            if ('.jpg' in tmpFile) or ('.JPG' in tmpFile):
                fid_test.write(os.path.join(testpath, tmpFile) + ' ' + str(i) + '\n')

    fid_train.close()
    fid_test.close()




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generating the list file of input data ')
    parser.add_argument('--inputDir', type=str, default='/media/MMVC_AD/Guoxian_Dai/data/modelnet/modelnet40/projection/mvcnn/12/modelnet40v1')
    parser.add_argument('--trainList', type=str, default='modelnet40_train.txt')
    parser.add_argument('--testList', type=str, default='modelnet40_test.txt')

    args = parser.parse_args()

    generateListFile(inputDir=args.inputDir, trainList=args.trainList, testList=args.testList)
