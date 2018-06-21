LButton::clicker()
clicker()
{
	Click
	While GetKeyState("ScrollLock", "T"){
		Sleep 100
		Click
	}
	return
}