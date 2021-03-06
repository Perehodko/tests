'''
Проверка текста на соответствие в форме.
'''
def init():
    source(findFile("scripts", "script_file_squish.py"))
    all()
    initial_PTS()
    geocalc()
    
def main():      
    startApplication("ArmkApplication")
    clickButton(waitForObject(route_b)) 
    clickButton(waitForObject(geo_calc_b)) 
    clickButton(waitForObject(OGZ_rb))
    
    test.startSection("Проверка на соответствие текста задачи")
    test.compare(str(waitForObjectExists(":mainWidget.qrb_plain_QRadioButton").text), "Плоскость")
    test.compare(str(waitForObjectExists(":mainWidget.qrb_sphere_QRadioButton").text), "Сфера")
    test.compare(str(waitForObjectExists(":qstw_mode.label_17_QLabel").text), "Точка №1")
    test.compare(str(waitForObjectExists(":qstw_mode.qlbl_ogzXB_QLabel").text), "X = ")
    test.compare(str(waitForObjectExists(":qstw_mode.qlbl_ogzYL_QLabel").text), "Y = ")
    test.compare(str(waitForObjectExists(":qstw_mode.label_20_QLabel").text), "Точка №2")
    test.compare(str(waitForObjectExists(":qstw_mode.qlbl_ogzXB2_QLabel").text), "X = ")
    test.compare(str(waitForObjectExists(":qstw_mode.qlbl_ogzYL2_QLabel").text), "Y = ")
    test.compare(str(waitForObjectExists(":qstw_mode.label_14_QLabel").text), "Направление и расстояние")
    test.compare(str(waitForObjectExists(":qstw_mode.qlbl_ogzXBR_QLabel").text), "S = ")
    test.compare(str(waitForObjectExists(":qstw_mode.qlbl_ogzYLR_QLabel").text), "A = ")     
    test.endSection()
