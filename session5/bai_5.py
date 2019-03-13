def is_inside(diem,hcn):
    if hcn[0] <= diem[0] <= hcn[0]+hcn[2] and hcn[1] <= diem[1] <= hcn[1]+hcn[3] :
        return True
    else:
        return False
point = [50,50]
rec = [60,60,120,200]
if is_inside(point,rec):
    print('Điểm',point,'nằm trong hcn')
else:
    print('Điểm',point,'không nằm trong hcn')
point_inside_rectangle = is_inside([200,120],[140,60,100,200])
if point_inside_rectangle == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")