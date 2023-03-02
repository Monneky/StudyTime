from flet import Page, Text, NavigationBar, NavigationDestination, icons,app, FontWeight, FloatingActionButton, AlertDialog, View

if __name__ == "__main__":
    def main(page: Page):
        page.title = "Home"
        
        dlg = AlertDialog(
            title = Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
        )
        
        def open_play():
            print('Hey')
            # page.go("/play")

        def open_dlg(e):
            page.dialog = dlg
            dlg.open = True
            page.update()
            
        def route_change(route):
            page.views.clear()
            page.views.append(
                View(
                    '/',
                    [
                        Text("This is main page")
                    ],
                )
            ),
            if page.route == "/play":
                page.views.append(
                    '/play', 
                    [
                        Text("Hello, this is Play section")
                    ]
                ),
            page.update()
        
        page.floating_action_button = FloatingActionButton(
            icon=icons.HELP,
            on_click=open_dlg
        )
        page.add(
            Text("Welcome to the Study Timer", size=50,  weight=FontWeight.W_900),
            Text("In the below menu you can choose an option, if you have doubts please click in the help icon to see how to use this app, thank you.", size=20)
        )
        
        # page.go(route_change)

app(target=main)