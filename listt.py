color=input("enter color seperated by commas:")
color_list1=color.split(',')
print(color_list1)
print("First Color:", color_list1[0])
print("Second Color:", color_list1[-1])
color_list2={"red","orange","black","white"}
print("color_list1 not contained in color_list2 are:")
diff=list(set(color_list1) - set(color_list2))
print(diff)
color_int_list=[]
for color in color_list1:
    color_int_list.append(len(color))
    print(f"list of integers corresponding to each color: {color_int_list}")
