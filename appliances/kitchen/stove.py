from appliances import Appliance

class Stove(Appliance):

    def __init__(self, color, heat_method="gas"):
        super().__init__(color)

    def make_tea(self):
        print("gurgle, gurgle. Ding. Your drug of choice is piping hot and ready!")
