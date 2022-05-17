def show_migration_prompt():
  import FreeCAD, FreeCADGui
  from PySide2.QtWidgets import QCheckBox, QMessageBox

  param = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/SnapMigrationPrompt")

  if param.GetBool("DontAskAgain", False):
    return

  def dont_ask(checked):
    param.SetBool("DontAskAgain", checked)

  checkbox = QCheckBox("Don't mention it again")

  dlg = QMessageBox(FreeCADGui.getMainWindow())
  dlg.setWindowTitle("freecad-ppd becomes freecad")

  dlg.setText(
  """
  The freecad-ppd snap has been adopted as the official snap package of the FreeCAD project.<br>
  From now on, new versions will be published as freecad, and freecad-ppd will be retired.<br>
  <p>
    If you want to continue receiving updates, install the freecad snap from the Snap Store:
  </p>
  <p>
    <a href="https://snapcraft.io/freecad">Install FreeCAD on Linux | Snap Store</a>
  </p>
  """)

  dlg.addButton(QMessageBox.Ok)
  dlg.setDefaultButton(QMessageBox.Ok)
  dlg.setCheckBox(checkbox)
  checkbox.toggled.connect(dont_ask)

  return dlg.exec()

show_migration_prompt()
