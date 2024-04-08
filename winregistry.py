import winreg as reg

# key_path = r"Directory\\Background\\shell"
# command_key_path = r"Directory\\Background\\shell\\Split PDF\\command"

key_path = r"*\\shell"
command_key_path = r"*\\shell\\Split PDF\\command"

key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path)

reg.SetValue(key, "", reg.REG_SZ, "Split PDF")
# reg.SetValueEx(key, "Icon", 0, reg.REG_SZ, "python C:\\Users\\ismail\\dev\\side-projects\\pdf-merge-split\\split.py %1")

reg.SetValue(command_key, "", reg.REG_SZ, "python C:\\Users\\ismail\\dev\\side-projects\\pdf-merge-split\\split.py %1")