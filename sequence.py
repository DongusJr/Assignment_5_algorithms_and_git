# 1. Get how long the sequence is from the user
# 2. Set 3 numbers for the sequence, a(1) = 1, a(2) = 2 and a(3) = 3
# 3. Implement the sequence for n > 3 a(n) = a(n-1) + a(n-2) + a(n-3)
# 4. Since we do not store the numbers permanently in a list we need to change them as the loops moves forward
# 5. print each number of the sequence

n = int(input("Enter the length of the sequence: ")) # Do not change this line

number_one = 1    # a(n-3)
number_two = 2    # a(n-2)
number_three = 3  # a(n-1) 
for i in range(1, n+1):  # In the range 1 to n
    if 1 <= i <= 3:      # The first 3 numbers are forced into the sequence, the rest is automatic
        print(i)
    else:
        seq_num = number_one + number_two + number_three  #a(n) = a(n-1) + a(n-2) + a(n-3)
        number_one = number_two          #We want to move the sequence forward,
        number_two = number_three        #so we need to move a(n-3) to a(n-2), a(n-2) to a(n-1),
        number_three = seq_num           #a(n-1) to a(n)
        print(seq_num)
