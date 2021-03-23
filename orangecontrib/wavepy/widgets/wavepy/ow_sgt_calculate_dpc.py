from orangewidget import gui

from orangecontrib.wavepy.widgets.gui.ow_wavepy_widget import WavePyWidget

from wavepy2.util.common.common_tools import AlreadyInitializedError
from wavepy2.util.log.logger import register_logger_single_instance, LoggerMode
from wavepy2.util.plot.plotter import register_plotter_instance, PlotterMode
from wavepy2.util.ini.initializer import get_registered_ini_instance, register_ini_instance, IniMode
from wavepy2.util.log.logger import LoggerMode
from wavepy2.util.plot.plot_tools import PlottingProperties, DefaultContextWidget

from wavepy2.tools.common.wavepy_data import WavePyData
from wavepy2.tools.common.bl import crop_image

class OWSGTCalculateDPC(WavePyWidget):
    name = "S.G.T. - Calculate DPC"
    id = "sgt_calculate_dpc"
    description = "S.G.T. - Calculate DPC"
    icon = "icons/sgt_calculate_dpc.png"
    priority = 4
    category = ""
    keywords = ["wavepy", "tools", "crop"]

    inputs = [("WavePy Data", WavePyData, "set_input"),]

    outputs = [{"name": "WavePy Data",
                "type": WavePyData,
                "doc": "WavePy Data",
                "id": "WavePy_Data"}]

    want_main_area = 0

    CONTROL_AREA_HEIGTH = 840
    CONTROL_AREA_WIDTH  = 1500

    MAX_WIDTH_NO_MAIN = CONTROL_AREA_WIDTH + 10
    MAX_HEIGHT = CONTROL_AREA_HEIGTH + 10

    def __init__(self):
        super(OWSGTCalculateDPC, self).__init__(show_general_option_box=True, show_automatic_box=True)

        self.setFixedWidth(self.MAX_WIDTH_NO_MAIN)
        self.setFixedHeight(self.MAX_HEIGHT)

        gui.rubber(self.controlArea)

    def set_input(self, data):
        if not data is None:
            self._initialization_parameters = data.get_parameter("initialization_parameters")
            self._calculation_parameters    = data.get_parameter("calculation_parameters")
            self._process_manager           = data.get_parameter("process_manager")

            if self.is_automatic_run:
                self._execute()

    def _get_execute_button_label(self):
        return "Calculate DPC"

    def _execute(self):
        self._clear_wavepy_layout()

        output_calculation_parameters = self._process_manager.calculate_dpc(initial_crop_parameters=self._calculation_parameters,
                                                                             initialization_parameters=self._initialization_parameters,
                                                                             plotting_properties=PlottingProperties(context_widget=DefaultContextWidget(self._wavepy_widget_area),
                                                                                                                    add_context_label=False,
                                                                                                                    use_unique_id=True))

        self.controlArea.setFixedWidth(self.CONTROL_AREA_WIDTH)
        self.controlArea.setFixedHeight(self.CONTROL_AREA_HEIGTH)

        gui.rubber(self.controlArea)

        output = WavePyData()

        output.set_parameter("process_manager",           self._process_manager)
        output.set_parameter("initialization_parameters", self._initialization_parameters)
        output.set_parameter("calculation_parameters",    output_calculation_parameters)

        self.send("WavePy Data", output)