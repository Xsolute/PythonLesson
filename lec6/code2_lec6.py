'''
while True:
    a = input()
    if a == 'quit':
        exit()
    elif a == 'skip':
        print('rejected\n----------')
    else:
        print('{}\n----------'.format(a))
'''

# skip�� �����ϴ� ���ڿ��� ��� rejected�� ����ϰ�
# ���м��� ������� �ʴ� �Լ�
def print_without_skip(string):
    if 'skip' in string:
        print('rejected')
        return
    else:
        print(string)
    print('-' * 10)

# quit�� �Է��� ������ �ݺ��Ͽ� ����� �Է��� ����
user_input = ' '
while user_input != 'quit':
    user_input = input('input: ')
    print_without_skip(user_input)

