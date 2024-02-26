import json

class MouseConfig:
  def __init__(self, dpi, sens, btnAssigment):
    self.dpi = dpi
    self.sens = sens
    self.btnAssigment = btnAssigment

  def from_json(data):
    return MouseConfig(
      dpi = data['dpiSetting'],
      sens = data['sensitivity'],
      btnAssigment = data['buttonAssigment']
    )


