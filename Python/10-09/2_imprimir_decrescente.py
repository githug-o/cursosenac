arr=[]
for i in range(3):
    num = int(input("Manda: "))
    arr.append(num)
print(f"{max(arr)}\n{(sum(arr)-min(arr)-max(arr))}\n{min(arr)}")