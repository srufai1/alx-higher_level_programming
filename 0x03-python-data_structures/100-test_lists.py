import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
len1 = ['hello', 'World']
lib.print_python_list_info(len1)
del len1[1]
lib.print_python_list_info(len1)
len1 = len1 + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(len1)
len1 = []
lib.print_python_list_info(len1)
len1.append(0)
lib.print_python_list_info(len1)
len1.append(1)
len1.append(2)
len1.append(3)
len1.append(4)
lib.print_python_list_info(len1)
len1.pop()
lib.print_python_list_info(len1)
