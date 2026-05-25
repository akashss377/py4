web_dev=['remya','arya','soorya']
data_science=['akash','athul','akthar']
ui_ux=['rahna','ashik','navanith']
all_participants = [web_dev,data_science,ui_ux]
web_dev.append("arun")
print(web_dev)
data_science.insert(1,"arjun")
print(data_science)
ui_ux.pop()
print(ui_ux)
new_data_science = data_science.copy()
data_science.clear()
print(new_data_science)
print(web_dev[:2])
name_len = [len(name)for name in new_data_science]
print(name_len)
if "asha" in all_participants :
    print("yes, asha in the  list")
else:
    print("no, asha not in the list ")
first_participant = (web_dev[0],new_data_science[0],ui_ux[0])
print(first_participant)