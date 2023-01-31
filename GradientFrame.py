__author__ = "Jean Loui Bernard Silva de Jesus"
__translator__= "Alexander Schumacher"

from tkinter import Canvas

class GradientFrame(Canvas):
    
    """
    Widget mit Farbverläufen.
    """

    __tag = "GradientFrame"
    __hex_format = "#%04x%04x%04x"
    
    top2bottom = 1
    left2right = 2

    def __init__(self, parent, colors = ("red", "black"), direction = left2right, **kw):

        # Falls keine Geometrie definiert wurde, wird eine Standard-Geometrie definiert.
        kw["height"] = kw.get("height", 200)
        kw["width"] = kw.get("width", 200)
        
        # Ruft den Konstruktor des Canvas auf.
        super().__init__(parent, **kw)

        # Instanziert die Parameter.
        self.__geometry = [kw["width"], kw["height"]]
        self.__colors = colors
        self.__direction = direction

        # Zeichnet den Verlauf im Canvas.
        self.__draw_gradient()
        
    def __draw_gradient(self):
        
        """
        Zeichne den Canvas mit Farbverläufen.
        """

        # Löscht den Verlauf im Canvas.
        self.delete(self.__tag)

        # Empfängt die Breiten-Grenze.
        limit = self.__geometry[0] if self.__direction == self.left2right else self.__geometry[1]
       
        # Empfängt die RGB-Werte der Farben.
        red1, green1, blue1 = self.winfo_rgb(self.__colors[0])
        red2, green2, blue2 = self.winfo_rgb(self.__colors[1])

        # Berechnet die RGB-Werte des Farbauftrags (z.B.: while red1 != red2: red1 += r_ratio)
        # durch Teilen durch die Breiten-Grenze.
        r_ratio = (red2 - red1) / limit
        g_ratio = (green2 - green1) / limit
        b_ratio = (blue2 - blue1) / limit

        for pixel in range(limit):
            
            # Berechnet die Farbe im RGB-Format.
            red = int(red1 + (r_ratio * pixel))
            green = int(green1 + (g_ratio * pixel))
            blue = int(blue1 + (b_ratio * pixel))

            # Konvertiert die Farbe von RGB zu Hex.
            color = self.__hex_format % (red, green, blue)

            # Legt die Positionen (x1, y1, x2, y2) des Objekts fest.
            x1 = pixel if self.__direction == self.left2right else 0
            y1 = 0 if self.__direction == self.left2right else pixel
            x2 = pixel if self.__direction == self.left2right else self.__geometry[0]
            y2 = self.__geometry[1] if self.__direction == self.left2right else pixel

            # Stelle den Verlauf hinter alle Elemente auf dem Canvas.
            self.create_line(x1, y1, x2, y2, tag = self.__tag, fill = color)

        # Stelle den Verlauf hinter alle Elemente auf dem Canvas.
        self.tag_lower(self.__tag)

    def config(self, cnf = None, **kw):

        # Konfiguriere die Farben des Verlaufs.
        if "colors" in kw and len(kw["colors"]) > 1:
            self.__colors = kw.pop("colors")

        # Konfiguriere die Richtung des Verlaufs.
        if "direction" in kw and kw["direction"] in (self.left2right, self.top2bottom):
            self.__direction = kw.pop("direction")

        # Konfiguriere die Höhe des Verlaufs.
        if "height" in kw:
            self.__geometry[1] = kw["height"]

        # Konfiguriere die Breite des Verlaufs.
        if "width" in kw:
            self.__geometry[0] = kw["width"]

        # Konfiguriere das Canvas und zeichne den Verlauf.
        super().config(cnf, **kw)
        self.__draw_gradient()

    def configure(self, cnf = None, **kw):
        self.config(cnf, **kw)