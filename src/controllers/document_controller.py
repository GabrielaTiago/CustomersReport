from models import get_document
from views import DocumentGenerator

class DocumentController:
    def __init__(self):
        self.document = get_document()

    def create_pdf(self):
        DocumentGenerator("document.pdf", self.document)


document_controller = DocumentController()
document_controller.create_pdf()