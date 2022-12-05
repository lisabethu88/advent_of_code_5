f = open("/Users/lisautsett/Developer/advent_of_code/advent_of_code_5/advent_of_code_5/input.txt", "r")

"""
[J]             [F] [M]            
[Z] [F]     [G] [Q] [F]            
[G] [P]     [H] [Z] [S] [Q]        
[V] [W] [Z] [P] [D] [G] [P]        
[T] [D] [S] [Z] [N] [W] [B] [N]    
[D] [M] [R] [J] [J] [P] [V] [P] [J]
[B] [R] [C] [T] [C] [V] [C] [B] [P]
[N] [S] [V] [R] [T] [N] [G] [Z] [W]
 1   2   3   4   5   6   7   8   9 
"""

dict = {1:['N', 'B', 'D', 'T', 'V', 'G', 'Z', 'J'],
2:['S', 'R', 'M', 'D', 'V', 'P', 'F'], 
3:['V', 'C', 'R', 'S', 'Z'], 
4:['R','T','J', 'Z', 'P', 'H', 'G'], 
5:['T', 'C', 'J', 'N', 'D', 'Z', 'Q', 'F'], 
6:['N', 'V', 'P', 'W', 'G', 'S', 'F', 'M'], 
7:['G', 'C', 'V', 'B', 'P', 'Q'], 
8:['Z', 'B', 'P', 'N'], 
9:['W', 'P', 'J']}


#move 2 from 4 to 6
# move by new_list[1], from =  new_list[3], to = new_list[6]
for line in f:
    line = line.strip()
    new_list = line.split(" ")
    for i in range(len(new_list[1])-1, len(new_list[1])):
        move_this_many = int(new_list[1])
        from_this_list = int(new_list[3])
        to_this_list = int(new_list[5])
        temp_list=[]
        for j in range(move_this_many):
            temp_list.append(dict[from_this_list].pop())

        for k in range(move_this_many):
            dict[to_this_list].append(temp_list.pop())   



result = ""
for i in range(1, len(dict)+1):
    result+=dict[i][-1]
print(result)