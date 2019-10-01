cost_vector = list(map(int,input("Enter cost coefficients: ").split()))
initial_cost_vector_length = len(cost_vector)
number_of_constraints = int(input("Enter number of constraints: "))
total_constraints_length = len(cost_vector)+number_of_constraints
coefficients_matrix = list()
print("Enter coefficients: ")

identity_matrix = []

for i in range(number_of_constraints):
	identity_matrix.append([0]*number_of_constraints)
#print(identity_matrix)
j=0
for i in range(number_of_constraints):
	l = list(map(int,input().split()))
	coefficients_matrix.append(l)
	cost_vector.append(0)
	identity_matrix[j][j] = 1
	coefficients_matrix[-1].extend(identity_matrix[j])
	j+=1


constraints_vector = list(map(int,input("Enter constraints: ").split()))

for i in range(number_of_constraints):
	coefficients_matrix[i].append(constraints_vector[i])

objective_value_function = input("Enter objective value function: ")

if objective_value_function=='maximization':
	for i in range(total_constraints_length):
		print(i)
		cost_vector[i]= 0 - cost_vector[i]

coefficients_matrix.append(cost_vector)
coefficients_matrix[-1].append(0)
basic_variables = []

for i in range(number_of_constraints):
	basic_variables.append(len(identity_matrix[0])+i)


row_length = len(coefficients_matrix[0])-1

unable_to_find_leaving_variable = 0
unable_to_find_entering_variable = 0

while True:
	maximum=0
	q = None
	for i in range(total_constraints_length):
		if coefficients_matrix[-1][i]!=0 and maximum>coefficients_matrix[-1][i]:
			maximum = coefficients_matrix[-1][i]
			q = i
	#print(rj_values)
	if q==None:
		# print("q breaking")
		unable_to_find_entering_variable=1
		break

	s = 1000000
	p = None
	for i in range(number_of_constraints):
		if coefficients_matrix[i][q]!=0:
			k = coefficients_matrix[i][-1]/coefficients_matrix[i][q]
			if k>0 and s>k:
				s=k
				p=i
	#print(optimum_value)
	if p==None:
		# print("p breaking")
		unable_to_find_leaving_variable=1
		break
	#print(p,q)
	pivot = coefficients_matrix[p][q]
	#print(pivot)
	for i in range(total_constraints_length+1):
		coefficients_matrix[p][i] = coefficients_matrix[p][i]/pivot


	for i in range(number_of_constraints+1):
		temp = []
		for j in range(total_constraints_length+1):
			if i!=p:
				#print(coefficients_matrix[i][j])
				temp.append(coefficients_matrix[i][j] - ((coefficients_matrix[i][q]/coefficients_matrix[p][q])*coefficients_matrix[p][j]))
				#print(coefficients_matrix[i][j])
		#print(temp)
		if i!=p:
	 		coefficients_matrix[i] = temp
	# for i in range(number_of_constraints+1):
	# 	for j in range(total_constraints_length+1):
	# 		print(coefficients_matrix[i][j],end=" ")
	# 	print()
	# print()
	basic_variables[p]=q
	#print(basic_variables,p,q)


print(basic_variables)
if unable_to_find_leaving_variable==1 and any([i for i in coefficients_matrix[-1] if i<0]):
	print("unboundedness")
elif unable_to_find_entering_variable==1 and all([i for i in coefficients_matrix[-1] if i>=0]) and all([i for i in basic_variables if i<initial_cost_vector_length]):
	print("infeasible")
else:
	d = {}
	for i in range(total_constraints_length):
		d["x"+str(i)]=0
	for i in range(number_of_constraints):
		d["x"+str(basic_variables[i])] = coefficients_matrix[i][-1]
		#print(coefficients_matrix[i][-1])
	print(d)
	print("optimum value: "+str(coefficients_matrix[-1][-1]))




