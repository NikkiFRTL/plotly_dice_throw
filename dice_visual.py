from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout


# Создание кубика D6
die_1 = Die()
die_2 = Die()

# Model of two dice throws with saving the results it in a list
results = []
for num in range(1000):
    roll = die_1.roll() + die_2.roll()
    results.append(roll)

# Analysis of the results.

# Making a list of frequencies.
max_possible_result = die_1.num_sides + die_2.num_sides
frequencies = [(results.count(value)) for value in range(2, max_possible_result+1)]

# Data visualisation via plotly.
x_values = list(range(2, max_possible_result+1))

# List of sides of a die - x axis, frequencies - y axis. Bar - столбцевая диаграмма.
data = [Bar(x=x_values, y=frequencies)]

# Name the axises. 'dtick' is a key to enumerate each column with a step(1).
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

# Layout of the Bar diagram - макет(оформление страницы).
my_layout = Layout(title='Results of rolling two D6 1000 times',
                   xaxis=x_axis_config,
                   yaxis=y_axis_config)

# Building the diagram.
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
