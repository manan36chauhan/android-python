from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCardSwipe


class Test(MDApp):
    def build(self):

        return Builder.load_string()

    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        return Builder.load_string(

            '''
BoxLayout:
    
    
    orientation:'vertical'
    
    MDToolbar:
        title: 'Welcome to Emedicare'
        md_bg_color: .3, .3, .2, 2
        specific_text_color: 6, 6, 6, 5
    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()
    MDSlider:
        min: 0
        max: 100
        value: 40
    MDFloatingActionButton:
        icon: "medical-bag"
        md_bg_color: app.theme_cls.primary_color
    MDCard:
            
        padding: "8dp"
        size_hint: None, None
        elevation: 500
        size: "150dp", "150dp"
        pos_hint: {"center_x": .1, "center_y": .1}
        Image:
            source: "image.jpg"
                        
    MDCard:
            
        padding: "8dp"
        size_hint: None, None
        elevation: 200
        size: "150dp", "150dp"
        pos_hint: {"center_x": .1, "center_y": .2}
        Image:
            source: "image2.jpg"
            
    MDCard:
            
        padding: "8dp"
        size_hint: None, None
        elevation: 
        size: "150dp", "150dp"
        pos_hint: {"center_x": .1, "center_y": .8} 
        Image:
            source: "image3.jpg"
                   
    MDBottomNavigation:
    
        
        panel_color: .3, .4, .5, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: ''
            icon: 'home'
  

        MDBottomNavigationItem:
            name: 'screen 2'
            text: ''
            icon: 'account'

            MDLabel:
                text: 'I programming of C++'
                halign: 'center'
        
        MDBottomNavigationItem:
            name: 'screen 2'
            text: ''
            icon: 'monitor-dashboard'

            
        MDBottomNavigationItem:
            name: 'screen 3'
            text: ''
            icon: 'settings'

            MDLabel:
                text: ''
                halign: 'center'
'''
        )

class TestCard(MDApp):



    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="DISCARD", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()


Test().run()
