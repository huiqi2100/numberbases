# converter.py
# convert number bases

import math

def dec_to_bin(dec_num):
    bin_num = ""
    while dec_num != 0:
        bin_num = str(dec_num%2) + bin_num
        dec_num = dec_num // 2
    return bin_num
    
def dec_to_oct(dec_num):
    bin_num = dec_to_bin(dec_num)
    oct_num = bin_to_oct(bin_num)
    return oct_num    
    
def dec_to_hex(dec_num):
    bin_num = dec_to_bin(dec_num)
    hex_num = bin_to_hex(bin_num)
    return hex_num
    
def bin_to_oct(bin_num):
    bin_num = str(bin_num)
    if len(bin_num)%3 == 0:
        bin_num = bin_num
    else:
        bin_num = (3 - (len(bin_num)%3)) * "0" + bin_num
    binoct = {"000":"0", "001":"1", "010":"2", "011":"3", "100":"4", "101":"5",
              "110":"6", "111":"7"}
    i = 0
    oct_num = ""
    while i+2 < len(bin_num):
        j = i + 3
        group = bin_num[i:j]
        oct_num = oct_num + binoct[group]
        i = i + 3
    return oct_num
    
def bin_to_dec(bin_num):
    bin_num = str(bin_num)
    dec_num = 0
    for i in range(0, len(bin_num)):
        dec_num = dec_num + (int(bin_num[i]) * (2**(len(bin_num)-1-i)))
    return dec_num

def bin_to_hex(bin_num):
    bin_num = str(bin_num)
    if len(bin_num)%4 == 0:
        bin_num = bin_num
    else:
        bin_num = (4 - (len(bin_num)%4)) * "0" + bin_num
    binhex = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4",
              "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9",
              "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E",
              "1111":"F"}
    i = 0
    hex_num = ""
    while i < len(bin_num):
        j = i + 4
        group = bin_num[i:j]
        hex_num = hex_num + binhex[group]
        i = i + 4
    return hex_num
    
def oct_to_bin(oct_num):
    oct_num = str(oct_num)
    octbin = {"0":"000", "1":"001", "2":"010", "3":"011", "4":"100", "5":"101",
              "6":"110", "7":"111"}
    bin_num = ""
    for i in oct_num:
        bin_num = bin_num + octbin[i]
    return bin_num
    
def oct_to_dec(oct_num):
    bin_num = oct_to_bin(oct_num)
    dec_num = bin_to_dec(bin_num)
    return dec_num
    
def oct_to_hex(oct_num):
    bin_num = oct_to_bin(oct_num)
    hex_num = bin_to_hex(bin_num)
    return hex_num
    
def hex_to_bin(hex_num):
    hex_num = str(hex_num)
    hexbin = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100",
              "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001",
              "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110",
              "F":"1111"}
    bin_num = ""
    for i in hex_num:
        bin_num = bin_num + hexbin[i]
    return bin_num
    
def hex_to_oct(hex_num):
    bin_num = hex_to_bin(hex_num)
    oct_num = bin_to_oct(bin_num)
    return oct_num
    
def hex_to_dec(hex_num):
    bin_num = hex_to_bin(hex_num)
    dec_num = bin_to_dec(bin_num)
    return dec_num
