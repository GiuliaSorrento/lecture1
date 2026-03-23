import flet as ft


class View:
    def __init__(self, page: ft.Page):
        self._page = page
        self._controller = None
        self._page.title = "TdP 2025 - Software Gestionale"
        self._page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centering
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # Don't call update_page here yet, wait until UI is loaded

    def carica_interfaccia(self):
        # TextFields - Prodotto
        self._txtInNomeP = ft.TextField(label="Nome prodotto", width=200)
        self._txtInPrezzo = ft.TextField(label="Prezzo", width=200)
        self._txtInQuantita = ft.TextField(label="Quantità", width=200)

        row1 = ft.Row(
            controls=[self._txtInNomeP, self._txtInPrezzo, self._txtInQuantita],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # TextFields - Cliente
        self._txtInNomeC = ft.TextField(label="Nome Cliente", width=200)
        self._txtInMail = ft.TextField(label="Mail", width=200)
        self._txtInCategoria = ft.TextField(label="Categoria", width=200)

        row2 = ft.Row(
            controls=[self._txtInNomeC, self._txtInMail, self._txtInCategoria],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Buttons - Using positional arguments for text to avoid the TypeError
        self._btnAdd = ft.ElevatedButton("Aggiungi ordine",
                                         on_click=self._controller.add_ordine, width=200)

        self._btnGestisciOrdine = ft.ElevatedButton("Gestisci prox ordine",
                                                    on_click=self._controller.gestisci_ordine, width=200)

        self._btnGestisciAllOrdini = ft.ElevatedButton("Gestisci tutti gli ordini",
                                                       on_click=self._controller.gestisci_all_ordini, width=200)

        self._btnStampaInfo = ft.ElevatedButton("Stampa sommario",
                                                on_click=self._controller.stampa_sommario, width=200)

        row3 = ft.Row(
            controls=[self._btnAdd, self._btnGestisciOrdine, self._btnGestisciAllOrdini, self._btnStampaInfo],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Output area
        self._lvOut = ft.ListView(expand=True, spacing=10, padding=20)

        # Add everything to page
        self._page.add(row1, row2, row3, self._lvOut)
        self.update_page()

    def set_controller(self, c):
        self._controller = c

    def update_page(self):
        self._page.update()