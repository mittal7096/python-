with open('log_file') as f:
    chake=f.read()
if 'python'in chake.lower():
    print("python word is present in the log_file.")
else:
    print("python word is not present in the log_file.")