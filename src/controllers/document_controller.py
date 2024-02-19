from models import get_document
from views import DocumentGenerator

class DocumentController:
    def __init__(self):
        """
        Initializes a new instance of the DocumentController class.
        """
        self.document = get_document()

    def create_pdf(self):
        """
        Creates a PDF document using the DocumentGenerator class.

        Parameters:
            None

        Returns:
            None
        """
        DocumentGenerator("document.pdf", self.document)


document_controller = DocumentController()
document_controller.create_pdf()