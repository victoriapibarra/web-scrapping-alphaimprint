# CÓDIGO PARA EXTRAER HYPERLIKS EN EXCEL

Sub ExtractHyperlinks()
    Dim cell As Range
    Dim column As Range
    
    ' Change the range based on your needs, here it's column A
    Set column = Range("A1:A100") ' Adjust the range based on your data
    
    For Each cell In column
        If cell.Hyperlinks.Count > 0 Then
            cell.Offset(0, 1).Value = cell.Hyperlinks(1).Address ' Extract the URL to column B
        End If
    Next cell
End Sub
