import pandas as pd

# Duong dan den file data.xlsx
iDanhMucCap = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\DanhMucCap.xlsx"
iDanhMucLoaiHinh = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\DanhMucLoaiHinh.xlsx"
iDanhMucLoaiTruong = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\DanhMucLoaiTruong.xlsx"
iDanhMucPhongDaoTao = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\DanhMucPhongDaoTao.xlsx"
iDanhMucSoDaoTao = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\DanhMucSoDaoTao.xlsx"
iGDTX = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\GDTX.xlsx"
iMN = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\MN.xlsx"
iTH = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\TH.xlsx"
iTHCS = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\THCS.xlsx"
iTHPT = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\THPT.xlsx"
pathTruong = [iGDTX, iMN, iTH, iTHCS, iTHPT]

# Path OUTPUT
oDanhMucCap = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\DanhMucCap.sql"
oDanhMucLoaiHinh = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\DanhMucLoaiHinh.sql"
oDanhMucLoaiTruong = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\DanhMucLoaiTruong.sql"
oDanhMucPhongDaoTao = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\DanhMucPhongDaoTao.sql"
oDanhMucSoDaoTao = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\DanhMucSoDaoTao.sql"
oTruong = r"D:\01_study\01_study_in_school\semester02\01_databases\practice\DO-AN-1\Data\DanhMucTruong.sql"



# File output: Data.sql
cap = open(oDanhMucCap, 'w', encoding="utf-8")
lh = open(oDanhMucLoaiHinh, 'w', encoding="utf-8")
lt = open(oDanhMucLoaiTruong, 'w', encoding="utf-8")
pdt = open(oDanhMucPhongDaoTao, 'w', encoding="utf-8")
sdt = open(oDanhMucSoDaoTao, 'w', encoding="utf-8")
truong = open(oTruong, 'w', encoding="utf-8")

# Dieu chinh du lieu dang string, loai bo cac ki tu: \n, ', ".
def form(string):
    if (type(string) is not str):
        return str(string)
    form = ""
    for x in string:
        if (x != '\n') & (x != chr(39)) & (x != chr(34)):
            form = form + x
    return form

# Comment truoc lenh INSERT cua 1 bang
def print_header(table, f):
    print("--", file=f)
    print("-- Dumping data for table `{}`".format(table), file=f)
    print("--\n", file=f)
    
# Comment sau lenh INSERT cua 1 bang
def print_footer(table, f):
    print("--", file=f)
    print("-- Completely dump data for table `{}`".format(table), file=f)
    print("--\n", file=f)
    
# Lenh INSERT cua SO
def import_table_so():
    print_header("so", sdt)
    data = pd.read_excel(iDanhMucSoDaoTao)
    for i in range (len(data)):
        print("INSERT INTO `so` VALUES ({},'{}');".format(data['IDSO'][i], data['TENSO'][i]), file=sdt)
    print_footer("so", sdt)
    
# Lenh INSERT cua PHONG
def import_table_phong():
    print_header("phong", pdt)
    data = pd.read_excel(iDanhMucPhongDaoTao)
    for i in range (len(data)):
        print("INSERT INTO `phong` VALUES ({},'{}', {});".format(data['IDPHONG'][i], data['TENPHONG'][i], data['IDSO'][i]), file=pdt)
    print_footer("phong", pdt)
    
# Lenh INSERT cua LOAIHINH
def import_table_loai_hinh():
    print_header("loaihinh", lh)
    data = pd.read_excel(iDanhMucLoaiHinh)
    for i in range (len(data)):
        print("INSERT INTO `loaihinh` VALUES ({},{});".format(data['IDLH'][i], chr(39) + data['TENLH'][i] + chr(39)), file=lh)
    print_footer("loaihinh", lh)
    
# Lenh INSERT cua LOAITRUONG
def import_table_loai_truong():
    print_header("loaitruong", lt)
    data = pd.read_excel(iDanhMucLoaiTruong)
    for i in range (len(data)):
        print("INSERT INTO `loaitruong` VALUES ({},'{}');".format(data['IDLT'][i], data['TENLT'][i]), file=lt)
    print_footer("loaitruong", lt)
    
# Lenh INSERT cua CAP
def import_table_cap():
    print_header("cap", cap)
    data = pd.read_excel(iDanhMucCap)
    for i in range (len(data)):
        print("INSERT INTO `cap` VALUES ('{}','{}');".format(data['IDCAP'][i], data['TENCAP'][i]), file=cap)
    print_footer("cap", cap)
    
# Kiem tra xem file excel do co field PHONG hay khong. Tra ve True neu Co. Nguoc lai tra ve False 
def is_have_phg(cap):
    if (cap == 'GDTX') | (cap == 'THPT'):
        return False
    else:
        return True

# Lenh INSERT cua TRUONG
def import_table_truong():
    print_header("truong", truong)
    cap = ['GDTX', 'MN', 'TH', 'THCS', 'THPT']
    for i_cap in range (len(cap)):
        data = pd.read_excel(pathTruong[i_cap])   
        idcap = form(cap[i_cap])                             
        for i in range (len(data)):
            matrg = form(data['MATRG'][i])
            tentrg = form(data['TENTRG'][i])
            # Kiem tra xem co bi missing data hay khong. Neu co thay bang null. Them truoc va sau du lieu dau "'" (chr(39)).
            dchi = "NULL" if pd.isnull(data['DCHI'][i]) else (chr(39) + form(data['DCHI'][i]) + chr(39))
            idso = "NULL" if pd.isnull(data['IDSO'][i]) else int(data['IDSO'][i])
            idphg = "NULL"
            # Neu khong co PHONG, tra ve NULL.
            if is_have_phg(cap[i_cap]):
                if pd.isnull(data['IDPHG'][i]) == False:
                    idphg = int(data['IDPHG'][i])
            idlh = "NULL" if pd.isnull(data['IDLH'][i]) else int(data['IDLH'][i])
            idlt = "NULL" if pd.isnull(data['IDLT'][i]) else int(data['IDLT'][i])
            print("INSERT INTO `truong` VALUES ('{}','{}',{},{},{},{},{},'{}');".format(matrg, tentrg, dchi, idso, idphg, idlh, idlt, idcap), file=truong)                                    
    print_footer("truong", truong)
    
import_table_so()
import_table_phong()
import_table_cap()
import_table_loai_hinh()
import_table_loai_truong()
import_table_truong()
