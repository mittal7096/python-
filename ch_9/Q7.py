chake=True
i=1
with open('log_file') as f:
    while chake:
        chake=f.readline()
        if 'python' in chake.lower():
            print(chake)
            print("python word is present in the log_file.line number:-",i)
        else:
            print('python word is not present in the log_file.')
        i+=1