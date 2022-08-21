import os
import pyautogui
import cv2

folder_icon = u'\U0001F4D2'
file_icon = u'\U0001F4C3'

def get_system_info():
	return os.uname()

def get_current_directory():
	return os.getcwd()

def get_files(path):
	files = os.listdir(path)
	sorted_files_dirs = parse_files(files, path)

	return sorted_files_dirs

def change_dir(path):
	check = os.path.exists(path)

	if check:
		check = path

	return check


def parse_files(files, path):
	result = ''

	for obj in files:
		if os.path.isdir(path + '/' + obj):
			folder_with_icon = folder_icon + ' ' + obj + '\n'
			result += folder_with_icon

		elif os.path.isfile(path + '/' + obj):
			file_with_icon = file_icon + ' ' + obj + '\n'
			result += file_with_icon

		else:
			file_with_icon = file_icon + ' ' + obj + '\n'
			result += file_with_icon

	return result

def make_screenshot():
	screen = pyautogui.screenshot('screenshot.png')

	return screen

def make_webcam_photo():
	cap = cv2.VideoCapture(0)

	for i in range(10):
		cap.read()

	ret, frame = cap.read()

	cv2.imwrite('cam.png', frame)

	cap.release()