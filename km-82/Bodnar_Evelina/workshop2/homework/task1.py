"""
написати рекурсивну функцію з даними
food (name, price)
"""
dataset = {
	"bob@kpi.ua": {
					"person": {
								"name": "Bob",
								"email": "bob@kpi.ua"
					},
					"foods": {
								"apple": [1.3, 12.1],
								"milk": [45]
					}
	},

	"boba@kpi.ua": {
					"person": {
								"name": "Boba",
								"email": "boba@kpi.ua"
					},
					"foods": {"milk": [45]}
	}
}

def names (dataset, emails, nameList):
	if len (dataset) == len (nameList):
		return nameList
	nameList.append(dataset[emails[0]]["person"]["name"])
	emails.pop(0)
	return names(dataset, emails, nameList)

nameList = []
emails = []
for i in dataset:
	emails.append(i)
print(names(dataset, emails, nameList))


def  food_list(dataset, food_set = {}):
	for key in dataset:
		for elm in dataset[key]["foods"]:
			try:
				times = food_set[elm]
			except KeyError:
				print('You are not right.Please try again')
			food_set[elm] = times + len(dataset[key]["foods"][elm])
	return food_set

print(food_list(dataset, food_set = {}))

food_list(dataset)

def spent(dataset):
	result = {}
	for key in dataset:
		food = dataset[key]["foods"]
		summa = 0
		result_key = dataset[key]["person"]["name"]
		for item in food:
			summa += sum(food[item])
			result[result_key] = summa
	return result

print(spent(dataset))



#TODO