import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800 
    page.title = "EchoFlow"
    text = ft.Text("EchoFlow")
    page.add(text)


ft.app(target=main)

