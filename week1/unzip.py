# coding=utf-8
# 循环解压压缩文件
import gzip
import tarfile
import zipfile
import os


# 递归遍历文件夹，若有压缩文件，则调用解压方法
def intofolder(filelist, roodir):

    for i in range(0, len(filelist)):
        print filelist
        tmppath = roodir + "/" + filelist[i]
        print "LOGGER:  当前文件夹为" + tmppath
        if os.path.isdir(tmppath):
            tmplist1 = os.listdir(tmppath)
            intofolder(tmplist1, tmppath)
        elif tmppath.__contains__(".tar") or tmppath.__contains__(".zip"):
            unZipFile(tmppath)
            # unTarfile(tmppath)
            tmplist2 = os.listdir(tmppath.split(".")[0] + "_files")
            tmppath2 = tmppath.split(".")[0] + "_files"
            intofolder(tmplist2, tmppath2)
        # elif tmppath.__contains__(".zip"):
        #     unZip(tmppath)
        #     tmplist2 = os.listdir(tmppath.split(".")[0] + "_files")
        #     tmppath2 = tmppath.split(".")[0] + "_files"
        #     intofolder(tmplist2, tmppath2)


# # 解压tar文件
# def unTarfile(file_name):
#     tar = tarfile.open(file_name)
#     names = tar.getnames()
#     rootdir = file_name.split(".")[0] + "_files"
#     if os.path.isdir(rootdir):
#         pass
#     else:
#         os.mkdir(rootdir)
#     for name in names:
#         tar.extract(name, rootdir)
#     filelist = os.listdir(rootdir)
#     print "1::" + rootdir
#     intofolder(filelist, rootdir)
#     tar.close()
#
#
# # 解压zip文件
# def unZip(file_name):
#     zipf = zipfile.ZipFile(file_name)
#     names = zipf.namelist()
#     rootdir = file_name.split(".")[0] + "_files"
#     if os.path.isdir(rootdir):
#         pass
#     else:
#         os.mkdir(rootdir)
#     for name in names:
#         zipf.extract(name, rootdir)
#     filelist = os.listdir(rootdir)
#     intofolder(filelist, rootdir)
#     zipf.close()


# unZip + unTarfile 合并
def unZipFile(file_name):
    rootdir = file_name.split(".")[0] + "_files"
    if os.path.isdir(rootdir):
        pass
    else:
        os.mkdir(rootdir)
    # 解压zip后缀文件
    if file_name.__contains__(".zip"):
        zipf = zipfile.ZipFile(file_name)
        names = zipf.namelist()
        for name in names:
            zipf.extract(name, rootdir)
        filelist = os.listdir(rootdir)
        print "LOGGER:  当前所在路径为：" + rootdir
        intofolder(filelist, rootdir)
        zipf.close()

    # 解压tar后缀文件
    elif file_name.__contains__(".tar"):
        print "111111"
        tarf = tarfile.open(file_name)
        names = tarf.getnames()
        print names
        for name in names:
            print name + rootdir
            tarf.extract(name, rootdir)
        filelist = os.listdir(rootdir)
        print "LOGGER:  当前所在路径为：" + rootdir
        intofolder(filelist, rootdir)
        tarf.close()


if __name__ == "__main__":
    tar = None
    filePath = str(raw_input("请输入文件路径:\n"))
    unZipFile(filePath)


