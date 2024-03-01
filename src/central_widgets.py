from PyQt5 import QtWidgets
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk
import os

from camera_style import CustomInteractorStyle

class CentralWidget(QtWidgets.QWidget):
    
    VTK_WINDOW_WIDTH = 400
    VTK_WINDOW_HEIGHT = 300
    OBJ_FILE = "assets/The-King-In-Yellow/the_king_in_yellow.obj"
    MTL_FILE = "assets/The-King-In-Yellow/the_king_in_yellow.mtl"

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupGrids()
        self.setupTabs()
        self.setupGroupBoxes()
        self.placeVTK()
        self.placeGroupBoxes()
        self.setupInputFields()
        self.setupLabels()
        self.placeFormLayoutItems()
        self.setupVTK()


    def setupTabs(self):

        self.PlaceholderLabel1 = QtWidgets.QLabel("This is the 2nd tab!")

        self.gridWidget = QtWidgets.QWidget()
        self.gridWidget.setLayout(self.grid1)

        self.gridWrapperLayout = QtWidgets.QVBoxLayout(self)

        self.tabWidget = QtWidgets.QTabWidget(self)

        self.gridWrapperLayout.addWidget(self.tabWidget)
        self.tabWidget.addTab(self.gridWidget, "Inventory")
        

    def setupGrids(self):

        self.grid1 = QtWidgets.QGridLayout()
        self.setLayout(self.grid1)
        

    def setupGroupBoxes(self):

        self.inspectGroup = QtWidgets.QGroupBox()
        self.inspectGroup.setTitle("Inspect")

        self.statsGroup = QtWidgets.QGroupBox()
        self.statsGroup.setTitle("Stats")

        self.listGroup = QtWidgets.QGroupBox()
        self.listGroup.setTitle("Table")


    def placeVTK(self):

        self.vtkWidget = QVTKRenderWindowInteractor(self.inspectGroup)
        self.vtkWidget.setFixedSize(self.VTK_WINDOW_WIDTH, self.VTK_WINDOW_HEIGHT)

        self.inspectVertLayout = QtWidgets.QVBoxLayout()
        self.inspectVertLayout.addWidget(self.vtkWidget)
        self.inspectGroup.setLayout(self.inspectVertLayout)


    def placeGroupBoxes(self):

        self.grid1.addWidget(self.inspectGroup, 0, 0)
        self.grid1.addWidget(self.statsGroup, 0, 1)
        self.grid1.addWidget(self.listGroup, 1, 0, 1, 2)


    def setupInputFields(self):

        self.bookNameField = QtWidgets.QLineEdit()
        self.bookNameField.setObjectName("statFieldOne")

        self.bookAuthorField = QtWidgets.QLineEdit()
        self.bookAuthorField.setObjectName("statFieldTwo")

        self.bookPrintDateField = QtWidgets.QLineEdit()
        self.bookPrintDateField.setObjectName("statFieldThree")

        self.bookCategoryField = QtWidgets.QLineEdit()
        self.bookCategoryField.setObjectName("statFieldFour")

        self.bookPublisherField = QtWidgets.QLineEdit()
        self.bookPublisherField.setObjectName("statFieldFive")

        self.bookLanguageField = QtWidgets.QLineEdit()
        self.bookLanguageField.setObjectName("statFieldSix")

        self.bookCoverTypeField = QtWidgets.QLineEdit()
        self.bookCoverTypeField.setObjectName("statFieldSeven")


    def setupLabels(self):

        self.bookName = QtWidgets.QLabel()
        self.bookName.setText("Book Name")

        self.bookAuthor =  QtWidgets.QLabel()
        self.bookAuthor.setText("Book Author")

        self.bookPrintDate = QtWidgets.QLabel()
        self.bookPrintDate.setText("Book Print Date")

        self.bookCategory = QtWidgets.QLabel()
        self.bookCategory.setText("Book Category")

        self.bookPublisher = QtWidgets.QLabel()
        self.bookPublisher.setText("Book Publisher")

        self.bookLanguage = QtWidgets.QLabel()
        self.bookLanguage.setText("Book Language")

        self.bookCoverType = QtWidgets.QLabel()
        self.bookCoverType.setText("Book Cover Type")

        
    def placeFormLayoutItems(self):

        self.statsFormLayout = QtWidgets.QFormLayout()

        self.statsFormLayout.addRow(self.bookName, self.bookNameField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookAuthor, self.bookAuthorField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookPrintDate, self.bookPrintDateField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookCategory, self.bookCategoryField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookPublisher, self.bookPublisherField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookLanguage, self.bookLanguageField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookCoverType, self.bookCoverTypeField)
        self.statsGroup.setLayout(self.statsFormLayout)
        

    def setupVTK(self):

        importer = vtk.vtkOBJImporter()
        importer.SetFileName(self.OBJ_FILE)
        importer.SetFileNameMTL(self.MTL_FILE)
        
        obj_dir = os.path.dirname(self.OBJ_FILE)

        importer.SetTexturePath(obj_dir)

        self.renderer = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)

        importer.SetRenderWindow(self.vtkWidget.GetRenderWindow())
        importer.Update()

        # Annotations

        self.textActor = vtk.vtkTextActor()
        self.textActor.SetInput("The King in Yellow")
        self.textActor.GetTextProperty().SetFontSize(10)
        self.textActor.GetTextProperty().SetColor(0, 0, 0)

        self.renderer.AddActor(self.textActor)

        # Shader

        # If this is still a case of shader

        # -> Use built-in shader methods
        # -> Completely override the shader methods
        
        
        # ------------------------------------------------------------------------

        self.renderWindowInteractor = self.vtkWidget.GetRenderWindow().GetInteractor()
        style = vtk.vtkInteractorStyleTrackballCamera()
        self.renderWindowInteractor.SetInteractorStyle(style)

        self.renderer.SetBackground(0.5, 0.5, 0.5)
        self.renderer.ResetCamera()

        style = CustomInteractorStyle(self.renderer)
        self.renderWindowInteractor.SetInteractorStyle(style)

        self.renderWindowInteractor.Initialize()
