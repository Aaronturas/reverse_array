def reverse_list(num_list, start, end):
    # Write your code here
    new_list = []
    index_list = num_list[start:end+1]#end needs 1 to add on because of the indexes
    print(index_list)
    
    for i in index_list[::-1]:#reversed the subarray by appending from the last element in a loop to a new list
        new_list.append(i)
        
    if len(new_list) == len(num_list):#if the both lenghts of new array and old array are equal then just return reversed array
            return new_list    
    
    while start <= end: #while loop needs to be less than or equal because of the indexes
        num_list[start] = new_list[start]
        start += 1
    return num_list

#TestCases
num_list = [1, 2, 3]
start = 0
end = 3
print(reverse_list(num_list, start, end),'\n')

num_list = [4,5,1,2]
start = 0
end = 2
print(reverse_list(num_list, start, end))