# general imports
import sys
# import PyQt5 elements
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
# import map classes
from maps import MapList
# import window classes
from aboutWindow import AboutWindow
from backgroundWindow import BackgroundWindow
from fittingWindow import FittingWindow
from mapWindow import MapWindow
from pixelInformationWindow import PixelInformationWindow
from spectrumWindow import SpectrumWindow


class Py2DSpectroscopy(QApplication):

    """
    Py2DSpectroscopy
    This is the main class of the application. It controls the different windows
    and saves the maps in a map list.
    """

    # TODO: Map geometry operations: flipping and rotation

    # define list signals
    map_added = pyqtSignal(int)             # int: map id
    map_removed = pyqtSignal(int)           # int: map id
    selected_map_changed = pyqtSignal(int)  # int: map id

    # define map signals
    fit_changed = pyqtSignal(int)            # int: map id
    focus_changed = pyqtSignal(int)          # int: map id
    interval_changed = pyqtSignal(int)       # int: map id
    selected_data_changed = pyqtSignal(int)  # int: map id
    spectrum_changed = pyqtSignal(int)       # int: map id

    def __init__(self):

        # call super init
        super().__init__(sys.argv)

        # connect exit method
        self.aboutToQuit.connect(self.exit_app)

        # list for all loaded maps
        self.maps = MapList()

        # dictionary for all windows
        self.windows = {
            "aboutWindow": AboutWindow(),
            "backgroundWindow": BackgroundWindow(),
            "fittingWindow": FittingWindow(),
            "mapWindow": MapWindow(),
            "pixelInformationWindow": PixelInformationWindow(),
            "spectrumWindow": SpectrumWindow()
        }

        # connect to map list signals
        self.map_added.connect(self.windows['backgroundWindow'].add_widget)
        self.map_added.connect(self.windows['fittingWindow'].add_widget)
        self.map_added.connect(self.windows['pixelInformationWindow'].add_widget)
        self.map_added.connect(self.windows['spectrumWindow'].add_widget)

        self.map_removed.connect(self.windows['backgroundWindow'].remove_widget)
        self.map_removed.connect(self.windows['fittingWindow'].remove_widget)
        self.map_removed.connect(self.windows['pixelInformationWindow'].remove_widget)
        self.map_removed.connect(self.windows['spectrumWindow'].remove_widget)

        self.selected_map_changed.connect(self.windows['backgroundWindow'].change_widget)
        self.selected_map_changed.connect(self.windows['fittingWindow'].change_widget)
        self.selected_map_changed.connect(self.windows['pixelInformationWindow'].change_widget)
        self.selected_map_changed.connect(self.windows['spectrumWindow'].change_widget)

        # connect to map signals
        self.fit_changed.connect(self.windows['mapWindow'].update_data)
        self.fit_changed.connect(self.windows['mapWindow'].update_data_selection_combo_box)
        self.fit_changed.connect(self.windows['pixelInformationWindow'].update_data)
        self.fit_changed.connect(self.windows['spectrumWindow'].update_data)

        self.focus_changed.connect(self.windows['mapWindow'].update_crosshair)
        self.focus_changed.connect(self.windows['pixelInformationWindow'].update_data)
        self.focus_changed.connect(self.windows['spectrumWindow'].update_data)

        self.interval_changed.connect(self.windows['mapWindow'].update_data)
        self.interval_changed.connect(self.windows['pixelInformationWindow'].update_data)
        self.interval_changed.connect(self.windows['spectrumWindow'].update_data)

        self.selected_data_changed.connect(self.windows['mapWindow'].update_data)

        self.spectrum_changed.connect(self.windows['mapWindow'].update_data)
        self.spectrum_changed.connect(self.windows['pixelInformationWindow'].update_data)
        self.spectrum_changed.connect(self.windows['spectrumWindow'].update_data)

        # show the map window
        self.windows['mapWindow'].show()

    @staticmethod
    def exit_app():

        print('Thanks for using me!')

if __name__ == "__main__":

    # create app
    app = Py2DSpectroscopy()

    # execute app and close system afterwards
    sys.exit(app.exec_())
