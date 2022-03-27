import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 

dice_result = []

df = pd.read_csv("data.csv")
data = df ["reading score"].tolist()

mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)
standard_deviation = statistics.stdev(data)
print("Mean:",mean)
print("Median:",median)
print("Mode:",mode)
print("Standard Deviation:", standard_deviation)

first_standarddeviation_start, first_standarddeviation_end = mean - standard_deviation, mean + standard_deviation
second_standarddeviation_start, second_standarddeviation_end = mean - (2*standard_deviation), mean + (2*standard_deviation)
third_standarddeviation_start, third_standarddeviation_end = mean - (3*standard_deviation), mean + (3*standard_deviation)

fig = ff.create_distplot([data], ["result"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_standarddeviation_start, first_standarddeviation_start], y = [0,0.15],mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [first_standarddeviation_end, first_standarddeviation_end], y = [0,0.15],mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [second_standarddeviation_start, second_standarddeviation_start], y = [0,0.15],mode = "lines", name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [second_standarddeviation_end, second_standarddeviation_end], y = [0,0.15],mode = "lines", name = "Standard Deviation 2"))
fig.show()

standard_deviation1 = [result for result in data if result > first_standarddeviation_start and result < first_standarddeviation_end]
standard_deviation2 = [result for result in data if result > second_standarddeviation_start and result < second_standarddeviation_end]
standard_deviation3 = [result for result in data if result > third_standarddeviation_start and result < third_standarddeviation_end]

print("{}% of data lies within first standard deviation".format(len(standard_deviation1)*100.0/len(data)))
print("{}% of data lies within second standard deviation".format(len(standard_deviation2)*100.0/len(data)))
print("{}% of data lies within third standard deviation".format(len(standard_deviation3)*100.0/len(data)))





