### Spiel Pong erweitert (programmiert mit Python und Bibliotheken pygame und spiel)
### Vorlage fuer B-Aufgabe INF-L
### Stand Mai 2020, Copyright Wilhelm Buechner Hochschule

from spiel import *

## hier Klasse ColoredBall definieren
## die Klasse erbt von Ball,
## initalisiert den Ball ueber den Konstruktor der Superklasse
## und setzt das Attribut farbe
class ColoredBall(Ball):
    def __init__(self, x, y, breite, hoehe, geschwindigkeit, farbe):
        super().__init__(
            x=x,
            y=y,
            breite=breite,
            hoehe=hoehe,
            geschwindigkeit=geschwindigkeit,
            farbe=farbe
        )


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
    def _ereignisse_behandeln(self):
        # Ereignis abfragen
        for ereignis in pygame.event.get():
            self._behandle(ereignis)

    def _behandle(self, event):
        # Ueberpruefe ob Schliessen-Symbol im Fenster gedrueckt wurde
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self._spieler.move([0, self._spieler.rect.y - self._spieler.geschwindigkeit])
            if event.key == pygame.K_s:
                self._spieler.move([0, self._spieler.rect.y - self._spieler.geschwindigkeit])
            if event.key == pygame.K_d:
                self._spieler.move([0, self._spieler.rect.y - self._spieler.geschwindigkeit])
            if event.key == pygame.K_f:
                self._spieler.move([0, self._spieler.rect.y - self._spieler.geschwindigkeit])
            if event.key == pygame.K_j:
                self._spieler.move([0, self._spieler.rect.y + self._spieler.geschwindigkeit])
            if event.key == pygame.K_k:
                self._spieler.move([0, self._spieler.rect.y + self._spieler.geschwindigkeit])
            if event.key == pygame.K_l:
                self._spieler.move([0, self._spieler.rect.y + self._spieler.geschwindigkeit])
            if event.key == pygame.K_SEMICOLON:
                self._spieler.move([0, self._spieler.rect.y + self._spieler.geschwindigkeit])

        return event


# das Hauptprogramm, Einstiegspunkt fuer den Aufruf vom Betriebssystem
def main():

    '''Konkrete Instanzen hier deklarieren'''

    ## hier Farbe in RGB-Werten definieren oder
    ## Farbe über pygame Methode Color mit Namen spezifizieren
    ## Objekt der Klasse ColoredBall anlegen
    ball = ColoredBall(
        x=config.fensterBreite // 2 - 20,
        y=config.fensterHoehe // 2 - 20,
        breite=config.linienDicke,
        hoehe=config.linienDicke,
        geschwindigkeit=1,
        farbe=pygame.Color('blue')
    )


    ## hier Objekt spielerSchlaeger von Klasse TastaturSchlaeger anlegen
    ## und mit Parametern (x, y, breite, hoehe, geschwindigkeit) initialisieren
    ## analog zur vorherigen Version
    spielerSchlaeger = TastaturSchlaeger(
        x=config.linker_rand(),
        y=config.schlaeger_mitte(),
        breite=config.schlaegerBreite,
        hoehe=config.schlaegerHoehe,
        geschwindigkeit=5
    )

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
