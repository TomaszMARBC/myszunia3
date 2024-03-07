import json


class MouseConfig:
  def __init__(self, dpi, sens, btnAssignments):
    self.dpi = dpi
    self.sens = sens
    self.btnAssignments = btnAssignments

  #@staticmethod
  def config_from_json(data):
    return MouseConfig(
      dpi = data['dpiSettings'],
      sens = data['sensitivity'],
      btnAssignments = data['buttonAssignments']
    )


with open('mouse_config.json', 'r') as file:
  data = json.load(file)
  mouse_config = MouseConfig.config_from_json(data)

print(mouse_config.dpi['high'])