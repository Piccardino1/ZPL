import win32print
import win32api
from printer_name import printer_name

win32print.SetDefaultPrinter(printer_name)

win32api.ShellExecute(0, "print", "result.pdf", None, ".", 0)
