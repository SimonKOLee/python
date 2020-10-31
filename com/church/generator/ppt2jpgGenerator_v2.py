from path import Path
import os
import win32com.client
import shutil
import glob

default_folder_path = os.getcwd()
ppt_files = glob.glob('./*.ppt')
pptx_files = glob.glob('./*.pptx')
ppt_folder_path = input('請輸入PPT檔案絕對路徑(默認路徑:'+default_folder_path+'):')
# print(os.listdir(default_folder_path))
print('\n'+default_folder_path + '的PPT 檔案如下:')
print(ppt_files)
print(pptx_files)
ppt_filename = input('請輸入PPT檔案名字(e.g ‘詩歌.ppt’ 請輸入 ‘詩歌’)(默認ALL):')
saveppt_ind = input('是否需要儲存PPT為JPG(Y/N) (默認Y):')
rename_ind = input('是否需要重命名(Y/N) (默認Y):')


def ppt2jpg():
	if ppt_filename == '':
	   ppt_full_paths = [Path(file).abspath() for file in ppt_files]
	   pptx_full_paths = [Path(file).abspath() for file in pptx_files]
	   full_paths = ppt_full_paths + pptx_full_paths
	   print("處理所有文件 ", len(full_paths))
	   for path in full_paths:
		   process(path)
	   return
		
	ppt_full_path = getFilePath(ppt_folder_path, ppt_filename)
	process(ppt_full_path)

def process(ppt_full_path):
	if ppt_full_path == '':
	   print('Invalid file path!')
	   return

	print('file path: '+ppt_full_path)
	if 'Y' == saveppt_ind.upper() or '' == saveppt_ind.upper():
		save2Jpg(ppt_full_path)
	else:
		print('skip saving ppt to JPG')
	if 'Y' == rename_ind.upper() or '' == rename_ind.upper():
		generate_filename(ppt_full_path)
	else:
		print('skip re-generating filenames')


def getFilePath(ppt_path, ppt_filename):
	if ppt_path != '':
		output_path = ppt_path + '\\' + ppt_filename
	else:
		output_path = default_folder_path + '\\' + ppt_filename

	if os.path.isfile(output_path):
		return output_path

	if os.path.isfile(output_path+'.ppt'):
		return output_path+'.ppt'

	if os.path.isfile(output_path+'.pptx'):
		return output_path+'.pptx'
	print('PPT file not exists: '+output_path)
	return ''


def save2Jpg(output_path):
	picture_path = output_path[:output_path.rfind('.')]
	if picture_path != '':
		print("remove old folder: "+picture_path)
		remove_files(picture_path)
	ppt_app = win32com.client.Dispatch('PowerPoint.Application')
	ppt_app.Visible = True
	ppt = ppt_app.Presentations.Open(output_path)  # start PowerPoint
	ppt.SaveAs(output_path, 17)  # 17 is the number to save as jpg file type
	ppt_app.Quit()  # close PowerPoint
	print('保存成功!')


def generate_filename(output_path):
	picture_path = output_path[:output_path.rfind('.')]
	n = 0
	for file in os.listdir(picture_path):
		originalFileName = ''.join(filter(str.isdigit, file))
		# print(originalFileName)
		fileName = '{:03d}'.format(int(originalFileName))
		os.rename(os.path.join(picture_path, file),
				  os.path.join(picture_path, fileName + '.jpg'))
		n += 1
	print('重命名成功!')


def remove_files(folder):
	if os.path.isdir(folder) != True:
		return
	for filename in os.listdir(folder):
		file_path = os.path.join(folder, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))


ppt2jpg()  # call the function
