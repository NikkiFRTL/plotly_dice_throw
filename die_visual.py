from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout


# Create a die object.
die = Die()

# Modeling throws and saving its values in a list.
results = []
for num in range(1000):
    roll = die.roll()
    results.append(roll)

# Analysis of the results
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Data visualisation via plotly.
x_values = list(range(1, die.num_sides+1))

# List of sides of a die - x axis, frequencies - y axis. Bar - type of diagram.
data = [Bar(x=x_values, y=frequencies)]

# Name the axises.
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

# Layout of the Bar diagram
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config,
                   yaxis=y_axis_config)

# Building the diagram
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
