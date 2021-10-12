# def flipped_bits(bin):
#     flipped = ''
#     for bit in range(len(bin)):
#         if (bin[bit] == '0'):
#             flipped+= '1'
#         else:
#             flipped+= '0'
#     return flipped

# print(flipped_bits('1100'))

def flipped_bits_2(bin):
    flipped = list(bin)
    for bit in range(len(bin)):
        if (bin[bit] == '0'):
            flipped[bit] = '1'
        else:
            flipped[bit] = '0'
    return "".join(flipped)



# print(flipped_bits_2('0111'))


#key notes when adding binary: 0+1 = 1 c 0, 1+1 = 0 c 1, 1+1+1 = 1 c 1
#step 1: we will be adding three values: the binary string, the carry_list set to ='0000', 
#and the add one binary representation => '0001'
#step 2: loop through the binary string (going backwards because we add from right to left)
# if binary[index] + add_one[index] + carry_list[index] == 3, we will concat 1 to the results string 
#variable and make the leftmost index of the carry_list = 1
# if binary[index] + add_one[index] + carry_list[index] == 2, we will concat 0 to the results string 
#variable and make the leftmost index of the carry_list = 1
# if binary[index] + add_one[index] + carry_list[index] == 1, we will concat 1 to the results string 
#variable and make the leftmost index of the carry_list = 0
# if binary[index] + add_one[index] + carry_list[index] == 0, we will concat 0 to the results string 
#variable and make the leftmost index of the carry_list = 0
#step 3: return results reversed.


def add_one(bin):
   
    carry = 1
    i = len(bin) - 1
    sum = ''
    while ( i >= 0):
        if((int(bin[i])) + carry == 2):
            carry = 1
            sum += '0'
        elif((int(bin[i])) + carry == 3):
            carry = 1
            sum+= '1'
        elif((int(bin[i])) + carry == 1):
            carry = 0
            sum +='1'
        elif((int(bin[i])) + carry == 0):
            carry = 0
            sum += '0'
        i-=1
    if(carry == 1):
        sum +='1'
    return sum[::-1]

def bin2dec(bin):
    return int(bin,2)

def add_one_2(bin):
    return 1 + bin2dec(bin)

print(add_one('1111'))
print(add_one_2('1111'))