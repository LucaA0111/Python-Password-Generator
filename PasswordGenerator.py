import random
import string


def generatePassword():
       l = passwordLength()
       t = passwordType()
       password = ''

       if t == 1:
         i = 0
         while i < l:
            password += random.choice(string.digits)
            i += 1
         return password
       elif t == 2:
         i = 0
         while i < l:
              password += random.choice(string.ascii_letters)
              i += 1
         return password  
       elif t == 3:
         i = 0
         while i < l:
              password += random.choice(string.ascii_letters + string.digits + string.punctuation)
              i += 1
         return password
       else:
              password = "Valore non valido, inserire un valore valido"
              return password


def passwordType():
       while True:
            try:
              password_t = int(input("Sceglie la tipologia di password da generare: \n 1--> Solo numeri \n 2--> Solo lettere \n 3--> Lettere + Numeri + Simboli \n Tipologia: "))   
              if password_t < 1 or password_t > 3:
                 print("Valore non valido, inserisci un valore compreso tra 1 e 3!")
              else:
                 return password_t
            except ValueError:
              print("Valore non valido")
       

def passwordLength():
       while True:
           try:
              password_l = int(input("Inserisci la lunghezza della password: "))
              if password_l >= 8:
                     return password_l
              else:
                     print("Password troppo corta, inserisci un valore maggiore o uguale a 8:")
           except ValueError:
              print("Valore non valido")   



generated_password = generatePassword()

print(f"La tua password generata è: {generated_password}")