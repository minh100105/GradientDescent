import matplotlib.pyplot as plt
import numpy as np
from math_function import LossFunction
from function_plot import plot_function_contour, plot_changes
from utilis import clear_graph_folder, create_gifs
import math


def gradient_descent_process(starting_point_threshold, starting_point_coefficient, learning_rate, precision, max_iterations):
    clear_graph_folder()

    threshold_old = starting_point_threshold
    coefficient_old = starting_point_coefficient

    i = 0

    f = LossFunction()

    threshold = np.linspace(-5, 5, 100)
    coefficient = np.linspace(-5, 5, 100)

    plot_function_contour(f, threshold, coefficient)


    while True:

        print("Iteration:", i)

        print("threshold_old:", threshold_old)

        print("coefficient_old:", coefficient_old)
        coefficient_gradient = f.deriv(threshold_old, coefficient_old)[0]
        threshold_gradient = f.deriv(threshold_old, coefficient_old)[1]
        

        print("threshold_gradient:", threshold_gradient)
        print("coefficient_gradient:", coefficient_gradient)

        coefficient_new = coefficient_old - (coefficient_gradient * learning_rate)
        threshold_new = threshold_old - (threshold_gradient * learning_rate)  


        print("threshold_new:", threshold_new)
        print("coefficient_new:", coefficient_new)
        print("lossfunction: ", f.value(threshold_new, coefficient_new))
        

        plot_changes(f, threshold, threshold_old, threshold_new, coefficient_old, coefficient_new, "" + str(i))

        if math.sqrt((threshold_new - threshold_old)**2 + (coefficient_new - coefficient_old)**2) < precision:
            print("Precision reached!")
            break

        if i > max_iterations:
            print("Maximum iterations exceeded!")
            break

        threshold_old = threshold_new
        coefficient_old = coefficient_new

        i += 1

    create_gifs()


gradient_descent_process(0.5, 0.5, 0.5, 0.0001, 150)