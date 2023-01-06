# try:
#   a = int(input('enter a number:'));
#   for i in range(1, 11):
#     print(f'{a} X {i} = {a*i}');
# except Exception as e:
#   print(e);

# try:
#   list = [21, 43, 65, 41];
#   num = int(input("enter a number:"));
#   # print(f'you have entered {num}')
#   print(list[num]);
# except ValueError:
#   print('The number you have entered is not an integer.');
# except IndexError:
#   print('The number is greater than list size.');

# try:
#   n = input('Enter a number: ');
#   print(n/3);
# except:
#   print('Error');
# finally:
#   print('This line will always get executed');

# **************************CUSTOM ERRORS**************************
A = int(input('Enter a  number: '));
if(A>5 or A<9):
  raise ValueError('value should be between 5 and 9');