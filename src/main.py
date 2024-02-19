from controllers import DocumentController

def main():
    """
    This is the main function that initializes the DocumentController
    and calls the create_pdf method to generate a PDF document.
    """
    document_controller = DocumentController()
    document_controller.create_pdf()

if __name__ == "__main__":
    main()