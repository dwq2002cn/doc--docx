#coding=gbk
import os
from win32com import client


def doc_to_docx(path):
    if os.path.splitext(path)[1] == ".doc":
        word = client.Dispatch('Word.Application')# ����word �ĵ�
        doc = word.Documents.Open(path)  # Ŀ��·���µ��ļ�����·���µ��ĵ�
        doc.SaveAs(os.path.splitext(path)[0] + ".docx", 16)  # ת����·���µ��ļ�
        doc.Close()
        word.Quit()


def find_file(path, ext, file_list=[]):
    dir = os.listdir(path)
    for i in dir:
        i = os.path.join(path, i)
        if os.path.isdir(i):
            find_file(i, ext, file_list)
        else:
            if ext == os.path.splitext(i)[1]:
                file_list.append(i)
    return file_list


if __name__ == "__main__":
    dir_path = "D:\\360��ȫ���������"
    ext = ".doc"
    file_list = find_file(dir_path, ext)
    for file in file_list:
        doc_to_docx(file)
        print(file)
