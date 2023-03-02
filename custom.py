from flet import app, Page, NavigationBar, NavigationDestination, icons, Text

def main(page: Page):
    page.title = "Play"
    page.navigation_bar = NavigationBar(
        destinations= [
            NavigationDestination(icon=icons.PLAY_ARROW, label="Start"),
            NavigationDestination(icon=icons.PERSON, label="Custom Mode"),
            NavigationDestination(icon=icons.HISTORY, label="History")
        ]
        )
    page.add(
        Text('This is custom section')
    )

app(target=main)