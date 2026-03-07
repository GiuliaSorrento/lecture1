from dataclasses import dataclass
from datetime import date

# Import necessari per il funzionamento (assicurati che i percorsi siano corretti)
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine
from gestionale.core.clienti import Cliente


@dataclass
class Fattura:  # Classe con l'iniziale maiuscola (convenzione PEP8)
    ordine: Ordine
    numero_fattura: str
    data: date

    def genera_fattura(self):
        # Usiamo una lista per accumulare le stringhe
        linee = [
            "=" * 60,
            f"FATTURA no. {self.numero_fattura} del {self.data}",
            "=" * 60,
            f"Cliente:   {self.ordine.cliente.nome}",
            f"Categoria: {self.ordine.cliente.categoria}",
            f"Mail:      {self.ordine.cliente.email}",
            "-" * 60,
            "DETTAGLIO ORDINE",
            "-" * 60
        ]

        # Ciclo per le righe dell'ordine
        for i, riga in enumerate(self.ordine.righe, 1):
            linee.append(
                f"{i}. {riga.prodotto.nome:.<20} Qty: {riga.quantita} x {riga.prodotto.prezzo:.2f}€ = {riga.totale_riga():.2f}€"
            )

        # Il calcolo del totale va FUORI dal ciclo for, altrimenti si ferma alla prima riga
        netto = self.ordine.totale_netto()
        iva = netto * 0.22
        lordo = self.ordine.totale_lordo(0.22)

        linee.extend([
            "=" * 60,
            f"Totale netto:       €{netto:>10.2f}",
            f"IVA (22%):          €{iva:>10.2f}",
            f"TOTALE LORDO:       €{lordo:>10.2f}",
            "=" * 60
        ])

        return "\n".join(linee)


def _test_module():
    # Simulazione record prodotti (usando i nomi attributi corretti)
    p1 = ProdottoRecord("Laptop", 1200.0)
    p2 = ProdottoRecord("Mouse", 20.0)
    p3 = ProdottoRecord("Tablet", 600.0)

    # Corretto: rimosso l'errore della parentesi graffa }
    cliente = Cliente(nome="Mario Bianchi", email="mario.bianchi@gmail.com", categoria="Gold")

    ordine = Ordine(righe=[
        RigaOrdine(p1, 1),
        RigaOrdine(p2, 5),
        RigaOrdine(p3, 2)
    ], cliente=cliente)

    # Passiamo la data correttamente (date.today() è una funzione)
    mia_fattura = Fattura(ordine, "2026/01", date.today())

    print(mia_fattura.genera_fattura())


if __name__ == "__main__":
    _test_module()
