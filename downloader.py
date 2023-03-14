import urllib.request , sys ,os
if os.name == 'nt':
  os.system('color') #windows only
tm_size = os.get_terminal_size()
progress = ['|','/','-','\\','|','/','-','\\']
progress_counts = 0

print("\033[38;2;0;255;0m===downloder===\033[38;2;255;255;255m")
def progress_print(block_count, block_size, total_size):
  global progress_counts
  progress_counts += 0.001
  percentage = 100.0 * block_count * block_size / total_size
  if percentage >= 100:
    percentage = 100
    block_count = total_size
    block_size = 1
  text = str(f"{percentage:.2f}% ( {block_count *block_size:,}/{total_size:,} B - {total_size / 1048576:.2f} MB )")
  max_bar = tm_size.columns - len(text) - 3
  bar_num = int(percentage / (100 / max_bar))
  progress_element = '█' * bar_num
  if bar_num != max_bar:
    progress_element += progress[int(progress_counts % 8)]
  bar_fill = '_' 
  bar = progress_element.ljust(max_bar, bar_fill)
  print(f'\033[38;2;0;230;255m|{bar}| \033[38;2;0;255;100m{text}\033[38;2;255;255;255m\r',
    
    end='')

def download(url, filepath_and_filename):
  
  print('\033[38;2;0;255;255m start download from:\033[38;2;255;255;255m', end="")
  print(f"{url}\n")
  urllib.request.urlretrieve(url, filepath_and_filename, progress_print)
  print('') 
  print(end="")

intrd_count = len(sys.argv)
if 2 > intrd_count:
  url= input("\033[38;2;0;230;255mURLをどぞ>>\033[00m")
else:
  url = sys.argv[1]
if 3 > intrd_count:
  filepath_and_filename= input("\033[38;2;0;230;255mファイル名をどぞ>>\033[00m")
else:
  filepath_and_filename =  sys.argv[2]
download(url, filepath_and_filename)
print(f"\n\033[38;2;0;255;mdone!!終わったよー \033[38;2;0;255;255m{url}\033[38;2;255;255;255m  to  \033[38;2;255;100;100m{filepath_and_filename} \033[38;2;0;255;mdownloded\033[38;2;255;255;255m") 
os.system('PAUSE')
