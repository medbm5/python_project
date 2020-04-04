from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.button import ButtonBehavior
from kivy.properties import ObjectProperty, StringProperty
from add_product import post,get
from kivymd.uix.label import MDLabel
from kivymd.theming import ThemeManager
from kivy.uix.image import Image
from functools import partial
from kivy.uix.widget import Widget
from Fire import sign_up
from Fire import sign_in,change
import Fire
import time
from add_user import get_user_name,get_user_city,get_user_mail
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window


class firebaseloginscreen(Screen):
    pass
class HomeScreen(Screen):
    pass
class AddScreen(Screen):
    pass
class DetailScreen(Screen):
    pass
class FirstScreen(Screen):
    pass
class SignIn(Screen):
    pass

class SignUp(Screen):
    pass


class MainApp(MDApp):


    def __init__(self, **kwargs):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = 'Gray'
        self.theme_cls.accent_palette = 'Gray'
        self.theme_cls.theme_style = 'Dark'
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            previous=True,
        )



    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        
    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True



    

    def build(self):
        self.load_product()

        Float=MDFloatingActionButton(icon="plus",pos_hint={'center_x': .5,"center_y": .1})
        self.root.ids['home_screen'].ids['Item'].add_widget(Float)
        Float.on_press=self.changer
        
        print("profile",self.root.ids['home_screen'].ids['profile_fragment'].ids)

        
        Gui=Builder.load_file("main.kv")
        pass
    def change_screen(self,screen_name):
        screen_manager=self.root.ids['screen_manger']
        screen_manager.current=screen_name

    def sign_in(self,text,password):
        sign_in(self,text,password)
        change(self)
        self.load_profile(get_user_name(Fire.localId),get_user_city(Fire.localId),get_user_mail(Fire.localId))

        

    def sign_up(self,mail,password,name,city):
        
        sign_up(mail,password,name,city)

    def add_product(self):
        title=self.root.ids['add_screen'].ids['name'].text
        Description=self.root.ids['add_screen'].ids['Description'].text
        Author=get_user_name(Fire.localId)
        City=get_user_city(Fire.localId)
        post(title,Description,Author,City)
        self.load_product()

        self.change_screen("home_screen")

    def changer(self):
        self.change_screen("add_screen")
    
    def toHome(self):
        self.change_screen("home_screen")


    def load_product(self):
        response = get()
        ls = list(response.keys())
        self.root.ids['home_screen'].ids['home_fragment'].clear_widgets()
        for i in range(len(ls)):
            titre = response.get(ls[i]).get('titre')
            Description=response.get(ls[i]).get('Description')
            Smart=SmartTileWithLabel(id=str(i),text="[size=12]{}[/size]".format(titre),source="cat-3.jpg")
            
            def open(tpl):
                self.load(tpl[0], tpl[1])
                self.change_screen("detail_screen")
                
            Smart.on_press=partial(open, (titre, Description))
            self.root.ids['home_screen'].ids['home_fragment'].add_widget(Smart)

    def load(self, titre, Description):
        #self.root.ids['detail_screen'].ids['mbox'].remove_widget(Ti)
        #self.root.ids['detail_screen'].ids['mbox'].remove_widget(Desc)

        Ti=MDLabel(id="titre",font_style='Body1',halign="center",text=titre)
        Desc=MDLabel(id="Descrip",font_style='Body1',halign="center",text=Description)
        Floati=MDFloatingActionButton(icon="plus",pos_hint={'center_x': .5,"center_y": .1})
        self.root.ids['detail_screen'].ids['mbox'].add_widget(Floati)
        
        def remove(tpl):
                self.root.ids['detail_screen'].ids['mbox'].remove_widget(tpl[0])
                self.root.ids['detail_screen'].ids['mbox'].remove_widget(tpl[1])
                self.root.ids['detail_screen'].ids['mbox'].remove_widget(tpl[2])

                self.change_screen("home_screen")
        Floati.on_press=partial(remove, (Ti, Desc,Floati))
        self.root.ids['detail_screen'].ids['mbox'].add_widget(Ti)
        self.root.ids['detail_screen'].ids['mbox'].add_widget(Desc)
    
    def load_profile(self,name,city,email):
        Img=Image(id="img",source="avatar.png",size=(200,200))    
        nom=MDLabel(id="name",font_style='Body1',halign="center",text=name)
        city=MDLabel(id="city",font_style='Body1',halign="center",text=city)
        email=MDLabel(id="city",font_style='Body1',halign="center",text=email)
        self.root.ids['home_screen'].ids['profile_fragment'].add_widget(Img)
        self.root.ids['home_screen'].ids['profile_fragment'].add_widget(nom)
        self.root.ids['home_screen'].ids['profile_fragment'].add_widget(city)
        self.root.ids['home_screen'].ids['profile_fragment'].add_widget(email)







        
    
MainApp().run()