# code by Alaa Dawoud

class OR():
	def __init__(self, w_1=0.3, w_2=-0.1,
	 				threshold_theta = 0.2, learning_rate_alpha = 0.1):
		# tuple (0, 0, 0) is x_1, x_2, output respectivly
		self.truth_table = ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1))
		self.desirable = (0, 1, 1, 1)
		self.threshold_theta = threshold_theta
		self.learning_rate_alpha = learning_rate_alpha
		self.w_1 = w_1
		self.w_2 = w_2
	def train(self, epochs=1):
		for epoch in range(epochs):
			print(f'for epoch {epoch + 1} ')
			print('___')
			for i in range(2):
				for j in range(2):
					y_actual = self.actual_output(self.w_1, self.w_2, x_1=i, x_2=j)
					# look for y_desired in the turth table using i and j
					# i for x and j for y
					# using list comprehension and [0] to get the element from the list
					y_desired = [x[2] for x in self.truth_table if x[0:2] == (i, j)][0]

					print('y_actual and desired and weights befor error and update for x = {}, y = {}'.format(i,j))
					self.test(y_actual, y_desired, self.w_1, self.w_2)
					
					# calculate the error and from the error function update the weights
					err = self.error(y_desired = y_desired, y_actual=y_actual,
						x=i, y=j)

					print('y_actual and desired and weights after error and update for x = {}, y = {}, and ERROR = {}'.format(i,j, err))
					self.test(y_actual, y_desired, self.w_1, self.w_2)
			print(f'End of epoch {epoch + 1}')
			print('-----------------------------------------------------')


	def test(self, y_actual, y_desired, w_1, w_2):
		print('y_actual is : ', y_actual)
		print('y_desired is : ', y_desired)
		print('w_1 is : ', w_1)
		print('w_2 is : ', w_2)
	def actual_output(self, w_1, w_2, x_1, x_2):
		out = x_1*w_1 + x_2*w_2 - self.threshold_theta
		if out >= 0:
			return 1
		else:
			return 0

	def updata_weight(self, error, x, y):
		delta_w_1 = self.learning_rate_alpha * x * error
		delta_w_2 = self.learning_rate_alpha * y * error
		self.w_1 = self.w_1 + delta_w_1
		self.w_2 = self.w_2 + delta_w_2

	def error(self, y_desired, y_actual, x, y):
		err = y_desired - y_actual
		if err == 0:
			return 0
		else:
			self.updata_weight(err, x, y)
			return err

model = OR()
model.train(epochs=4)