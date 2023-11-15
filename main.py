import flet as ft
from flet import (
    Column,
    Container,
    border_radius,
    colors,
    MainAxisAlignment,
    UserControl
)

drop_down = []
heading = ft.Text("Knitting Gauge Calculator", size=20, color=colors.WHITE)
pattern_gauge_heading = ft.Text("Select Pattern Gauge", size=15, color=colors.WHITE)
user_gauge_heading = ft.Text("Select User Gauge", size=15, color=colors.WHITE)
ask_rows = ft.Text("            Rows")
ask_stitches = ft.Text("Stitches")


class GaugeCalculator(UserControl):

    def build(self):
        self.change_text = ft.Text()

        for i in range(100):
            drop_down.append(ft.dropdown.Option(i))

        pattern_row_dropdown = ft.Dropdown(
            width=100,
            options=drop_down,
        )
        pattern_stitch_dropdown = ft.Dropdown(
            width=100,
            options=drop_down,
        )
        user_row_dropdown = ft.Dropdown(
            width=100,
            options=drop_down,
        )
        user_stitch_dropdown = ft.Dropdown(
            width=100,
            options=drop_down,
        )

        def button_clicked(e):
            try:
                pattern_rows = int(pattern_row_dropdown.value)
                pattern_stitches = int(pattern_stitch_dropdown.value)
                user_rows = int(user_row_dropdown.value)
                user_stitches = int(user_stitch_dropdown.value)
                stitch_change = ((user_stitches - pattern_stitches) / pattern_stitches) * 100
                row_change = ((user_rows - pattern_rows) / pattern_rows) * 100
                self.change_text.value = f"Multiply the stitches by {stitch_change:.2f}%\nMultiply the rows by {row_change:.2f}%"
                self.update()
            except TypeError:
                self.change_text.value = "Please select values"
                self.update()
            except:
                self.change_text.value = "An Error Has Occurred"
                self.update()

        return Container(
            width=400,
            bgcolor=colors.BLUE_900,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    ft.Row(
                        controls=[heading],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls=[pattern_gauge_heading],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls=[
                            ask_stitches,
                            ask_rows
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls=[
                            pattern_stitch_dropdown,
                            pattern_row_dropdown
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls=[user_gauge_heading],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls=[
                            ask_stitches,
                            ask_rows
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls=[
                            user_stitch_dropdown,
                            user_row_dropdown
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls=[ft.ElevatedButton(text="Submit", on_click=button_clicked, bgcolor="blue")],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls=[self.change_text],
                        alignment=MainAxisAlignment.CENTER
                    )
                ]
            )
        )


def main(page: ft.Page):
    page.title = "Knitting Gauge Calculator"

    calc = GaugeCalculator()

    page.add(
        calc
    )


ft.app(target=main)
