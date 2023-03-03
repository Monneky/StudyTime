from flet import Page, Text, icons,app, FloatingActionButton, AlertDialog, View, AppBar, colors, ElevatedButton, Icon

if __name__ == "__main__":
    def main(page: Page):
        page.title = "Home"
        
        dlg = AlertDialog(
            title = Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
        )
        
        def open_play(e):
            page.go("/play")
        
        def go_main(e):
            page.go('/')
        
        def go_custome(e):
            page.go('/custome')
            
        def go_history(e):
            page.go('/history')

        def open_dlg(e):
            page.dialog = dlg
            dlg.open = True
            page.update()
            
        def route_change(e):
            page.views.clear()
            page.views.append(
                View(
                    "/",
                    [
                        AppBar(
                            leading=Icon(icons.ACCESS_TIME_FILLED_OUTLINED),
                            leading_width=50,
                            title=Text("Study Timer "), 
                            bgcolor=colors.SURFACE_VARIANT,
                            center_title=False,
                            actions= [
                                ElevatedButton('Home', on_click=go_main),
                                ElevatedButton('Play', on_click=open_play),
                                ElevatedButton('Custome', on_click=go_custome),
                                ElevatedButton('History', on_click=go_history),
                            ]
                        ),
                    ],
                )
            )
            if page.route == "/play":
                page.views.append(
                    View(
                        "/play",
                        [
                            AppBar(
                                leading=Icon(icons.ACCESS_TIME_FILLED_OUTLINED),
                                leading_width=50,
                                title=Text("Study Timer "), 
                                bgcolor=colors.SURFACE_VARIANT,
                                center_title=False,
                                actions= [
                                    ElevatedButton('Home', on_click=go_main),
                                    ElevatedButton('Play', on_click=open_play),
                                    ElevatedButton('Custome', on_click=go_custome),
                                    ElevatedButton('History', on_click=go_history),
                                ]
                        ),
                        ],
                    )
                )
            elif page.route == '/custome': 
                page.views.append(
                    View(
                        '/custome',
                        [
                            AppBar(
                                leading=Icon(icons.ACCESS_TIME_FILLED_OUTLINED),
                                leading_width=50,
                                title=Text("Study Timer "), 
                                bgcolor=colors.SURFACE_VARIANT,
                                center_title=False,
                                actions= [
                                    ElevatedButton('Home', on_click=go_main),
                                    ElevatedButton('Play', on_click=open_play),
                                    ElevatedButton('Custome', on_click=go_custome),
                                    ElevatedButton('History', on_click=go_history),
                                ]
                        ),
                        ]
                    )
                )
            elif page.route == '/history':
                page.views.append(
                    View(
                        '/history',
                        [
                            AppBar(
                                leading=Icon(icons.ACCESS_TIME_FILLED_OUTLINED),
                                leading_width=50,
                                title=Text("Study Timer "), 
                                bgcolor=colors.SURFACE_VARIANT,
                                center_title=False,
                                actions= [
                                    ElevatedButton('Home', on_click=go_main),
                                    ElevatedButton('Play', on_click=open_play),
                                    ElevatedButton('Custome', on_click=go_custome),
                                    ElevatedButton('History', on_click=go_history),
                                ]
                        ),
                        ]
                    )
                )
            page.update()
        
        page.on_route_change = route_change
        
        page.go(page.route)

app(target=main)