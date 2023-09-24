import numpy as np

total_study_time = np.array([0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50,
                             2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50])
exam_result = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0,
                       1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

class LossFunction():
    def __init__(self):
        self.threshold = 0
        self.coefficient = 0
    
    def sigmoid(self,x):
        return 1 / (1+np.exp(-x))
    
    def predict(self, study_time):
        print(self.coefficient)
        print(type(self.coefficient))
        return self.sigmoid(self.coefficient * study_time - self.threshold)

    def value(self, threshold, coefficient):
        self.threshold = threshold
        self.coefficient = coefficient
        loss_sum = 0
        for i in range(len(total_study_time)):
            result = exam_result[i]
            study_time = total_study_time[i]
            loss_sum += (result - self.predict(study_time))**2
        return loss_sum
    
    def deriv(self, threshold, coefficient):
        self.threshold = threshold
        self.coefficient = coefficient
        self.derivative_threshold = 0
        self.derivative_coefficient = 0
        for i in range(len(total_study_time)):
            result = exam_result[i]
            study_time = total_study_time[i]
            self.derivative_threshold += 2 * (result - self.predict(study_time)) * self.predict(study_time) * (1 - self.predict(study_time))
            self.derivative_coefficient +=  -2 * (result - self.predict(study_time)) * self.predict(study_time) * (1 - self.predict(study_time)) * study_time
        return np.array([self.derivative_threshold, self.derivative_coefficient])