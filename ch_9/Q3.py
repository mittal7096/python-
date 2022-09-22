'''write a program to generate multiplication tables from 2 to 20 and write it to the deifferent files.
place thes files in a folder for a 13-years old.'''

for i in range(1,21):
    with open(f"table/Multiplication_table_of_{i}.txt", 'a') as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}")
            if j>10:
                i=i+1
            elif j!=10:
                f.write('\n')


# '''write a program to generate multiplication tables from 2 to 20 and write it to the deifferent files.
# place thes files in a folder for a 13-years old.'''
#
# for i in range(2, 21):
#     with open(f"table/Multiplication_table_of_{i}.txt", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i}X{j}={i*j}")
#             if j!=10:
#                 f.write('\n')
