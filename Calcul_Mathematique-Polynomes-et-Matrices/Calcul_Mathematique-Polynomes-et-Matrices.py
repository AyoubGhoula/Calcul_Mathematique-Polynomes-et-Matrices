import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
import numpy as np
def div_polynome(self,dividende, diviseur):
    deg_dividende = len(dividende) - 1
    deg_diviseur = len(diviseur) - 1

    if deg_diviseur < 0:
        self.reselt_add_7.setText("Le diviseur ne peut pas être le polynôme nul.")

    if deg_dividende < deg_diviseur:
        return [], dividende

    quotient = [0] * (deg_dividende - deg_diviseur + 1)

    while deg_dividende >= deg_diviseur:
        coef = dividende[deg_dividende] / diviseur[deg_diviseur]
        quotient[deg_dividende - deg_diviseur] = coef

        for i in range(deg_diviseur + 1):
            dividende[deg_dividende - i] -= coef * diviseur[deg_diviseur - i]

        deg_dividende -= 1

    reste = dividende[:deg_diviseur]
    return quotient, reste
def polyProd(P, Q) :
  R=[0]*(len(Q)+len(P)-1)
  for i in range(len(P)-1,-1,-1):
    for j in range(len(Q)-1,-1,-1):
      R[i+j]=R[i+j]+(P[i]*Q[j])  
  return R
def sous_polynome(p1,p2):
        res = [0] * max(len(p1), len(p2))
        for i in range(len(p1)):
                    res[i] += p1[i]
        for i in range(len(p2)):
                    res[i] -= p2[i]
        return res
def add_polynome(p1,p2):
        res = [0] * max(len(p1), len(p2))
        for i in range(len(p1)):
                    res[i] += p1[i]
        for i in range(len(p2)):
                    res[i] += p2[i]
        return res

