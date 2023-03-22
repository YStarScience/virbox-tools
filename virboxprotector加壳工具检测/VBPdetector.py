import tkinter as tk
from tkinter import filedialog
import platform
import os

# define function to read file and display it in listbox
def read_file():
    file_paths = filedialog.askopenfilenames()
    # Add file to listbox
    for file_path in file_paths:
        file_list.insert(tk.END, file_path)


def traverse_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # if not file.startswith('.'): # 忽略隐藏文件
            yield os.path.join(root, file)

def read_folder():
    folder_path = filedialog.askdirectory()
    # Add files to listbox
    # folder_file_list = glob.glob(os.path.join(folder_path, "*.*"))
    
    
    for file_path in traverse_files(folder_path):
        file_list.insert(tk.END, file_path)

# define function to clear listbox
def clear_list():
    file_list.delete(0, tk.END)

# # define function to check characters 41-44 in selected file
# def check_sens_win():
#     for index in range(file_list.size()):
#         file_path = file_list.get(index)
#         with open(file_path, "rb") as f:
#             content = f.read()
#             # Check if bytes 41-44 are "SENS"
#             if content[40:44] == b"SENS":
#                 file_list.itemconfig(index, bg="green")
#             else:
#                 file_list.itemconfig(index, bg="red")

def check_sens():
    for index in range(file_list.size()):
        file_path = file_list.get(index)
        with open(file_path, 'rb') as file:
            data = file.read()
            if(data[0:4]==b"\x7fELF" and  b"Virbox Protector" in data )or data[40:44] == b"SENS":
                file_list.itemconfig(index, bg="green")
                # print("File contains 'Virbox Protector'")
            else:
                file_list.itemconfig(index, bg="red")
                # print("File does not contain 'Virbox Protector'")


# if platform.system() == "Windows":
#     def check_sens():
#         # Call Windows-specific function
#         check_sens_win()
# else:
#     def check_sens():
#         # Call Linux-specific function
#         check_sens_linux()

                
if __name__=='__main__':
    # create main window and listbox
    root = tk.Tk()
    root.title("Virbox加壳检测工具")

    left_frame = tk.Frame(root, bg="grey", width=100, height=300)
    left_frame.pack(side="left", fill="y")
    # create buttons and add to main window
    button1 = tk.Button(left_frame, text="读取文件", command=read_file)
    button1.pack( fill=tk.X)
    button2 = tk.Button(left_frame, text="读取文件夹", command=read_folder)
    button2.pack( fill=tk.X)
    button3 = tk.Button(left_frame, text="清空列表", command=clear_list)
    button3.pack( fill=tk.X)
    button4 = tk.Button(left_frame, text="检测加壳", command=check_sens)
    button4.pack( fill=tk.X)
    info_text='''本工具只检测VirboxProtector加壳后的可执行程序，对jar、app等压缩包不提供检测！
    如果您觉得好用，可以提交赞赏，谢谢！！！'''
    info = tk.Label(left_frame,text=info_text)
    info.pack(fill="both",expand=True)

    file_list = tk.Listbox(root, width=50, height=20)
    file_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # start main loop
    root.mainloop()
