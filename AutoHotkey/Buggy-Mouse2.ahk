RButton::	
	If (A_TimeSincePriorHotkey < 80) ;hyperclick
		Return
	Click Down Right
	KeyWait, RButton
	Click Up Right
Return