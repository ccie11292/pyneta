import textfsm
from pprint import pprint

text_file = "lab4-2_show_int_status.txt"
template_file = "lab4-2_show_int_status.tpl"


with open(text_file) as f:
    show_int_status = f.read()


with open(template_file) as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(show_int_status)

print(fsm.header)
pprint(result)
print()

table_keys = fsm.header
final_list=[]

for fsm_list in result:
    fsm_dict = dict(zip(table_keys, fsm_list))
    final_list.append(fsm_dict)

print()
pprint(final_list)
print() 
