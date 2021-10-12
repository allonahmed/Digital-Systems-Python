import sys
sys.path.append("../part0")
from client_csv import *

class NumberConverter:

    def __init__(self):
        self.row = None

    def set_row(self, row): 
        self.row = row

    def return_row(self): #test
        return self.row

    def to_pad(self, string): #padding helper function
        while len(string) % 4 != 0:
            string = '0' + string
        return string

    def decimal_to(self, decimal, base): #decimal to base conversion
        if (int(decimal) < 1):
            return ''
        else:
            return self.decimal_to(int(decimal)//base, base) + str(int(decimal)%base) 
    
    def bin_to_dec(self, binary):
        exp = 0
        results = 0
        for i in range(len(binary) -1, -1, -1):
            results += int(binary[i]) * (2**exp)
            exp += 1
        return str(results)

    def bin_to_hex(self, binary):
        conversion = hex(int(self.bin_to_dec(binary)))
        return conversion[2:len(conversion)].upper() #slices the string to get rid of the 'Ox' prefix

    def bin_to_hex2(self, bin): #alternative method brute force (0(n^2))
        converter = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': 7,
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
        binary = list(converter) #access key elements (binary)
        updated_bin = self.to_pad(bin) # add neccessary zeros
        i = 0
        results = ''
        while (i < len(updated_bin)):
            string = updated_bin[i:i+4] # slice hexi string into a four string 
            for j in binary:
                if ( string  == j):
                    results += converter.get(j)
            i += 4
        return results

    def bin_to_oct(self, binary):
        while(len(binary) % 3 != 0):
            binary = '0' + binary
        results = ''
        i = 0
        while (i < len(binary)):
            results = results + self.bin_to_dec(binary[i:i+3])
            i += 3
        return results

    def hex_to_binary(self, hexi):
        converter = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': 7,
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
        binary = list(converter) #access key elements (binary)
        i = 0
        results = ''
        for i in range(0, len(hexi)):
            for j in range (0, len(converter)):
                if (hexi[i] == converter.get(binary[j])):
                    results += binary[j]   
        return results

    def hex_to_decimal(self,hexi):
        return self.bin_to_dec(self.hex_to_binary(hexi))
    
    def hex_to_octal(self, hexi):
        return self.bin_to_oct(self.hex_to_binary(octal))
    
    def octal_to_binary(self, octal):
        convert = ['000', '001', '010', '011', '100', '101', '110', '111']
        results = ''
        for i in range(0, len(octal)):
            results += convert[int(octal[i])]
        return results

    def octal_to_decimal(self, octal):
        return self.bin_to_dec(self.octal_to_binary(octal)) 
    
    def octal_to_hex(self, octal):
        return self.bin_to_hex(self.octal_to_binary(octal))
    
    def flipped_bits(self, bin): #helper function for flipping bits
        flipped = list(bin)
        for bit in range(len(bin)):
            if (bin[bit] == '0'):
                flipped[bit] = '1'
            else:
                flipped[bit] = '0'
        return "".join(flipped)


    def add_one(self, bin):
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

    def twos_comp_to_dec(self, two_comp):
        if two_comp[0] == '1':
            flipped = self.flipped_bits(two_comp)
            added = self.add_one(flipped)
            return '-' + self.bin_to_dec(added)
        else:
            return self.bin_to_dec(two_comp)

    def decimal_to_twos_comp(self, decimal):
        if (decimal[0] == '-'):
            bits = self.to_pad(self.decimal_to(decimal[1:len(decimal)],2))
            print('bits', bits)
            flipped = self.flipped_bits(bits)
            added = self.add_one(flipped)
            return added
        else:
            return self.to_pad(self.decimal_to(decimal,2))

    def convert(self):
        problem = self.row['problem']
        if self.row['description'] == 'dec' and self.row['todo'] == 'bin': #decimal to binary
            return self.to_pad(self.decimal_to(problem, 2))
        elif self.row['description'] == 'dec' and self.row['todo'] == 'hex': #decimal to hexadecimal
            return self.decimal_to('25', 16)
        elif self.row['description'] == 'dec' and self.row['todo'] == 'oct': #decimal to octal
            return self.decimal_to(problem, 8)
        elif self.row['description'] == 'bin' and self.row['todo'] == 'dec': #binary to decimal
            return self.bin_to_dec(problem)
        elif self.row['description'] == 'bin' and self.row['todo'] == 'hex': #binary to hexadecimal
            return self.bin_to_hex(problem)
        elif self.row['description'] == 'bin' and self.row['todo'] == 'oct': #binary to octal
            return self.bin_to_oct(problem)
        elif self.row['description'] == 'hex' and self.row['todo'] == 'bin': #hex to binary
            return self.hex_to_binary(problem)
        elif self.row['description'] == 'hex' and self.row['todo'] == 'dec': #hex to decimal
            return self.hex_to_decimal(problem)
        elif self.row['description'] == 'hex' and self.row['todo'] == 'oct': #hex to octal
            return self.hex_to_octal(problem)
        elif self.row['description'] == 'oct' and self.row['todo'] == 'bin': #oct to binary
            return self.octal_to_binary(problem)
        elif self.row['description'] == 'oct' and self.row['todo'] == 'dec': #oct to decimal
            return self.octal_to_decimal(problem)
        elif self.row['description'] == 'oct' and self.row['todo'] == 'hex': #oct to hexadecimal
            return self.octal_to_hex(problem)
        elif self.row['description'] == 'tcomp' and self.row['todo'] == 'dec': #tcomp to decimal
            return self.twos_comp_to_dec('1001')
        elif self.row['description'] == 'dec' and self.row['todo'] == 'tcomp': #decimal to decimal
            return self.decimal_to_twos_comp('-2')





# question = Questions(location = '../part0', filename= 'questions.csv')
# test = question.get(qid = 41)
# test['todo'] = 'tcomp'
# nc = NumberConverter()
# nc.set_row(test)
# print(nc.return_row())
# print(nc.convert())