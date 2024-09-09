class YarnDetail:
    raw_length: float = 0.
    raw_count: int = 0
    cal_length: float = 0.
    cal_count: int = 0
    cal_weight: float = 0

    def cal_line_length(self):
        return f"{self.raw_length}cm/{self.raw_count}针"

    def cal_staple(self):
        return f"{self.raw_length * self.cal_count * 0.00591903719 / self.cal_weight:.2f}S"

    def cal_denier(self):
        return f"{5314.5 / (self.raw_length * self.cal_count * 0.00591903719 / self.cal_weight):.2f}D"


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
        self.fabric_weight = self.weight / (self.length * self.width / 10000)
        return f"{self.fabric_weight:.2f} GSM"

    def get_density_x(self):
        return f"{self.density_x_count / self.density_x_length:.2f}N/cm"

    def get_density_y(self):
        return f"{self.density_y_count / self.density_y_length:.2f}N/cm"
