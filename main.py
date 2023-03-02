import flet as ft

def main(page: ft.Page):
    page.title = "Home"
    page.navigation_bar = ft.NavigationBar(
        destinations= [
            ft.NavigationDestination(icon=ft.icons.PLAY_ARROW, label="Start"),
            ft.NavigationDestination(icon=ft.icons.PERSON, label="Custom Mode"),
            ft.NavigationDestination(icon=ft.icons.HISTORY, label="History")
        ]
    )
    page.add(
        ft.Text("Welcome to the Study Timer", size=50,  weight=ft.FontWeight.W_900),
        ft.Text("In the below menu you can choose an option, if you have doubts please click in the help icon to see how to use this app, thank you.", size=20)
    )

ft.app(target=main)