from dataclasses import dataclass
from datetime import date

from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine
from gestionale.core.clienti import ClienteRecord, Cliente


@dataclass
class fattura:
    ordine:"Ordine"
    numero_fattura:str
    data: date

    def genera_fattura(self):
        linee = [
            f"="*60  #ripeti 60 voltr uguale
            #intestazione fattura:data e numero fattura
            f"Fattura no. {self.numero_fattura} del {self.data}"
            f"=" * 60
            #dettagli del cliente
            f"Cliente:{self.ordine.cliente.nome}",
            f"Categoria: {self.ordine.cliente.nome}",
            f"Mail: {self.ordine.cliente.email}"
            f"DETTAGLIO ORDINE"
        ]
        for i,riga in enumerate(self.ordine.righe):    #enumerate si usa sulle liste, mi restituisce due quantita: indice e valore
            linee.append(
                f"{i}"
                f"{riga.prodotto.name}"
                f"quantita{riga.quantita } x {riga.prodotto.prezzo_unitario} = "
                f"tot. {riga.totale_riga()}"
            )

            linee.append(
                 f"=" * 60 ,
                 f"Totale netto: {self.ordine.totale_netto()}",
                 f"(IVA(22%): {self.ordine.totale_netto()*0.22}",
                 f"totale lordo: {self.ordine.totale_lordo()}",
                 f"=" * 60
            )
            return "\n".join(linee)




def _test_module():
    p1=ProdottoRecord("Laptop", 1200)
    p2=ProdottoRecord("Mouse",20)
    p3=ProdottoRecord("tablet", 600.0)
    cliente = Cliente(nome= "Mario Bianchi", mail= "mario.bianchi@gmail.com",categoria = "Gold" }
    ordine = Ordine(righe=[
        RigaOrdine(p1,1),
        RigaOrdine(p2,5),
        RigaOrdine(p3,2)], cliente=cliente)

    fattura = fattura(ordine,"2026/01",date.today)

    print(fattura.genera_fattura())





if __name__=="__main__":
    _test_module()

