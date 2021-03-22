import re as pintinho

cpfs = '123.123.123-23'

print(pintinho.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpfs))
print(pintinho.findall(r'(^(?:\d{3}\.){2}\d{3}(?:-\d{2})$)', cpfs))
eita = pintinho.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

# print(eita.search(cpfs))

# maneira mais clara e mais precisa
# ip_reg_exp = pintinho.compile(r'''
#       ^
#       (?:
#             25[0-5]| # de 250-255
#             2[0-4][0-9]| # de 200-249
#             1[0-9]{2}| # de 100-199
#             [1-9][0-9]| # de 10-99
#             [0-9] # de 0-9
#       )
#       \.
#       (?:
#             25[0-5]| # de 250-255
#             2[0-4][0-9]| # de 200-249
#             1[0-9]{2}| # de 100-199
#             [1-9][0-9]| # de 10-99
#             [0-9] # de 0-9
#       )
#       \.
#       (?:
#             25[0-5]| # de 250-255
#             2[0-4][0-9]| # de 200-249
#             1[0-9]{2}| # de 100-199
#             [1-9][0-9]| # de 10-99
#             [0-9] # de 0-9
#       )
#       \.
#       (?:
#             25[0-5]| # de 250-255
#             2[0-4][0-9]| # de 200-249
#             1[0-9]{2}| # de 100-199
#             [1-9][0-9]| # de 10-99
#             [0-9] # de 0-9
#       )
#       $
# ''', flags=pintinho.X)

ip_reg_exp = pintinho.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$')   


for i in range(301):
      ip = f'{i}.{i}.{i}.{i}'
      print(ip, ip_reg_exp.findall(ip))