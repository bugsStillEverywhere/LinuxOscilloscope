from HWaccess.USBTMC import USBTMC
from HWaccess.LXI import lxi
from HWaccess.RS232Device import RS232Device


class Device:
    def __init__(self):
        self.device = None
        self.locale = 'utf-8'
        pass

    def init_device(self, mode, port, params={}):
        """

        :param mode: 0 - lxi, 1 - rs232, 2 - usbtmc
        :param port: ip, rs232 or usbtmc ports
        :param params - rs232 parameters as dictionary, for rs232 only, empty otherwise
        :return:
        """
        idn = None
        status = -1
        if mode == 0:
            self.device = lxi(port)
            idn = self.device.ask("*idn?")
            status = 0
        elif mode == 2:
            self.device =USBTMC(port)
            idn = str(self.device.getName())
            status = 0
        elif mode == 1:
            self.device = RS232Device(port)
            self.device._setup_port(params)
            params_check = self.device.serial.get_settings()
            print(params_check)
            idn = str(self.device.getName())
            pass
        else:
            idn = None
            status = -1
        return idn, status

    def ask(self, cmd:str):
        answer, status = self.device.ask(cmd)
        return answer, status
        pass

    def write(self, cmd:str):
        answer, status = self.device.write(cmd)
        return answer, status

    def get_horizontal_data(self):
        pass

    def get_vertical_data(self):
        pass



