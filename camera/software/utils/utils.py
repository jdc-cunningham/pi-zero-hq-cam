from subprocess import run

class Utils:
  def __init__(self):
    self.pi_ver = 1 # or 2 determine

    self.get_pi_ver()

  # need this for OLED max SPI speed (refresh)
  # https://stackoverflow.com/a/72163326
  def get_pi_ver(self):
    # cmd = 'less "/proc/cpupinfo" | grep processor | wc -l' # was trying to use this initially
    cmd = 'less "/proc/cpuinfo" | grep processor'

    try:
      core_count = run(cmd, capture_output=True, shell=True, text=True)
      self.pi_ver = 2 if len(core_count.stdout.split("\n")) == 5 else 1 # this is dumb
    except:
      # I put this here because the above doesn't run on pi zero 1, 3.5.3 python
      print('failed to determine pi version')
