import os

MAX_SPLIT_SIZE = 10 #Mb

class FileHandler():

	def __init__(self,path,file):
		self.path = path
		self.file = file
		self.index = 0

	def zip_and_split(self):
		os.system(f"gzip -c {self.path}{self.file} | split -b {MAX_SPLIT_SIZE}000000 - {self.path}node1_audio_compressed.gz")
		self.index += 1

	def remove(self,chunk):
		os.system(f"rm -f {chunk}")