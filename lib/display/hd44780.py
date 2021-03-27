####################################################
# PGSparkLite Pedal - HD44780 Display (v2 Hardware)
####################################################

from RPLCD.i2c import CharLCD
from lib.display.hd44780_large_font import HD44780_Large_Font

class HD44780_Display:
    def __init__(self, i2c_address, port_expander, display_height, display_width):

        self.lcd = CharLCD(port_expander, i2c_address, cols=display_width,
                           rows=display_height, auto_linebreaks=True)

        self.big_font = HD44780_Large_Font(self.lcd)

        pass

    def clear_screen(self):
        self.lcd.clear()

    def display_status(self, status):
        self.lcd.clear()
        self.lcd.write_string(status)

    def show_selected_preset(self, preset, name=None, bpm=None):
        self.lcd.clear()
        self.big_font.write_string(preset)
        self.lcd.cursor_pos = (3,0)

        # TODO: Chop this if it's too long
        if name != None:
            self.lcd.write_string(name)

        if bpm != None:
            self.lcd.cursor_pos = (0,13)
            self.lcd.write_string('BPM:' + bpm)

    def show_unselected_preset(self, preset, name=None, bpm=None):
        preset = preset + '*'
        self.show_selected_preset(preset, name, bpm)
