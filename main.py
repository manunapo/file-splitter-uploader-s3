import os
from filehandler import FileHandler
from awshandler import AWShandler

PATH = "./to_upload/"

#	Will use whis 140Mb file because was told to me that the Audio files
# 	were avg 100Mb
file_name = 'jdk-7u181-windows-x64.exe'



file_handler = FileHandler(PATH, file_name)

# 	splitting and zipping file into several
file_handler.zip_and_split()

#	initializing AWS conection/handler
aws_handler = AWShandler()

#	main loop, get every chunk of the splitted original file and upload it to S3
if __name__ == '__main__':
	print("Starting uploading files...")
	for file in os.listdir(f"{PATH}"):
		if file.endswith(".gz",-5,-2):
			file_to_upload = os.path.join(f"{PATH}", file)
			print(f'File: {file_to_upload}')
			aws_handler.upload_file(file_to_upload,'upload-audio-files-test',file_to_upload[2:])
			print()
			#	file_handler.remove() not implemented, it is straigh-fordward.
			#	Main idea working