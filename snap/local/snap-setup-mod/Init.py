import os
import sys
from xdg_desktop_portal_file_chooser import enable_native_file_dialog_if_whitelisted

pythonpath = os.environ.get("SNAP_PYTHONPATH")

if pythonpath:
  print(f"Adding snap-specific PYTHONPATH to sys.path: {pythonpath}")
  os.environ["PYTHONPATH"] = pythonpath
  for path in pythonpath.split(":"):
    sys.path.insert(0, path)

enable_native_file_dialog_if_whitelisted()
