import textfsm
from pprint import pprint

filename = "ex1_show_int_status.txt"
template = open("ex2test_show_int_status.tpl")



#read the file
with open(filename) as f:
    raw_text_data = f.read()   

re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(raw_text_data)
template.close()
print( ', '.join(re_table.header) )

'''
for row in fsm_results:
    print(row)
'''
listK = re_table.header
final_list = []
listV = fsm_results

# Given lists
print("List of K: ", listK)
for fsm_list in fsm_results:
    print("List of V : ", fsm_list)		
# Convert to dictionary
    fsm_dict = dict(zip(listK, fsm_list))
    final_list.append(fsm_dict)

print()
print("Dictionary from list :\n ",fsm_dict)

print("=" * 30)
print(final_list)
