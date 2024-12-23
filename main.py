
import flet as ft

def main(page: ft.Page):
    page.title = "Best Dev Ever"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.controls.append(
        ft.Text(
            "I'm the best Dev ever!",
            text_align=ft.TextAlign.CENTER,
            font_size=24,
            font_weight=ft.FontWeight.BOLD,
        )
    )

ft.app(target=main)
