import vowpalwabbit

# creating an instance
model = vowpalwabbit.Workspace(quiet = True)
if model:
    print("Hello World, Vowpal Wabbit has started to make predictions")
    print()

train_model = [
    "0 | price:.23 sqft:.25 age:.05 2006",
    "1 | price:.18 sqft:.15 age:.35 1976",
    "0 | price:.53 sqft:.32 age:.87 1924",
]

for example in train_model:
    model.learn(example)

test_example = "| price:.35 sqft:.10 age:.10 2020"

predict = model.predict(test_example)

print(predict)
# the model predicts a value of 0.03800103813409805, requirement of a new roof
