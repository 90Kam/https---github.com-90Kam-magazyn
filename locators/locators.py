# EMPLOYEES MODULE
pracownicy_button = "//span[@class='toggle-text'][normalize-space()='Pracownicy']" # XPATH
add_employee_button = "//button[@type='button']" # XPATH
new_employee_name_input = "name" # NAME
new_employee_lastname_input = "lastName" # NAME
submit_adding_new_employee_button = "//button[text()='Dodaj']" # XPATH
filter_employee_button = "(//button[contains(@class,'MuiButtonBase-root MuiIconButton-root')])[2]" # XPATH
filter_name_input = "(//input[contains(@class,'MuiInputBase-input MuiInput-input')])[2]" # XPATH
filter_lastname_input = "(//input[contains(@class,'MuiInputBase-input MuiInput-input')])[3]" # XPATH
found_employee_name = "(//td[contains(@class,'MuiTableCell-root MuiTableCell-body')])[2]" # XPATH
found_employee_lastname = "(//td[contains(@class,'MuiTableCell-root MuiTableCell-body')])[3]" # XPATH
edit_employee_button = "//button[text()='Edytuj']" # XPATH

# DEPARTMENTS MODULE
submit_edit_employee_button = "//button[text()='Zapisz']" # XPATH
działy_button = "//a[@href='/departments']//div[@class='side-menu-toggle']" # XPATH
add_new_department_button = "//button[@type='button']" # XPATH
new_department_input = "name" # NAME
submit_adding_new_department = "//button[text()='Dodaj']" # XPATH
magnifier_button = "//button[contains(@class,'MuiButtonBase-root MuiIconButton-root')]" # XPATH
magnifier_input = "//input[contains(@class,'MuiInputBase-input MuiInput-input')]" # XPATH
found_department = "(//td[contains(@class,'MuiTableCell-root MuiTableCell-body')])[2]" # XPATH
edit_department_button = "//button[text()='Edytuj']" # XPATH
submit_edit_department_button = "//button[text()='Zapisz']" #XPATH

# SOURCES OF FOUNDING MODULE
zrodla_finansowania_button = "//span[text()='Źródła Finansowania']" # XPATH
add_source_of_founding_button = "//button[@type='button']" # XPATH
source_of_founding_input = "name" # NAME
submit_new_source_of_founding_button = "//button[text()='Dodaj']" # XPATH
edit_source_of_founding_button = "//button[text()='Edytuj']" # XPATH
found_source_of_founding_name = "(//td[contains(@class,'MuiTableCell-root MuiTableCell-body')])[2]" # XPATH
submit_edited_source_of_founding = "//button[text()='Zapisz']" # XPATH

# UNITS MODULE
jednostki_button = "//span[text()='Jednostki']" # XPATH
add_unit_button = "//button[contains(@class,'MuiButtonBase-root MuiButton-root')]" # XPATH
submit_new_unit = "//div[contains(@class,'MuiContainer-root MuiContainer-maxWidthXs')]//button[1]" # XPATH
edit_unit_button = "//button[text()='Edytuj']" # XPATH
edit_unit_input = "name" # NAME
add_unit_input = edit_unit_input
submit_edit_unit_button = "//button[text()='Zapisz']" # XPATH
founded_unit = "(//td[contains(@class,'MuiTableCell-root MuiTableCell-body')])[2]" # XPATH

# PRZYJECIA MODULE
przyjecia_button = "//span[text()='Przyjęcia']" # XPATH
dodaj_przyjecie_button = "//button[contains(@class,'MuiButtonBase-root MuiButton-root')]" # XPATH
nr_dokumentu_input = "invoiceNumber" # NAME
komentarz_input = "comment" # NAME
wybierz_kontrahenta_button = "//button[text()='Wybierz kontrahenta / klienta']" # XPATH
wybierz_projekt_button = "//button[text()='Wybierz Projekt']" # XPATH 
wybierz_zrodlo_finansowania_button = "//button[text()='Wybierz Źródło finansowania']" # XPATH
wybierz_przedmioty_button = "//button[text()='Wybierz przedmioty']" # XPATH
calendar_icon = "span#modal-conent>div>div>div>div>div:nth-of-type(3)>div>div>div>button" # CSS
day_button = "//button[text()='10']" # XPATH
wybierz_first_button = "//button[text()='Wybierz']" # XPATH
confirm_dodaj_przyjecie_button = "//button[text()='Dodaj']" # XPATH
x_button = "(//button[text()='X'])[2]" # XPATH
x_button2 = "//button[text()='X']" # XPATH

# WYDANIA WEWNETRZNE MODULE
wydania_wew_button = "//span[text()='Wydania Wewnętrzne']" # XPATH
dodaj_wydanie_wew_button = "//button[@type='button']" # XPATH
wybierz_pracownika_button = "//button[text()='Wybierz Pracownika']" # XPATH
confirm_dodaj_wydanie_wew_button = "//button[text()='Dodaj']" # XPATH

# WYDANIA ZEWNETRZNE MODULE
wydania_zew_button = "//span[text()='Wydania Zewnętrzne']" # XPATH
dodaj_wydanie_zew_button = "//button[@type='button']" # XPATH
confirm_dodaj_wydanie_zew_button = "//button[text()='Dodaj']" # XPATH

# ZWROTY MODULE
zwroty_button = "//span[text()='Zwroty']" # XPATH
dodaj_zwrot_button = "//button[@type='button']" # XPATH
confirm_dodaj_zwrot_button = "//button[text()='Dodaj']" # XPATH