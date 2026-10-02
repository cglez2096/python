


card_number = "4347691129246203"
odd_sum = 0
double_list = []
even_sum = 0

number = list(card_number)

for (idx,val) in enumerate(number):
    if idx % 2 != 0:
        odd_sum = odd_sum + int(val)
       
    else:
        double_list.append(int(val)*2)

        

##CONVERTING LIST INTO A STRING
double_string =""
for x in double_list:
    double_string += str(x)

#CONVERTING THE STRING BACK TO A LIST
double_list =list(double_string)

for x in double_list:
    even_sum += int(x)

net_sum = even_sum + odd_sum

if net_sum % 10 == 0:
    print("VALID CARD")

else:
    print("INVALID CARD")







