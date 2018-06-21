LButton::	
	If (A_TimeSincePriorHotkey < 80) ;hyperclick
		Return
	Click Down
	KeyWait, LButton
	Click Up
Return