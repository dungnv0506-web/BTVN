import math

def cong(p1, p2):
    tu = p1[0] * p2[1] + p2[0] * p1[1]
    mau = p1[1] * p2[1]
    return rut_gon(tu, mau)

def tru(p1, p2):
    tu = p1[0] * p2[1] - p2[0] * p1[1]
    mau = p1[1] * p2[1]
    return rut_gon(tu, mau)

def nhan(p1, p2):
    tu = p1[0] * p2[0]
    mau = p1[1] * p2[1]
    return rut_gon(tu, mau)

def chia(p1, p2):
    tu = p1[0] * p2[1]
    mau = p1[1] * p2[0]
    return rut_gon(tu, mau)

def rut_gon(tu, mau):
    ucln = math.gcd(tu, mau)
    return tu // ucln, mau // ucln