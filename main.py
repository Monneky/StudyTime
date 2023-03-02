from flet import Page,Text, NavigationBar, NavigationDestination, icons,app, FontWeight, FloatingActionButton

if __name__ == "__main__":
    def main(page: Page):  
        page.title = "Home"
        page.navigation_bar = NavigationBar(
            destinations= [
                NavigationDestination(icon=icons.PLAY_ARROW, label="Start"),
                NavigationDestination(icon=icons.PERSON, label="Custom Mode"),
                NavigationDestination(icon=icons.HISTORY, label="History")
            ]
        )
        page.floating_action_button = FloatingActionButton(
            icon=icons.HELP
        )
        page.add(
            Text("Welcome to the Study Timer", size=50,  weight=FontWeight.W_900),
            Text("In the below menu you can choose an option, if you have doubts please click in the help icon to see how to use this app, thank you.", size=20),
            Text(f'Route {page.route}')
        )

app(target=main)