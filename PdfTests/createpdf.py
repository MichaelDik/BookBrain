from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_hello_world_pdf(output_path):
    # Create a new PDF with letter size
    c = canvas.Canvas(output_path, pagesize=letter)
    
    # Add text
    c.drawString(100, 750, "Hello World")
    
    # Save the PDF
    c.save()

if __name__ == "__main__":
    create_hello_world_pdf("test.pdf")