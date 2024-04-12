"""Evaluating algorithms!"""
__author__ = "730468225"


import matplotlib.pyplot as plt
from runtime_analysis_functions import evaluate_runtime, evaluate_memory_usage

START_SIZE: int = 0
END_SIZE: int = 1000

# Selection Sort graph 
times_selection_sort = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times_selection_sort)
plt.title("Runtime Analysis of Selection Sort - hajnaloc")
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.show()

# Insertion Sort graph 
times_insertion_sort = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
plt.plot(times_insertion_sort)
plt.title("Runtime Analysis of Insertion Sort - hajnaloc")
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.show()

# Memory Usage Analysis
usage_selection_sort = evaluate_memory_usage("selection_sort", START_SIZE, END_SIZE)
plt.plot(usage_selection_sort)
plt.title("Memory Usage Analysis of Selection Sort - hajnaloc")
plt.xlabel("Input Size")
plt.ylabel("Memory Usage (bytes)")
plt.show()

usage_insertion_sort = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage_insertion_sort)
plt.title("Memory Usage Analysis of Insertion Sort - hajnaloc")
plt.xlabel("Input Size")
plt.ylabel("Memory Usage (bytes)")
plt.show()