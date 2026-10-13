print("***************Student Marks List Mangament**********************")
marks=[78,67,89,78,92]#creating a list
print("Marks list:",marks)
print("----------------------------------------------------------------")
print("Highest marks:",max(marks))
print("----------------------------------------------------------------")
print("Lowest marks:",min(marks))
print("----------------------------------------------------------------")
print("Length of marks",len(marks))
print("----------------------------------------------------------------")
print("First mark:",marks[0])
print("----------------------------------------------------------------")
print("Last marks:",marks[-1])
print("----------------------------------------------------------------")
print("The first three marks:",marks[0:3])
print("----------------------------------------------------------------")
print("Times 78 appear:",marks.count(78))
print("----------------------------------------------------------------")
#To find out the index value:
print("Index of 78:",marks.index(78))
print("---------------------------------------------------------------")
#adding new elemnt to the last
marks.append(85)
print("Adding 85:",marks)
print("---------------------------------------------------------------")
#adding new element to the selected range
marks.insert(1,95)
print("Inserting 95 at index 1:",marks)
print("---------------------------------------------------------------")
#Adding multiple elements to the list
new_marks=[71,88]
marks.extend(new_marks)
print("Extending the list:",marks)
print("--------------------------------------------------------------")
marks.remove(78)# remove the element for ur specific range
print("Remove 78:", marks)
print("--------------------------------------------------------------")
marks.pop()#means remove the last element
print("Poping :",marks)
print("-------------------------------------------------------------")
marks.sort()#in ascending order
print("Sorting the list:",marks)
print("--------------------------------------------------------------")
marks.reverse()
print("Reverse the elements:",marks)
print("--------------------------------------------------------------")
print("-------------THANK YOU-----------------------------------------")
print("---------------------------------------------------------------")
