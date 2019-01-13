get_text() {
    WinActive("A")
    ControlGetFocus, ctrl_edit
    if (RegExMatch(ctrl_edit, "A)Edit\d+")){
        ControlGet, outputVar, Selected,, %ctrl_edit%
        return % outputVar
    } else {
        Send, ^{Insert}
        clipboard_text_1 := Clipboard
        return, % clipboard_text_1



        ;if (Clipboard != clipboard_old) {
        ;}
    }
}
~LShift::
    if (A_ThisHotkey = A_PriorHotkey && A_TimeSincePriorHotkey < 250) {
        clipboard_old := Clipboard
        clipboard_text := get_text()
        Clipboard := clipboard_old
        WinActivate, 书香年华
    ;ToolTip, %clipboard_text%
}
return

;#if
;AppsKey & Esc::
;	ExitApp
;return
;AppsKey & Delete::
;	Reload

;return