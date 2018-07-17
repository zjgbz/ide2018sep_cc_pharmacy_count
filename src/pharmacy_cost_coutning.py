import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

drug_dict = {}
drug_list = []
drug_cost = []
drug_custmer_num = []
with open(input_filename, 'r') as f:
	content = f.readlines()
content = [x.strip() for x in content][1:]
for content_i in content:
	count_quotation = 0
	for char_i in range(len(content_i)):
		if content_i[char_i] == '"':
			count_quotation += 1
		if (count_quotation%2) and (content_i[char_i] == ","):
			content_i = content_i[:char_i] + "@" + content_i[char_i + 1:]
	temp_content = content_i.split(",")
	temp_key = temp_content[-2].replace("@",",")
	if temp_key not in drug_dict:
		drug_dict[temp_key] = []
	drug_dict[temp_key].append(float(temp_content[-1]))

for key in drug_dict:
	drug_list.append(key)
	drug_custmer_num.append(len(drug_dict[key]))
	drug_cost.append(sum(drug_dict[key]))

drug_num = len(drug_cost)
original_list_index = list(range(drug_num))
top_cost_list_index = list(reversed([x for _,x in sorted(zip(drug_cost,original_list_index))]))

sorted_drug_custmer_num = [drug_custmer_num[i] for i in top_cost_list_index]
sorted_drug_list = [drug_list[i] for i in top_cost_list_index]
sorted_drug_cost = [drug_cost[i] for i in top_cost_list_index]

with open(output_filename, 'w') as f:
	f.write("{0:s},{1:s},{2:s}\n".format("drug_name","num_prescriber","total_cost"))
	for i in range(drug_num):
		f.write("{0:s},{1:d},{2:.2f}\n".format(sorted_drug_list[i],sorted_drug_custmer_num[i],sorted_drug_cost[i]))
