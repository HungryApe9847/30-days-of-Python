from sklearn.linear_model import LinearRegression

X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [2, 5, 6, 8, 8.5, 8.5, 8.5, 8, 6, 5, 4]

model = LinearRegression().fit(X, y)
time_spent = float(input('Input the hours spent studying: '))
result = model.predict([[time_spent]])
result = str(result)
result = result.replace("[", "")
result = result.replace("]", "")
result = float(result)
result = round(result)
message = f"On average, a student will most likely recieve a {result}"
print(message)