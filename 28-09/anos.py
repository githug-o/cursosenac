hab1 = 80000
hab2 = 200000
txpais1 = 1.03
txpais2 = 1.015

anos = 0
while hab1<hab2:
    hab1 = hab1*txpais1
    hab2 = hab2*txpais2
    anos = anos+1

print(anos, "anos")