# 1. Get how long the sequence is from the user
# 2. Realise that the sequence doesn't work for a(0),a(1) and a(2), so let a(0) = 1, a(1) = 2 and a(2) = 3
# 3. Implement the sequence a(n) = a(n-1)*2 - (n-3)  i.e: a(4) = a(3)*2 - (4-3) = 6*2 - 1 = 11
# 4. print each number of the sequence with a "," inbetween

n = int(input("Enter the length of the sequence: ")) # Do not change this line

seq_num = 0
difference = 0

#Let the loop run from index 0 to index n-1, that's the total of n numbers
for i in range(0, n):
    difference = seq_num*2 - (i-3)  # Here is the sequence a(n) = a(n-1)*2 - (n-3)
    if 0 <= i <=2:                  # The sequence does not work for a(0), a(1) and a(2), so let's asign them values
        seq_num += 1
    else:
        seq_num = difference        # We store the seq_num here so we can use it for calculation for the next loop
    if i != (n-1):
        print(seq_num, end=", ")    # Put a comma when it is not the last number
    else:
        print(seq_num)
