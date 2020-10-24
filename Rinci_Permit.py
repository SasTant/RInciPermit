
def baca_p():
    baca = open('PERMIT.txt','r')
    return baca.readlines()


def baca_st():
    baca2 = []
    for line in baca_p():
        if len(line) > 70:
              baca2.append(line.strip())
    return baca2


def baca_st_sel(sel):
    baca3=[]
    for line in baca_sel():
        if line == sel:
              baca3.append(line.strip())
    return baca3


def baca_sel():
    id_sel=[]
    for line in baca_st():
        id_sel.append(line[:2])
    return id_sel


def baca_exp():
    exp=[]
    for line in baca_st():
        exp.append(line[8:16])
    exp.sort()
    return exp


def hitung_sel():
    cek2=baca_sel()
    tes=0
    hit_sel=[]
    for line in cek2:
        jml=len(baca_st_sel(line))
        if tes != line:
            print("Jumlah cell "+str(line)+ "= "+str(jml))
            hit_sel.append(line.strip())
            hit_sel.append(jml)
            tes=line
    print("Jumlah cell Total= "+str(len(cek2)))
    hit_sel.append('total')
    hit_sel.append(len(cek2))
    return hit_sel

def hitung_exp():
    cek_exp=baca_exp()
    tes=0
    basi=[]
    for line in cek_exp:
        if tes != line:
            basi.append(line.strip())
            tes=line
    return basi


def cetak_basi():
    ind_exp=[]
    Q = 0
    for line in hitung_exp():
        print("Cell expiry date (YYYYMMDD) =" +str(line))
        ind_exp.append("Indeks Expiry "+ str(Q) + "= " + str(line))
        Q = Q + 1
    return ind_exp

def hitung_sel_exp(ex):
    exp1=[]
    line_x = hitung_exp()
    for line in baca_st():
        if line_x[ex] in line:
            exp1.append(line.strip())
    print('sell yang habis pada '+ line_x[ex] +' berjumlah ' + str(len(exp1)))
    exp1.append('sell yang habis pada '+ line_x[ex] +' berjumlah ' + str(len(exp1)))
    print(exp1)
    return exp1[-1]

def cetak_hse():
    a=0
    for i in hitung_exp():
        hitung_sel_exp(a)
        a=a+1



# print(baca_sel())
# print(hitung_sel())
# #print(baca_exp())
# # print(hitung_exp())
# cetak_basi()
# # hitung_sel_exp(1)
# # hitung_sel_exp(0)
# cetak_hse()