class polynome():
	def __init__(self,pol):
		self.pol = pol
		self.num = "0123456789"
		self.oper = "-+*/()"
		self.elemnts = []
		self.mat = []
	def Clean(self):
		for i in range(len(self.pol)-self.pol.count(" ")):
			if self.pol[i] == " ":
				self.pol[i] =self.pol[:i] + self.pol[i+1:]
	def Collect(self):
		j = -1
		for i in range(0,len(self.pol)) :
			if self.pol[i] in self.oper:
				self.elemnts.append(self.pol[j+1:i])
				self.elemnts.append(self.pol[i])
				self.pol = "#"*i + self.pol[i:]
				j = i
		self.elemnts.append(self.pol[j+1:])
		if self.elemnts[0] == "":
			self.elemnts = self.elemnts[1:]
	def ConvertToIntMat(self):
		x = ""
		for i in self.elemnts:
			if i == "-" or i == "+":
				x = i
			elif i.find("^") != -1:
				x = int(x+i[:i.find("x")])
				y = int(i[i.find("^")+1:])
				self.mat.append([x,y])
				x = ""
				y = ""
			elif i.find("x") != -1:
				if x+i[:i.find("x")] not in self.oper :
					x = int(x+i[:i.find("x")])
					y = 1
					self.mat.append([x,y])
					x = ""
					y = ""
				else:
					x = int(x+"1")
					y = 1
					self.mat.append([x,y])
					x = ""
					y = ""
			else :
				x = int(x+i)
				self.mat.append([x,0])
				x = ""
				y = ""
	def Filtrer(self):
		for i in range(len(self.mat)):
			j = i+1
			while(j < len(self.mat)):
				if self.mat[i][1] == self.mat[j][1]:
					self.mat[i][0] += self.mat[j][0]
					self.mat[j] = ["y","y"]
				j += 1

		self.mat = [i for i in self.mat if i != ["y","y"]]
		#print(self.mat)
		mat1=[]
		mat2=self.mat
		while len(mat2)!=len(mat1):
                        m=mat2[0][1]
                        s=0
                        for j in range(len(mat2)):
                                if mat2[j][1]>m :
                                    m=mat2[j][1]
                                    s=j
                        mat1.append(mat2[s])
                        mat2[s]=[0,-1111]
        
		tap=[0 for i in range(mat1[0][1]+1)]
		for i in range(len(mat1)):
                    tap[mat1[i][1]]=mat1[i][0]
		return tap
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('Calcul_Mathematique-Polynomes-et-Matrices_QT_DESIGNER.ui', self)

        # add
        self.reslt_add.clicked.connect(self.add_matrices)
        self.cree_add.clicked.connect(self.ceer_matrices_add)
        self.remis_add.clicked.connect(self.remis_matrices_add)
        #sous
        self.reslt_sos.clicked.connect(self.sos_matrices)
        self.ceer_sos.clicked.connect(self.ceer_matrices_sos)
        self.remis_sos.clicked.connect(self.remis_matrices_sos)
        #mul
        self.reslt_mul.clicked.connect(self.mul_matrices)
        self.cree_mul.clicked.connect(self.ceer_matrices_mul)
        self.remis_mul.clicked.connect(self.remis_matrices_mul)
        #det
        self.reslt_det.clicked.connect(self.det_matrices)
        self.cree_det.clicked.connect(self.ceer_matrices_det)
        self.remis_det.clicked.connect(self.remis_matrices_det)
        self.revers.clicked.connect(self.revers_matrices_det)
        #add_pol
        self.reselt_add_2.clicked.connect(self.add_pol1)
        #mul_pol
        self.reselt_add_3.clicked.connect(self.mul_pol)
        #sous_pol
        self.remis_mul_2.clicked.connect(self.sous_pol)
        #div_pol
        self.reselt_add_5.clicked.connect(self.div_pol)
        self.pushButton_3.clicked.connect(self.style)
        self.pushButton_7.clicked.connect(self.style2)
        self.remis_add_6.clicked.connect(self.clen)
        self.remis_add_5.clicked.connect(self.clen)
        self.remis_add_3.clicked.connect(self.clen)
        self.remis_add_2.clicked.connect(self.clen)
    def style2(self):
        self.pushButton_3.setStyleSheet("QPushButton"
                                        "{"
                                        "color: rgb(205, 231, 255);"
                                        "border-radius: 10px;"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(0, 0, 103, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "border: none;"
                                        "padding-top: 5px;"
                                        "font: 75 12pt 'Arial';"
                                        "border-left: 2px solid  rgb(0, 0, 0);"
                                        "border-bottom: 2px solid  rgb(0, 0, 0);"
                                        "}"
                                        "QPushButton:hover"
                                        "{"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(36, 13, 137, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "}"
                                        "QPushButton:pressed"
                                        "{"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(0, 0, 187, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "}")
        self.pushButton_7.setStyleSheet("QPushButton"
                                        "{"
                                        "color: rgb(205, 231, 255);"
                                        "border-radius: 10px;"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(0, 0, 103, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "padding-top: 5px;"
                                        "font: 75 12pt 'Arial';"
                                        "}"
                                        "QPushButton:hover"
                                        "{"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(36, 13, 137, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "}"
                                        "QPushButton:pressed"
                                        "{"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(0, 0, 187, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "}")
    def style(self):
        self.pushButton_3.setStyleSheet("QPushButton"
                                        "{"
                                        "color: rgb(205, 231, 255);"
                                        "border-radius: 10px;"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(0, 0, 103, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "border: none;"
                                        "padding-top: 5px;"
                                        "font: 75 12pt 'Arial';"
                                        "}"
                                        "QPushButton:hover"
                                        "{"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(36, 13, 137, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "}"
                                        "QPushButton:pressed"
                                        "{"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(0, 0, 187, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "}")
        self.pushButton_7.setStyleSheet("QPushButton"
                                        "{"
                                        "color: rgb(205, 231, 255);"
                                        "border-radius: 10px;"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(0, 0, 103, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "border-left: 2px solid  rgb(0, 0, 0);"
                                        "border-bottom: 2px solid  rgb(0, 0, 0);"
                                        "padding-top: 5px;"
                                        "font: 75 12pt 'Arial';"
                                        "}"
                                        "QPushButton:hover"
                                        "{"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(36, 13, 137, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "}"
                                        "QPushButton:pressed"
                                        "{"
                                        "background-color: qlineargradient(spread:pad, x1:0.886, y1:0.119318, x2:1, y2:0, stop:0 rgba(0, 0, 187, 255), stop:1 rgba(255, 255, 255, 255));"
                                        "}")
    def remis_matrices_det(self):
        for i in range(self.tab_a_det.columnCount()):
            self.tab_a_det.removeColumn(0)
        for i in range(self.tab_a_det.rowCount()):
            self.tab_a_det.removeRow(0)
        for i in range(self.tab_b_det.columnCount()):
            self.tab_b_det.removeColumn(0)
        for i in range(self.tab_b_det.rowCount()):
            self.tab_b_det.removeRow(0)
        self.c1_det.setValue(0)
        self.erreur3.clear()
        self.det.clear()
    def remis_matrices_mul(self):
        for i in range(self.tab_a_mul.columnCount()):
            self.tab_a_mul.removeColumn(0)
        for i in range(self.tab_a_mul.rowCount()):
            self.tab_a_mul.removeRow(0)
        for i in range(self.tab_b_mul.columnCount()):
            self.tab_b_mul.removeColumn(0)
        for i in range(self.tab_b_mul.rowCount()):
            self.tab_b_mul.removeRow(0)
        for i in range(self.tab_c_mul.columnCount()):
            self.tab_c_mul.removeColumn(0)
        for i in range(self.tab_c_mul.rowCount()):
            self.tab_c_mul.removeRow(0)
        self.c1_mul.setValue(0)
        self.c2_mul.setValue(0)
        self.l1_mul.setValue(0)
        self.l2_mul.setValue(0)
        self.erreur2.clear()
    def remis_matrices_add(self):
        for i in range(self.tab_a_add.columnCount()):
            self.tab_a_add.removeColumn(0)
        for i in range(self.tab_a_add.rowCount()):
            self.tab_a_add.removeRow(0)
        for i in range(self.tab_b_add.columnCount()):
            self.tab_b_add.removeColumn(0)
        for i in range(self.tab_b_add.rowCount()):
            self.tab_b_add.removeRow(0)
        for i in range(self.tab_c_add.columnCount()):
            self.tab_c_add.removeColumn(0)
        for i in range(self.tab_c_add.rowCount()):
            self.tab_c_add.removeRow(0)
        self.c1_add.setValue(0)
        self.l1_add.setValue(0)
        self.erreur.clear()
    def remis_matrices_sos(self):
        for i in range(self.tab_a_sos.columnCount()):
            self.tab_a_sos.removeColumn(0)
        for i in range(self.tab_a_sos.rowCount()):
            self.tab_a_sos.removeRow(0)
        for i in range(self.tab_b_sos.columnCount()):
            self.tab_b_sos.removeColumn(0)
        for i in range(self.tab_b_sos.rowCount()):
            self.tab_b_sos.removeRow(0)
        for i in range(self.tab_c_sos.columnCount()):
            self.tab_c_sos.removeColumn(0)
        for i in range(self.tab_c_sos.rowCount()):
            self.tab_c_sos.removeRow(0)
        self.c1_sos.setValue(0)
        self.l1_sos.setValue(0)
        self.erreur1.clear()
    def ceer_matrices_det(self):
        self.erreur3.clear()
        c1_det= self.c1_det.value()
        self.tab_a_det.setRowCount(c1_det)
        self.tab_a_det.setColumnCount(c1_det)
        for i in range(c1_det):
                self.tab_a_det.setColumnWidth(i,20)
    def ceer_matrices_mul(self):
        self.erreur2.clear()
        c1_mul= self.c1_mul.value()
        l1_mul= self.l1_mul.value()
        c2_mul= self.c2_mul.value()
        l2_mul= self.l2_mul.value()
        if c1_mul!=l2_mul:
            self.erreur2.setText("n’est défini que si le nombre de colonnes de mat1 est égal au nombre de lignes de mat2.")
        else :
            self.tab_a_mul.setRowCount(l1_mul)
            self.tab_a_mul.setColumnCount(c1_mul)
            self.tab_b_mul.setRowCount(l2_mul)
            self.tab_b_mul.setColumnCount(c2_mul)
            for i in range(c1_mul):
                self.tab_a_mul.setColumnWidth(i,20)
            for i in range(c2_mul):
                self.tab_b_mul.setColumnWidth(i,20)
    def ceer_matrices_add(self):
        self.erreur1.clear()
        c1_add= self.c1_add.value()
        l1_add= self.l1_add.value()
        c2_add= self.c1_add.value()
        l2_add= self.l1_add.value()
        if c1_add!=c2_add or l1_add!=l2_add:
            self.erreur1.setText("les deux matrices ne sont pas de même taille.")
        else :
            self.tab_a_add.setRowCount(l1_add)
            self.tab_a_add.setColumnCount(c1_add)
            self.tab_b_add.setRowCount(l2_add)
            self.tab_b_add.setColumnCount(c2_add)
            for i in range(c1_add):
                self.tab_a_add.setColumnWidth(i,20)
            for i in range(c2_add):
                self.tab_b_add.setColumnWidth(i,20)
    def ceer_matrices_sos(self):
        self.erreur1.clear()
        c1_sos= self.c1_sos.value()
        l1_sos= self.l1_sos.value()
        c2_sos= self.c1_sos.value()
        l2_sos= self.l1_sos.value()
        if c1_sos!=c2_sos or l1_sos!=l2_sos:
            self.erreur.setText("les deux matrices ne sont pas de même taille.")
        else :
            self.tab_a_sos.setRowCount(l1_sos)
            self.tab_a_sos.setColumnCount(c1_sos)
            self.tab_b_sos.setRowCount(l2_sos)
            self.tab_b_sos.setColumnCount(c2_sos)
            for i in range(c1_sos):
                self.tab_a_sos.setColumnWidth(i,20)
            for i in range(c2_sos):
                self.tab_b_sos.setColumnWidth(i,20)
    def sos_matrices(self):
        matrix_a = []
        for i in range(self.tab_a_sos.rowCount()):
            row = []
            for j in range(self.tab_a_sos.columnCount()):
                item = self.tab_a_sos.item(i, j)
                if item is not None and item.text() != '':
                    row.append(int(item.text()))
                else:
                    row.append(0)
            matrix_a.append(row)

        matrix_b = []
        for i in range(self.tab_b_sos.rowCount()):
            row = []
            for j in range(self.tab_b_sos.columnCount()):
                item = self.tab_b_sos.item(i, j)
                if item is not None and item.text() != '':
                    row.append(int(item.text()))
                else:
                    row.append(0)
            matrix_b.append(row)
        if matrix_a!=[] and matrix_b!=[]:
            result = np.subtract(matrix_a, matrix_b)

            self.tab_c_sos.setRowCount(len(result))
            self.tab_c_sos.setColumnCount(len(result[0]))
            for i in range(len(result)):
                for j in range(len(result[0])):
                    item = QTableWidgetItem(str(result[i][j]))
                    self.tab_c_sos.setItem(i, j, item)
            for i in range(len(result[0])):
                self.tab_c_sos.setColumnWidth(i,20)   
    def add_matrices(self):
        matrix_a = []
        for i in range(self.tab_a_add.rowCount()):
            row = []
            for j in range(self.tab_a_add.columnCount()):
                item = self.tab_a_add.item(i, j)
                if item is not None and item.text() != '':
                    row.append(int(item.text()))
                else:
                    row.append(0)
            matrix_a.append(row)

        matrix_b = []
        for i in range(self.tab_b_add.rowCount()):
            row = []
            for j in range(self.tab_b_add.columnCount()):
                item = self.tab_b_add.item(i, j)
                if item is not None and item.text() != '':
                    row.append(int(item.text()))
                else:
                    row.append(0)
            matrix_b.append(row)
        if matrix_a!=[] and matrix_b!=[]:
            result = np.add(matrix_a, matrix_b)

            self.tab_c_add.setRowCount(len(result))
            self.tab_c_add.setColumnCount(len(result[0]))
            for i in range(len(result)):
                for j in range(len(result[0])):
                    item = QTableWidgetItem(str(result[i][j]))
                    self.tab_c_add.setItem(i, j, item)
            for i in range(len(result[0])):
                self.tab_c_add.setColumnWidth(i,20)
    def revers_matrices_det(self):
        matrix_a = []
        for i in range(self.tab_a_det.rowCount()):
            row = []
            for j in range(self.tab_a_det.columnCount()):
                item = self.tab_a_det.item(i,j)
                if item is not None and item.text() != '':
                    row.append(int(item.text()))
                else:
                    row.append(0)
            matrix_a.append(row)
        if matrix_a!=[]:
            m= np.linalg.det(matrix_a)
            if int(m)==0:
                self.erreur3.setText("Le determinant est nul.")
            else:
                result = np.linalg.inv(matrix_a)
                self.tab_b_det.setRowCount(len(result))
                self.tab_b_det.setColumnCount(len(result[0]))
                for i in range(len(result)):
                    for j in range(len(result[0])):
                        item = QTableWidgetItem(str((result[i][j])))
                        self.tab_b_det.setItem(i, j, item)
                for i in range(len(result[0])):
                    self.tab_b_det.setColumnWidth(i,20)
    def det_matrices(self):
        matrix_a = []
        for i in range(self.tab_a_det.rowCount()):
            row = []
            for j in range(self.tab_a_det.columnCount()):
                item = self.tab_a_det.item(i,j)
                if item is not None and item.text() != '':
                    row.append(int(item.text()))
                else:
                    row.append(0)
        
            matrix_a.append(row)
        if matrix_a!=[] :
            result= np.linalg.det(matrix_a)
            if result<0:
                self.det.setText(str(int(result-0.0000001)))
            else :
                self.det.setText(str(int(result+0.0000001)))
    def mul_pol(self):
        x1=self.pol1_mul.text()
        if x1 !='' :
            polynome1 = polynome(x1)
            polynome1.Clean()
            polynome1.Collect()
            polynome1.ConvertToIntMat()
            mat1 = polynome1.Filtrer()
        x2=self.pol2_mul.text()
        if x1 !='' and x2!='':
            polynome2 = polynome(x2)
            polynome2.Clean()
            polynome2.Collect()
            polynome2.ConvertToIntMat()
            mat2 = polynome2.Filtrer()
            rus=polyProd(mat1,mat2)
            ruselt=''
            for i in range(len(rus)):
                if i==0:
                   if i==0:
                    if rus[0]>0:
                        ruselt=ruselt+'+'+str(rus[0])
                    elif rus[0]<0:
                        ruselt=ruselt+str(rus[0])
                elif i==1:
                    if rus[1]>0:
                        ruselt='+'+str(rus[1])+'x'+ruselt
                    elif rus[1]<0:
                        ruselt=str(rus[1])+'x'+ruselt
                else:
                    if rus[i]>0:
                        ruselt='+'+str(rus[i])+'x^'+str(i)+ruselt
                    elif rus[i]<0:
                        ruselt=str(rus[i])+'x^'+str(i)+ruselt
            if ruselt!='':
                if ruselt[0]=='+':
                    ruselt=ruselt[1::]
            else:
                ruselt='0'
            self.reselt_add_4.setText(ruselt)
    def add_pol1(self):
        #x1 = "3x^2 + 9"
        x1=self.pol1_add.text()
        if x1 !='':
            polynome1 = polynome(x1)
            polynome1.Clean()
            polynome1.Collect()
            polynome1.ConvertToIntMat()
            mat1 = polynome1.Filtrer()
        #x2 = "+4x -9"
        x2=self.pol2_add.text()
        if x1 !='' and x2!='' :
            polynome2 = polynome(x2)
            polynome2.Clean()
            polynome2.Collect()
            polynome2.ConvertToIntMat()
            mat2 = polynome2.Filtrer()
            rus=add_polynome(mat1, mat2)
            ruselt=''
            for i in range(len(rus)):
                if i==0:
                    if rus[0]>0:
                        ruselt=ruselt+'+'+str(rus[0])
                    elif rus[0]<0:
                        ruselt=ruselt+str(rus[0])
                elif i==1:
                    if rus[1]>0:
                        ruselt='+'+str(rus[1])+'x'+ruselt
                    elif rus[1]<0:
                        ruselt=str(rus[1])+'x'+ruselt
                else:
                    if rus[i]>0:
                        ruselt='+'+str(rus[i])+'x^'+str(i)+ruselt
                    elif rus[i]<0:
                        ruselt=str(rus[i])+'x^'+str(i)+ruselt
            if ruselt!='':
                if ruselt[0]=='+':
                    ruselt=ruselt[1::]
            else:
                ruselt='0'
            self.reselt_add.setText(ruselt)

    def sous_pol(self):
        #x1 = "3x^2 + 9"
        x1=self.pol2_add_2.text()
        if x1 !='':
            polynome1 = polynome(x1)
            polynome1.Clean()
            polynome1.Collect()
            polynome1.ConvertToIntMat()
            mat1 = polynome1.Filtrer()
        #x2 = "+4x -9"
        x2=self.pol2_add_3.text()
        if x1 !='' and x2!='':   
            polynome2 = polynome(x2)
            polynome2.Clean()
            polynome2.Collect()
            polynome2.ConvertToIntMat()
            mat2 = polynome2.Filtrer()
            rus=sous_polynome(mat1, mat2)
            ruselt=''
            for i in range(len(rus)):
                if i==0:
                    if rus[0]>0:
                        ruselt=ruselt+'+'+str(rus[0])
                    elif rus[0]<0:
                        ruselt=ruselt+str(rus[0])
                elif i==1:
                    if rus[1]>0:
                        ruselt='+'+str(rus[1])+'x'+ruselt
                    elif rus[1]<0:
                        ruselt=str(rus[1])+'x'+ruselt
                else:
                    if rus[i]>0:
                        ruselt='+'+str(rus[i])+'x^'+str(i)+ruselt
                    elif rus[i]<0:
                        ruselt=str(rus[i])+'x^'+str(i)+ruselt
            if ruselt!='':
                if ruselt[0]=='+':
                    ruselt=ruselt[1::]
            else:
                ruselt='0'
            self.label_27.setText(ruselt)

    def clen(self):
        self.pol1_add.clear()
        self.pol2_add.clear()
        self.reselt_add.clear()
        self.pol2_add_2.clear()
        self.pol2_add_3.clear()
        self.label_27.clear()
        self.pol1_mul.clear()
        self.pol2_mul.clear()
        self.reselt_add_4.clear()
        self.pol1_add_3.clear()
        self.pol2_add_5.clear()
        self.reselt_add_6.clear()
        self.reselt_add_7.clear()
        
    def div_pol(self):
        #x1 = "3x^2 + 9"
        x1=self.pol1_add_3.text()
        if x1 !='':
            polynome1 = polynome(x1)
            polynome1.Clean()
            polynome1.Collect()
            polynome1.ConvertToIntMat()
            mat1 = polynome1.Filtrer()
        #x2 = "+4x -9"
        x2=self.pol2_add_5.text()
        if x2 !='':
            polynome2 = polynome(x2)
            polynome2.Clean()
            polynome2.Collect()
            polynome2.ConvertToIntMat()
            mat2 = polynome2.Filtrer()
        if x2 !='' and mat2!=[0] and x1!='':
            ques,rest=div_polynome(mat1, mat2)
            ruselt=''
            for i in range(len(ques)):
                if i==0:
                    if ques[0]>0:
                        ruselt=ruselt+'+'+str(ques[0])
                    elif ques[0]<0:
                        ruselt=ruselt+str(ques[0])
                elif i==1:
                    if ques[1]>0:
                        ruselt='+'+str(ques[1])+'x'+ruselt
                    elif ques[1]<0:
                        ruselt=str(ques[1])+'x'+ruselt
                else:
                    if ques[i]>0:
                        ruselt='+'+str(ques[i])+'x^'+str(i)+ruselt
                    elif ques[i]<0:
                        ruselt=str(ques[i])+'x^'+str(i)+ruselt
            if ruselt!='':
                if ruselt[0]=='+':
                    ruselt=ruselt[1::]
            else:
                ruselt='0'
            self.reselt_add_6.setText(ruselt)
            ruselt=''
            for i in range(len(rest)):
                if i==0:
                    if rest[0]>0:
                        ruselt=ruselt+'+'+str(rest[0])
                    elif rest[0]<0:
                        ruselt=ruselt+str(rest[0])
                elif i==1:
                    if rest[1]>0:
                        ruselt='+'+str(rest[1])+'x'+ruselt
                    elif rest[1]<0:
                        ruselt=str(rest[1])+'x'+ruselt
                else:
                    if rest[i]>0:
                        ruselt='+'+str(rest[i])+'x^'+str(i)+ruselt
                    elif rest[i]<0:
                        ruselt=str(rest[i])+'x^'+str(i)+ruselt
            if ruselt!='':
                if ruselt[0]=='+':
                    ruselt=ruselt[1::]
            else:
                ruselt='0'
            self.reselt_add_7.setText(ruselt)
        else:
            self.reselt_add_7.setText("le polynôme nul.")
    def mul_matrices(self):
        matrix_a = []
        for i in range(self.tab_a_mul.rowCount()):
            row = []
            for j in range(self.tab_a_mul.columnCount()):
                item = self.tab_a_mul.item(i, j)
                if item is not None and item.text() != '':
                    row.append(int(item.text()))
                else:
                    row.append(0)
            matrix_a.append(row)

        matrix_b = []
        for i in range(self.tab_b_mul.rowCount()):
            row = []
            for j in range(self.tab_b_mul.columnCount()):
                item = self.tab_b_mul.item(i, j)
                if item is not None and item.text() != '':
                    row.append(int(item.text()))
                else:
                    row.append(0)
            matrix_b.append(row)
        if matrix_a!=[] and matrix_b!=[]:
            result = np.matmul(matrix_a, matrix_b)

            self.tab_c_mul.setRowCount(len(result))
            self.tab_c_mul.setColumnCount(len(result[0]))
            for i in range(len(result)):
                for j in range(len(result[0])):
                    item = QTableWidgetItem(str(result[i][j]))
                    self.tab_c_mul.setItem(i, j, item)
            for i in range(len(result[0])):
                self.tab_c_mul.setColumnWidth(i,20)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())