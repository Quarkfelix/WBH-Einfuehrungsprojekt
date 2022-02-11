### Spiel Pong erweitert (programmiert mit Python und Bibliotheken pygame und spiel)
### Vorlage fuer B-Aufgabe INF-L
### Stand Mai 2020, Copyright Wilhelm Buechner Hochschule

from spiel import *

## hier Klasse ColoredBall definieren
## die Klasse erbt von Ball,
## initalisiert den Ball ueber den Konstruktor der Superklasse
## und setzt das Attribut farbe 


## hier ist Klasse TastaturSchlaeger schon definiert
## die Klasse erbt von Schlaeger und fuegt die Methode movekey hinzu
class TastaturSchlaeger(Schlaeger):
    # Funktion zum Bewegen des Schlaegers mit Tastatur
    def movekey(self, pos):
        self.rect.y = self.rect.y + (pos * self.geschwindigkeit)

## hier ist der Rumpf der Klasse SpielErweiterung schon definiert
class SpielErweitert(Spiel):
    '''Erweiterung des Spiels um Tastatureingaben und
       Tastatursteuerung des Schlaegers'''

    # hier Erweiterung des Spiels um Tastatureingaben und
    # Tastatursteuerung des Schlaegers hinzufuegen



    # hier neue Methode zur Tastensteuerung einfuegen



# das Hauptprogramm, Einstiegspunkt fuer den Aufruf vom Betriebssystem
def main():

    '''Konkrete Instanzen hier deklarieren'''

    ## hier Farbe in RGB-Werten definieren oder
    ## Farbe über pygame Methode Color mit Namen spezifizieren
    ## Objekt der Klasse ColoredBall anlegen



    ## hier Objekt spielerSchlaeger von Klasse TastaturSchlaeger anlegen
    ## und mit Parametern (x, y, breite, hoehe, geschwindigkeit) initialisieren
    ## analog zur vorherigen Version




    ## die folgenden Objekte sind vorgegeben (id. zur anderen Vorlage)
    spielfeld = Spielfeld()

    computerSchlaeger = AutoSchlaeger(
        x = config.rechter_rand(),
        y = config.schlaeger_mitte(),
        breite = config.schlaegerBreite,
        hoehe = config.schlaegerHoehe,
        geschwindigkeit = 5,
        ball = ball
    )

    punkteAnzeige = PunkteAnzeige(
        punkte = 0,
        x = config.fensterBreite - 150,
        y = 25,
        schrift = config.schrift()
    )

    ## Aufruf der Methode run der Klasse SpielErweitert
    SpielErweitert(spielfeld, spielerSchlaeger, computerSchlaeger, ball, punkteAnzeige).run()

# Aufruf der Main-Funktion
if __name__ == '__main__':
    main()
