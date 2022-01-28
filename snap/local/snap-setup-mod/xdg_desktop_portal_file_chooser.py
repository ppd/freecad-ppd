import FreeCAD as App

def get_host_os_info():
  os_info = {}
  with open("/etc/lsb-release") as f:
    for line in f:
      [key, value] = line.split("=")
      os_info[key] = value.strip("\"'\n ")
  return os_info

def host_supports_unproxied_file_chooser():  
  whitelist = [
    "Ubuntu 21.04",
    "Ubuntu 21.10"
  ]
  os_info = get_host_os_info()
  return f"{os_info['DISTRIB_ID']} {os_info['DISTRIB_RELEASE']}" in whitelist

def has_pref(pref_group, pref_key):
  content = pref_group.GetContents()
  if content:
    for pref in content:
      if pref[1] == pref_key:
        return True
  return False

def enable_native_file_dialog_if_whitelisted():
  dialog_params = App.ParamGet("User parameter:BaseApp/Preferences/Dialog")
  is_native_dialog_explicitly_set = has_pref(dialog_params, "DontUseNativeDialog")

  if not is_native_dialog_explicitly_set and host_supports_unproxied_file_chooser():
    dialog_params.SetBool("DontUseNativeDialog", False)  
