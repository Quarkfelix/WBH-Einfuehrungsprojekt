### Spiel Pong programmiert mit Python und Bibliotheken pygame und spiel
### Vorlage fuer B-Aufgabe INF-L
### Stand Mai 2020, Copyright Wilhelm Buechner Hochschule

from spiel import *


# das Hauptprogramm, Einstiegspunkt fuer den Aufruf vom Betriebssystem
def main():
    '''Konkrete Instanzen hier deklarieren'''

    # Hinweis: Achten Sie auf die korrekte Einrückung der Zeilen

    ## hier Objekt ball von Klasse Ball anlegen
    ## und mit Parametern (x, y, breite, hoehe, geschwindigkeit) initialisieren
    ball = Ball(
        x=config.fensterBreite // 2 - 20,
        y=config.fensterHoehe // 2 - 20,
        breite=config.linienDicke,
        hoehe=config.linienDicke,
        geschwindigkeit=1
    )

    ## hier Objekt spielerSchlaeger von Klasse Schlaeger anlegen
    ## und mit Parametern (x, y, breite, hoehe, geschwindigkeit) initialisieren
    spielerSchlaeger = Schlaeger(
        x=config.linker_rand(),
        y=config.schlaeger_mitte(),
        breite=config.schlaegerBreite,
        hoehe=config.schlaegerHoehe,
        geschwindigkeit=5
    )
    ## hier Objekt spielfeld von Klasse Spielfeld anlegen (keine Parameter)
    spielfeld = Spielfeld()
    ## Objekt computerSchlaeger von Klasse AutoSchlaeger ist schon angelegt
    ## und mit Parametern (x, y, breite, hoehe, geschwindigkeit) initialisiert
    ## Objekt ball wird uebergeben, damit computerSchlaeger dem Ball folgen kann
    computerSchlaeger = AutoSchlaeger(
        x=config.rechter_rand(),
        y=config.schlaeger_mitte(),
        breite=config.schlaegerBreite,
        hoehe=config.schlaegerHoehe,
        geschwindigkeit=5,
        ball=ball
    )

    ## Objekt punkteAnzeige von Klasse PunkteAnzeige ist schon angelegt
    ## und mit Parametern (punkte, x, y, schrift) initialisiert
    punkteAnzeige = PunkteAnzeige(
        punkte=0,
        x=config.fensterBreite - 150,
        y=25,
        schrift=config.schrift()
    )

    ## Aufruf der Methode run der Klasse Spiel ist ebenfalls vorgegeben
    Spiel(spielfeld, spielerSchlaeger, computerSchlaeger, ball, punkteAnzeige).run()


# Aufruf der Main-Funktion
if __name__ == '__main__':
    main()
