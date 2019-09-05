# 1. Get how long the sequence is from the user
# 2. Realise that the sequence doesn't work for a(0),a(1) and a(2), so let a(0) = 1, a(1) = 2 and a(2) = 3
# 3. Implement the sequence a(n) = a(n-1)*2 - (n-3)
# 4. print each number of the sequence with a "," inbetween

n = int(input("Enter the length of the sequence: ")) # Do not change this line
seq_num = 0
difference = 0
for i in range(0, n):
    difference = seq_num*2 - (i-3)
    if 0 <= i <=2:
        seq_num += 1
    else:
        seq_num = difference
    print(seq_num, end=", ")
