import re 

senha_forte_regexp = re.compile(
      r'^'
      r'(?=.*[a-z])'
      r'(?=.*[A-Z])'
      r'(?=.*[0-9])'
      r'(?=.*[ -\/:-@[-`{-~])'
      r'.{12,}'
      r'$',
      flags=re.M
      )

senhas = '''
VÁLIDAS
Pp5="V/Hdm92zx3
W7u8~swT*0P,asd
@kvfT#\B7F90
IPt1]q;40fF~
3?(e8}MQ0uZc

SEM MINÚSCULAS
9Y;^0J*A8F~9
7K|->O)7V2V6
37_^]V}VB3T8
BN48EW~8}~\7
G]A7@1UX06\^

SEM MINÚSCULAS E NÚMEROS
|]MAM@-T>K=Q
XH*!}A~\IK>B
Y{EAJ|_HV_;}
Z}A__D@OK|O|
*=V`?S^R}EPD

SEM NÚMEROS CARACTERES E MINÚSCULAS
CNSLDAGWNORN
BGZZaYRUKHFY1
OOADJGWYDOUJ
XVFISGHYLAMI
HHZPSHFYDMBB

QUANTIDADE INVÁLIDA (6)
04w}wQ
9di{9T
dr13C-
<l0dO112'312adaq
8So`y6
'''

print(senha_forte_regexp.findall(senhas))