import cv2
import numpy as np
import matplotlib.pyplot as plt

class RealTimeImageProcessor:
	def __init__(self,camera_ind):
		assert (camera_ind), "camera id must be provided"
		self.camera_index = camera_ind
		self.camera = cv2.VideoCapture(self.camera_index)
		self.process = (lambda x: x)
		self.listener = None

	def set_process_function(self,func):
		self.process = func

	def set_key_listener(self,listener):
		self.listener = listener

	def run(self, win_name, break_key = None):
		assert (win_name is not None), "window name must be provided for run()"
		while True:
			self.window = cv2.namedWindow(win_name)
			r,img = self.camera.read()
			if self.listener:
				cv2.setMouseCallback(win_name,self.listener,img)
			result = self.process(img)
			cv2.imshow(win_name,result)
			c = cv2.waitKey(10)
			if c == break_key and break_key is not None:
				break

rip = RealTimeImageProcessor(1)
rip.set_process_function(lambda x: cv2.cvtColor(x,cv2.COLOR_BGR2GRAY))
rip.run("test")
