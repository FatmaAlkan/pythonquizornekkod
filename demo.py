import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

        

class UserRepsitory:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False     #log in olup olmadığını tutmak için
        self.currentUser = {}

        # .json dosyasından dosyaları aktarmak
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):     #json dosyası var mı yok mu (true false döndürür)
            with open('users.json','r', encoding= 'utf-8') as file :
                users = json.load(file)       #json.load okuma işlevi
                for user in users :
                    user = json.loads(user)     #json dic dönüşürdük
                    newUser = User (username=user['username'], password= user['password'], email= user['email'])
                    self.users.append(newUser)

            print(self.users)

    def register(self, user: User ):
        self.users.append(user)
        self.savetoFile()
        print ("Kullanici Olusturuldu...")
    
    def login(self, username, password):

        for user in self.users :
            if user.username == username and user.password == password :
                self.isLoggedIn = True
                self.currentUser = user
                print('login yapildi')
                break

    def logout (self) :
        self.isLoggedIn = False
        self.currentUser = {}
        print('cikis yapildi')

    def identity(self):
        if self.isLoggedIn:
            print(f'username : {self.currentUser.username}')
        else: 
            print('giris yapilmadi')

    def savetoFile(self):
        list = []

        for user in self.users :
            list.append(json.dumps(user.__dict__))

        with open ('users.json', 'w') as file:
            json.dump(list, file) #use.json dosyası içerisine self.user objesini kayıt ederiz


repository = UserRepsitory()    #uygulamayı kullandığım sürece aynı nesneyi hedef alması için

while True:     #sonsuz döngü
    print("menu".center(50, '*'))
    secim = input('1-Register \n2-Login \n3-Logout \n4-Identity \n5-Exit \nSeciminiz:  ')
    
    if secim == '5':
        break
    else :
        if secim == '1':    #register
            username = input("username : ")
            password = input ("password : ")
            email = input ("email : ")

            user = User ( username=username, password=password, email=email)
            repository.register(user)       #oluşturduğumuz user bilgisini aktarırız 

        elif secim == '2':  #login
            if repository.isLoggedIn :
                print('giris daha onceden yapildi')
            else:
                username = input ('username : ')
                password = input ('password: ')

                repository.login(username, password)

        elif secim == '3':  #logout
            repository.logout()

        elif secim == '4':  #dislay username
            repository.identity()
        else:   #
            print("Hatali Secim")

