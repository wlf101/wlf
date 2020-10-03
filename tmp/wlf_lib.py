import os
import matplotlib.pyplot as plt
import csv
import pandas as pd

# file
def wlf_dir(dir):
    os.chdir(dir)
    list_dir = os.listdir(dir)
    return list_dir
def file_select_cv(path):
    # find cv.txt file
    file = wlf_dir(path)
    file_cv = []
    for i in file:
        if i.find('cv') != -1 and i.find('txt') != -1:
            file_cv.append(i)
    return file_cv
def file_select_cp(path):
    # find cp.txt file
    file = wlf_dir(path)
    file_cp = []
    for i in file:
        if i.find('cp') != -1 and i.find('txt') != -1:
            file_cp.append(i)
    return file_cp
def file_select_eis(path):
    # find cp.txt file
    file = wlf_dir(path)
    file_eis = []
    for i in file:
        if i.find('EIS') != -1 and i.find('txt') != -1:
            file_eis.append(i)
    return file_eis
def file_find_line_cv(file):
    # find line 'Potential/V, Current/A\n' cv
    with open(file, 'r') as f:
        lines = f.readlines()
    i = 0
    t = 0
    for line in lines:
        i = i + 1
        if line == 'Potential/V, Current/A\n':
            t = i
    return t+1
def file_del_head_cv(file):
    # del head cv
    file_cv = []
    i = 0
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        i = i + 1
        if i > file_find_line_cv(file):
            file_cv.append(line)
    return file_cv
def file_find_line_cp(file):
    # find line 'Time/sec, Potential/V\n' cp
    with open(file, 'r') as f:
        lines = f.readlines()
    i = 0
    t = 0
    for line in lines:
        i = i + 1
        if line == 'Time/sec, Potential/V\n':
            t = i
    return t+1
def file_find_line_eis(file):
    # find line 'Freq/Hz, Z'/ohm, Z"/ohm, Z/ohm, Phase/deg\n' cp
    with open(file[0], 'r') as f:
        lines = f.readlines()
    i = 0
    t = 0
    for line in lines:
        i = i + 1
        if line == 'Freq/Hz, Z\'/ohm, Z\"/ohm, Z/ohm, Phase/deg\n':
            t = i
    return t+1
def file_del_head_cp(file):
    # del head cp
    file_cp = []
    i = 0
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        i = i + 1
        if i > file_find_line_cp(file):
            file_cp.append(line)
    return file_cp
def file_del_head_eis(file):
    # del head eis
    file_eis = []
    i = 0
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        i = i + 1
        if i > file_find_line_eis(file):
            file_eis.append(line)
    return file_eis
def devide_list_cv(file_cv):
    # devide list cv
    vol = []
    cur = []
    for i in file_cv:
        a = i.split(",", 1)
        vol.append(float(a[0]))
        cur.append(float(a[1]))
    return vol, cur
def devide_list_cp(file_cp):
    # devide list cv
    vol = []
    cur = []
    for i in file_cp:
        a = i.split(",", 1)
        vol.append(float(a[0]))
        cur.append(float(a[1]))
    return vol, cur
def max_list(A,B):
    point = len(B) / 40
    n = 0
    while n * point < len(B):
        n = n + 1
    C = []
    D = []
    E = []
    for i in range(n - 1):
        C1 = max(B[i * point:(i + 1) * point])
        C2 = B[i * point:(i + 1) * point].index(C1) + i * point
        if C1 > B[i * point] and C1 > B[(i + 1) * point]:
            C.append(C1)
            D.append(C2)
    D.append(A.index(A[-1]))
    return D
def list_last_cp(vol, cur):
    # list last cycle cp
    A = vol
    B = cur
    point = len(B) // 10
    n = 0
    while n * point < len(B):
        n = n + 1
    C = []
    D = []
    for i in range(n - 1):
        C1 = min(B[i * point:(i + 1) * point])
        C2 = B[i * point:(i + 1) * point].index(C1) + i * point
        if C1 < B[i * point] and C1 < B[(i + 1) * point]:
            C.append(C1)
            D.append(C2)

    D.append(A.index(A[-1]))
    vol = vol[D[-2]:]
    vol = [i - vol[0] for i in vol]
    cur = cur[D[-2]:]
    return vol, cur
def list_last_cv(vol, cur):
    # list last cycle cv
    A = vol
    B = cur
    point = len(B) // 5
    n = 0
    while n * point < len(B):
        n = n + 1
    C = []
    D = []
    for i in range(n - 1):
        C1 = min(B[i * point:(i + 1) * point])
        C2 = B[i * point:(i + 1) * point].index(C1) + i * point
        if C1 < B[i * point] and C1 < B[(i + 1) * point]:
            C.append(C1)
            D.append(C2)
    D.append(A.index(A[-1]))
    vol = vol[D[-2]:]
    cur = cur[D[-2]:]
    return vol, cur
def rm_file(path):
    if os.path.exists(path):
        os.remove(path)
def concat(vol, cur):
    vol = pd.DataFrame({'': vol})
    cur = pd.DataFrame({'': cur})
    data = pd.concat([vol, cur], axis=1)
    return data












