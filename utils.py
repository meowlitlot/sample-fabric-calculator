class YarnDetail:
    raw_length: float = 0.
    raw_count: int = 0
    cal_length: float = 0.
    cal_count: int = 0
    cal_weight: float = 0

    def cal_line_length(self):
        return f"{self.raw_length}cm/{self.raw_count}针"

    def cal_staple(self):
        try:
            return f"{self.cal_length * self.cal_count * 0.00591903719 / self.cal_weight:.2f}S"
        except ZeroDivisionError:
            return "0S"

    def cal_denier(self):
        try:
            return f"{5314.5 / (self.cal_length * self.cal_count * 0.00591903719 / self.cal_weight):.2f}D"
        except ZeroDivisionError:
            return "0D"


class SampleFabric:
    length: float = 0.
    width: float = 0.
    weight: float = 0.
    fabric_weight: float = 0.
    density_x_count: int = 0
    density_x_length: float = 0.
    density_y_count: int = 0
    density_y_length: float = 0.

    def get_gsm(self):
        try:
            self.fabric_weight = self.weight / (self.length * self.width / 10000)
        except ZeroDivisionError:
            self.fabric_weight = 0.
        return f"{self.fabric_weight:.2f} GSM"

    def get_density_x(self):
        try:
            return f"{self.density_x_count / self.density_x_length:.2f}N/cm"
        except ZeroDivisionError:
            return "0N/cm"

    def get_density_y(self):
        try:
            return f"{self.density_y_count / self.density_y_length:.2f}N/cm"
        except ZeroDivisionError:
            return "0N/cm"
